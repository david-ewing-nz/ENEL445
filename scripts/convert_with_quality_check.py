"""
Enhanced PDF to Markdown converter with quality control
- Uses Marker for initial conversion
- Uses Surya-OCR for handwritten/problematic pages
- Generates quality reports for manual review
"""
import sys
sys.path.insert(0, 'D:\\Python_Packages')

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple
from marker.convert import convert_single_pdf
from marker.models import load_all_models
from PIL import Image
import json

# Surya-OCR imports
try:
    from surya.ocr import run_ocr
    from surya.model.detection.model import load_model as load_det_model, load_processor as load_det_processor
    from surya.model.recognition.model import load_model as load_rec_model
    from surya.model.recognition.processor import load_processor as load_rec_processor
    SURYA_AVAILABLE = True
except ImportError:
    print("Warning: Surya-OCR not available. Install with: pip install surya-ocr")
    SURYA_AVAILABLE = False

class QualityIssue:
    def __init__(self, page_num, issue_type, text_preview, char_count, image_path):
        self.page_num = page_num
        self.issue_type = issue_type
        self.text_preview = text_preview
        self.char_count = char_count
        self.image_path = image_path

def load_surya_models():
    """Load Surya-OCR models for fallback processing"""
    if not SURYA_AVAILABLE:
        return None
    
    try:
        print("  Loading Surya-OCR models...")
        det_model = load_det_model()
        det_processor = load_det_processor()
        rec_model = load_rec_model()
        rec_processor = load_rec_processor()
        return {
            'det_model': det_model,
            'det_processor': det_processor,
            'rec_model': rec_model,
            'rec_processor': rec_processor
        }
    except Exception as e:
        print(f"  Warning: Could not load Surya models: {e}")
        return None

def ocr_image_with_surya(image_path: Path, surya_models: Dict) -> str:
    """
    Run Surya-OCR on a single image
    Returns extracted text
    """
    if not surya_models:
        return "[Surya-OCR not available]"
    
    try:
        # Load image
        image = Image.open(image_path)
        images = [image]
        langs = [["en"]]  # English
        
        # Run OCR
        predictions = run_ocr(
            images,
            langs,
            surya_models['det_model'],
            surya_models['det_processor'],
            surya_models['rec_model'],
            surya_models['rec_processor']
        )
        
        # Extract text from predictions
        text_lines = []
        for pred in predictions[0].text_lines:
            text_lines.append(pred.text)
        
        return '\n'.join(text_lines)
        
    except Exception as e:
        return f"[Surya-OCR error: {e}]"

def analyze_page_quality(page_text: str, page_num: int) -> Tuple[bool, str]:
    """
    Analyze if a page conversion is good quality
    Returns: (is_good_quality, issue_description)
    """
    char_count = len(page_text.strip())
    
    # Check for very short content (likely blank or image-only)
    if char_count < 50:
        return False, f"Very short content ({char_count} chars) - likely blank or image-only page"
    
    # Check for high ratio of special characters (garbled OCR)
    alpha_count = sum(c.isalpha() for c in page_text)
    if char_count > 100 and alpha_count / char_count < 0.3:
        return False, f"High special char ratio - possibly garbled OCR"
    
    # Check for repeated error patterns
    if "���" in page_text or page_text.count("�") > 10:
        return False, "Contains many replacement characters - encoding issues"
    
    return True, "OK"

def split_markdown_by_pages(markdown_text: str) -> List[Tuple[int, str]]:
    """
    Split markdown into pages (best effort)
    Returns list of (page_num, page_text) tuples
    """
    # Marker doesn't always preserve page boundaries, so we'll estimate
    # by splitting on major section breaks or every ~2000 chars
    pages = []
    lines = markdown_text.split('\n')
    
    current_page = 1
    current_content = []
    char_count = 0
    
    for line in lines:
        current_content.append(line)
        char_count += len(line)
        
        # Heuristic: new page after ~2000 chars and a heading or double newline
        if char_count > 2000 and (line.startswith('#') or line == ''):
            pages.append((current_page, '\n'.join(current_content)))
            current_page += 1
            current_content = []
            char_count = 0
    
    # Add remaining content
    if current_content:
        pages.append((current_page, '\n'.join(current_content)))
    
    return pages

