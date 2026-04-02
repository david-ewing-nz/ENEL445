"""
Convert PDFs to Markdown using PyMuPDF + Surya-OCR for problematic pages
Reliable and fast approach
"""
import fitz  # PyMuPDF
import urllib.parse
from pathlib import Path
from typing import Dict, List, Tuple
from PIL import Image

# EasyOCR imports
try:
    import easyocr
    EASYOCR_AVAILABLE = True
except ImportError as e:
    EASYOCR_AVAILABLE = False
    print(f"Warning: EasyOCR not available: {e}")

def load_easyocr_reader():
    """Load EasyOCR reader once"""
    if not EASYOCR_AVAILABLE:
        return None
    print("Loading EasyOCR models (this may take a minute on first run)...")
    try:
        # Load English language model
        reader = easyocr.Reader(['en'], gpu=False)
        print("  ✓ EasyOCR models loaded")
        return reader
    except Exception as e:
        print(f"Warning: Could not load EasyOCR: {e}")
        return None

def ocr_image_with_easyocr(image_path: Path, reader) -> str:
    """Run EasyOCR on an image"""
    if not reader:
        return "[EasyOCR unavailable]"
    
    try:
        # Read text from image
        result = reader.readtext(str(image_path), detail=0)
        # Join all detected text with newlines
        return '\n'.join(result)
    except Exception as e:
        return f"[EasyOCR error: {e}]"

def analyze_page_text(text: str, page_num: int) -> Tuple[bool, str]:
    """Check if page text is good quality"""
    char_count = len(text.strip())
    
    if char_count < 30:
        return False, f"Very short ({char_count} chars)"
    
    alpha_count = sum(c.isalpha() for c in text)
    if char_count > 50 and alpha_count / char_count < 0.2:
        return False, "High special char ratio"
    
    return True, "OK"

def convert_pdf(pdf_path: Path, figs_dir: Path, use_ocr: bool = True) -> Dict:
    """Convert a single PDF to markdown"""
    print(f"\n{'='*80}")
    print(f"Converting: {pdf_path.name}")
    print(f"{'='*80}")
    
    # Load EasyOCR reader if needed
    ocr_reader = None
    if use_ocr and EASYOCR_AVAILABLE:
        ocr_reader = load_easyocr_reader()
    
    # Extract text with PyMuPDF
    print("Extracting text...")
    try:
        doc = fitz.open(str(pdf_path))
        pages_text = []
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            pages_text.append(text)
        doc.close()
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return {
            'pdf_file': pdf_path.name,
            'status': 'ERROR',
            'error': str(e)
        }
    
    # Process each page
    markdown_parts = []
    markdown_parts.append(f"# {pdf_path.stem}\n\n")
    markdown_parts.append(f"*Converted from PDF: {pdf_path.name}*\n\n")
    markdown_parts.append("---\n\n")
    
    fig_folder = figs_dir / pdf_path.stem
    problematic_pages = []
    ocr_improvements = 0
    
    for page_num, page_text in enumerate(pages_text, 1):
        is_good, issue = analyze_page_text(page_text, page_num)
        
        if not is_good and ocr_reader and fig_folder.exists():
            # Try EasyOCR
            img_file = fig_folder / f"page_{page_num:03d}.png"
            if img_file.exists():
                print(f"  Page {page_num}: {issue}, trying EasyOCR...")
                ocr_text = ocr_image_with_easyocr(img_file, ocr_reader)
                ocr_good, _ = analyze_page_text(ocr_text, page_num)
                
                if ocr_good:
                    print(f"    ✓ EasyOCR improved page {page_num}")
                    page_text = ocr_text
                    is_good = True
                    ocr_improvements += 1
        
        if not is_good:
            problematic_pages.append({
                'page': page_num,
                'issue': issue,
                'char_count': len(page_text),
                'preview': page_text[:200]
            })
        
        # Add to markdown
        markdown_parts.append(f"## Page {page_num}\n\n")
        if page_text.strip():
            markdown_parts.append(page_text.strip())
            markdown_parts.append("\n\n")
        else:
            markdown_parts.append("*[Page appears blank or contains only images]*\n\n")
        
        # Add image reference (relative to the contents folder)
        if fig_folder.exists():
            img_file = fig_folder / f"page_{page_num:03d}.png"
            if img_file.exists():
                # Path relative to contents folder: ../figs/...
                # URL-encode spaces for markdown compatibility
                folder_name_encoded = urllib.parse.quote(pdf_path.stem)
                rel_path_str = f"../figs/{folder_name_encoded}/page_{page_num:03d}.png"
                markdown_parts.append(f"![Page {page_num}]({rel_path_str})\n\n")
        
        markdown_parts.append("---\n\n")
    
    markdown_text = ''.join(markdown_parts)
    
    # Summary
    print(f"  Total pages: {len(pages_text)}")
    print(f"  Total characters: {len(markdown_text):,}")
    if ocr_improvements > 0:
        print(f"  ✓ EasyOCR improved {ocr_improvements} pages")
    if problematic_pages:
        print(f"  ⚠ {len(problematic_pages)} problematic pages")
    
    return {
        'pdf_file': pdf_path.name,
        'status': 'NEEDS_REVIEW' if problematic_pages else 'OK',
        'markdown': markdown_text,
        'total_pages': len(pages_text),
        'char_count': len(markdown_text),
        'ocr_improvements': ocr_improvements,
        'problematic_pages': problematic_pages
    }

def generate_report(reports: List[Dict], output_file: Path):
    """Generate quality report"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# PDF Conversion Quality Report\n\n")
        f.write("---\n\n")
        
        for report in reports:
            f.write(f"## {report['pdf_file']}\n\n")
            
            if report['status'] == 'ERROR':
                f.write(f"- **Status**: ❌ ERROR\n")
                f.write(f"- **Error**: {report.get('error')}\n\n")
                f.write("---\n\n")
                continue
            
            f.write(f"- **Status**: {'✅ OK' if report['status'] == 'OK' else '⚠️ NEEDS_REVIEW'}\n")
            f.write(f"- **Pages**: {report.get('total_pages', 0)}\n")
            f.write(f"- **Characters**: {report.get('char_count', 0):,}\n")
            
            if report.get('ocr_improvements', 0) > 0:
                f.write(f"- **OCR improvements**: {report['ocr_improvements']}\n")
            
            if report.get('problematic_pages'):
                f.write(f"\n### Problematic Pages ({len(report['problematic_pages'])})\n\n")
                for page in report['problematic_pages']:
                    f.write(f"#### Page {page['page']}\n\n")
                    f.write(f"- **Issue**: {page['issue']}\n")
                    f.write(f"- **Characters**: {page['char_count']}\n")
                    f.write(f"\n**Text preview:**\n```\n{page['preview']}\n```\n\n")
            
            f.write("---\n\n")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert PDFs to Markdown')
    parser.add_argument('--test', type=str, help='Test single PDF')
    parser.add_argument('--first', type=int, help='Process first N PDFs')
    parser.add_argument('--all', action='store_true', help='Process all PDFs')
    parser.add_argument('--no-ocr', action='store_true', help='Disable OCR')
    args = parser.parse_args()
    
    pdf_dir = Path(r"d:\github\ENEL445\contents")
    output_dir = Path(r"d:\github\ENEL445\contents")
    figs_dir = Path(r"d:\github\ENEL445\figs")
    output_dir.mkdir(exist_ok=True)
    
    # Find PDFs
    if args.test:
        pdf_files = [pdf_dir / f"{args.test}.pdf"]
        if not pdf_files[0].exists():
            print(f"Error: {pdf_files[0]} not found")
            return
    elif args.first:
        pdf_files = sorted(pdf_dir.glob("*.pdf"))[:args.first]
    elif args.all:
        pdf_files = sorted(pdf_dir.glob("*.pdf"))
    else:
        print("Usage:")
        print("  python convert_pdfs_simple.py --first N")
        print("  python convert_pdfs_simple.py --test 'filename'")
        print("  python convert_pdfs_simple.py --all")
        return
    
    print(f"Processing {len(pdf_files)} PDF(s)")
    use_ocr = not args.no_ocr
    
    # Convert
    reports = []
    for i, pdf_path in enumerate(pdf_files, 1):
        print(f"\n[{i}/{len(pdf_files)}]")
        
        report = convert_pdf(pdf_path, figs_dir, use_ocr)
        reports.append(report)
        
        # Save markdown
        if 'markdown' in report:
            md_file = output_dir / f"{pdf_path.stem}.md"
            md_file.write_text(report['markdown'], encoding='utf-8')
            print(f"  ✓ Saved: {md_file.name}")
    
    # Generate report
    report_file = output_dir / "QUALITY_REPORT.md"
    generate_report(reports, report_file)
    
    # Summary
    print(f"\n{'='*80}")
    ok = sum(1 for r in reports if r['status'] == 'OK')
    review = sum(1 for r in reports if r['status'] == 'NEEDS_REVIEW')
    errors = sum(1 for r in reports if r['status'] == 'ERROR')
    
    print(f"✅ OK: {ok}")
    print(f"⚠️  Needs review: {review}")
    print(f"❌ Errors: {errors}")
    print(f"\nOutput: {output_dir}")
    print(f"Report: {report_file}")
    print(f"{'='*80}")

if __name__ == "__main__":
    main()