def convert_pdf_with_quality_check(pdf_path: Path, output_dir: Path, figs_dir: Path, use_surya: bool = True) -> Dict:
    """
    Convert a single PDF and check quality
    Returns quality report
    """
    print(f"\n{'='*80}")
    print(f"Converting: {pdf_path.name}")
    print(f"{'='*80}")
    
    # Load models
    print("Loading Marker models...")
    model_lst = load_all_models()
    
    # Load Surya models if available and requested
    surya_models = None
    if use_surya and SURYA_AVAILABLE:
        surya_models = load_surya_models()
    
    # Convert PDF to markdown
    print("Converting PDF to markdown...")
    full_text, images, out_meta = convert_single_pdf(
        str(pdf_path),
        model_lst,
        max_pages=None,
        langs=["English"],
        batch_multiplier=2
    )
    
    # Save markdown
    md_file = output_dir / f"{pdf_path.stem}.md"
    md_file.write_text(full_text, encoding='utf-8')
    print(f"✓ Saved markdown: {md_file.name}")
    
    # Save extracted images
    if images:
        img_dir = output_dir / f"{pdf_path.stem}_images"
        img_dir.mkdir(exist_ok=True)
        for img_name, img_data in images.items():
            img_path = img_dir / img_name
            img_path.write_bytes(img_data)
        print(f"✓ Saved {len(images)} extracted images")
    
    # Quality analysis
    print("\nAnalyzing quality...")
    issues = []
    
    # Check overall length
    total_chars = len(full_text)
    print(f"  Total characters: {total_chars:,}")
    
    if total_chars < 500:
        issues.append({
            'type': 'OVERALL_SHORT',
            'description': f'Very short document ({total_chars} chars)',
            'severity': 'HIGH'
        })
    
    # Split by pages and check each
    pages = split_markdown_by_pages(full_text)
    print(f"  Estimated pages: {len(pages)}")
    
    # Find corresponding figure folder
    fig_folder = figs_dir / pdf_path.stem
    
    problematic_pages = []
    surya_retries = []
    
    for page_num, page_text in pages:
        is_good, issue_desc = analyze_page_quality(page_text, page_num)
        
        if not is_good:
            # Find corresponding image
            image_path = None
            img_file = None
            if fig_folder.exists():
                img_file = fig_folder / f"page_{page_num:03d}.png"
                if img_file.exists():
                    image_path = str(img_file.relative_to(Path.cwd()))
            
            # Try Surya-OCR if available and image exists
            surya_text = None
            if surya_models and img_file and img_file.exists():
                print(f"    Retrying page {page_num} with Surya-OCR...")
                surya_text = ocr_image_with_surya(img_file, surya_models)
                surya_is_good, surya_issue = analyze_page_quality(surya_text, page_num)
                
                if surya_is_good:
                    print(f"    ✓ Surya-OCR improved page {page_num}")
                    surya_retries.append({
                        'page': page_num,
                        'improved': True,
                        'original_text': page_text[:200],
                        'surya_text': surya_text[:200]
                    })
                    continue  # Don't add to problematic pages
            
            problematic_pages.append({
                'page': page_num,
                'issue': issue_desc,
                'char_count': len(page_text),
                'text_preview': page_text[:200],
                'surya_text_preview': surya_text[:200] if surya_text else None,
                'surya_tried': surya_text is not None,
                'image_path': image_path
            })
    
    if problematic_pages:
        print(f"  ⚠ Found {len(problematic_pages)} problematic pages")
        issues.extend([{
            'type': 'PAGE_QUALITY',
            'pages': problematic_pages,
            'severity': 'MEDIUM'
        }])
    else:
        print(f"  ✓ All pages look good")
    
    if surya_retries:
        print(f"  ✓ Surya-OCR improved {len(surya_retries)} pages")
        issues.append({
            'type': 'SURYA_IMPROVEMENTS',
            'pages': surya_retries,
            'severity': 'INFO'
        })
    
    # Create report
    report = {
        'pdf_file': pdf_path.name,
        'output_file': md_file.name,
        'total_chars': total_chars,
        'estimated_pages': len(pages),
        'surya_improvements': len(surya_retries),
        'issues': issues,
        'status': 'NEEDS_REVIEW' if problematic_pages else 'OK'
    }
    
    return report

def generate_quality_report(reports: List[Dict], output_file: Path):
    """Generate a markdown report for manual review"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# PDF Conversion Quality Report\n\n")
        f.write(f"Generated: {Path(output_file).name}\n\n")
        f.write("---\n\n")
        
        for report in reports:
            f.write(f"## {report['pdf_file']}\n\n")
            f.write(f"- **Status**: {report['status']}\n")
            f.write(f"- **Output**: `{report['output_file']}`\n")
            f.write(f"- **Total characters**: {report['total_chars']:,}\n")
            f.write(f"- **Estimated pages**: {report['estimated_pages']}\n")
            if report.get('surya_improvements', 0) > 0:
                f.write(f"- **Surya-OCR improvements**: {report['surya_improvements']} pages\n")
            f.write("\n")
            
            if report['issues']:
                f.write("### Issues Found\n\n")
                for issue in report['issues']:
                    f.write(f"**{issue['type']}** - Severity: {issue['severity']}\n\n")
                    
                    if issue['type'] == 'SURYA_IMPROVEMENTS':
                        f.write("Surya-OCR successfully improved these pages:\n\n")
                        for page_info in issue['pages']:
                            f.write(f"- Page {page_info['page']}\n")
                        f.write("\n")
                    
                    elif issue['type'] == 'PAGE_QUALITY':
                        f.write(f"Problematic pages: {len(issue['pages'])}\n\n")
                        for page_issue in issue['pages']:
                            f.write(f"#### Page {page_issue['page']}\n\n")
                            f.write(f"- **Issue**: {page_issue['issue']}\n")
                            f.write(f"- **Characters**: {page_issue['char_count']}\n")
                            if page_issue.get('surya_tried'):
                                f.write(f"- **Surya-OCR tried**: Yes (still problematic)\n")
                            
                            if page_issue['image_path']:
                                f.write(f"\n**Original Image:**\n\n")
                                f.write(f"![Page {page_issue['page']}]({page_issue['image_path']})\n\n")
                            
                            f.write(f"**Marker converted text preview:**\n")
                            f.write(f"```\n{page_issue['text_preview']}\n```\n\n")
                            
                            if page_issue.get('surya_text_preview'):
                                f.write(f"**Surya-OCR text preview:**\n")
                                f.write(f"```\n{page_issue['surya_text_preview']}\n```\n\n")
                    else:
                        f.write(f"- {issue.get('description', 'No description')}\n\n")
            else:
                f.write("✓ No issues detected\n\n")
            
            f.write("---\n\n")

def main():
    """Main conversion process"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert PDFs to Markdown with quality checking')
    parser.add_argument('--test', type=str, help='Test with single PDF file (name without .pdf)')
    parser.add_argument('--all', action='store_true', help='Process all PDFs')
    parser.add_argument('--first', type=int, help='Process first N PDFs')
    parser.add_argument('--no-surya', action='store_true', help='Disable Surya-OCR fallback')
    args = parser.parse_args()
    
    # Paths
    pdf_dir = Path(r"d:\github\ENEL445\reference\contents")
    md_output_dir = Path(r"d:\github\ENEL445\reference\notes_new")
    figs_dir = Path(r"d:\github\ENEL445\figs")
    md_output_dir.mkdir(exist_ok=True)
    
    # Find PDFs to process
    if args.test:
        pdf_files = [pdf_dir / f"{args.test}.pdf"]
        if not pdf_files[0].exists():
            print(f"Error: {pdf_files[0]} not found")
            return
    elif args.all:
        pdf_files = sorted(pdf_dir.glob("*.pdf"))
    elif args.first:
        pdf_files = sorted(pdf_dir.glob("*.pdf"))[:args.first]
    else:
        print("Usage:")
        print("  python convert_with_quality_check.py --test 'filename'")
        print("  python convert_with_quality_check.py --first N")
        print("  python convert_with_quality_check.py --all")
        return
    
    print(f"Processing {len(pdf_files)} PDF(s)")
    use_surya = not args.no_surya
    if not use_surya:
        print("Surya-OCR fallback disabled")
    
    # Convert and analyze
    reports = []
    for pdf_path in pdf_files:
        try:
            report = convert_pdf_with_quality_check(pdf_path, md_output_dir, figs_dir, use_surya)
            reports.append(report)
        except Exception as e:
            print(f"✗ Error processing {pdf_path.name}: {e}")
            import traceback
            traceback.print_exc()
            reports.append({
                'pdf_file': pdf_path.name,
                'status': 'ERROR',
                'error': str(e),
                'estimated_pages': 0,
                'total_chars': 0,
                'surya_improvements': 0,
                'issues': []
            })
    
    # Generate quality report
    report_file = md_output_dir / "QUALITY_REPORT.md"
    generate_quality_report(reports, report_file)
    
    print(f"\n{'='*80}")
    print(f"✓ Conversion complete!")
    print(f"  Output: {md_output_dir}")
    print(f"  Quality report: {report_file}")
    print(f"{'='*80}")
    
    # Summary
    ok_count = sum(1 for r in reports if r.get('status') == 'OK')
    needs_review = sum(1 for r in reports if r.get('status') == 'NEEDS_REVIEW')
    errors = sum(1 for r in reports if r.get('status') == 'ERROR')
    
    print(f"\nSummary:")
    print(f"  ✓ Good: {ok_count}")
    print(f"  ⚠ Needs review: {needs_review}")
    print(f"  ✗ Errors: {errors}")

if __name__ == "__main__":
    main()
