"""
Convert PDFs to Markdown using Marker CLI with quality control
Uses subprocess to call marker_single.exe
"""
import subprocess
import os
from pathlib import Path
from typing import Dict, List
import re

def analyze_markdown_quality(md_text: str, pdf_name: str, fig_folder: Path) -> Dict:
    """Analyze the quality of converted markdown"""
    issues = []
    
    # Basic metrics
    char_count = len(md_text)
    line_count = len(md_text.split('\n'))
    alpha_count = sum(c.isalpha() for c in md_text)
    
    print(f"  Analysis: {char_count:,} chars, {line_count} lines")
    
    # Check for very short content
    if char_count < 500:
        issues.append({
            'type': 'SHORT_CONTENT',
            'description': f'Only {char_count} characters - may be incomplete',
            'severity': 'HIGH'
        })
    
    # Check for low alpha ratio (garbled text)
    if char_count > 100 and alpha_count / char_count < 0.3:
        issues.append({
            'type': 'GARBLED_TEXT',
            'description': f'Low alpha ratio ({alpha_count/char_count:.2%}) - possibly garbled',
            'severity': 'MEDIUM'
        })
    
    # Split into sections to find problematic areas
    sections = md_text.split('\n##')
    short_sections = []
    for i, section in enumerate(sections):
        if len(section.strip()) < 50 and i > 0:  # Skip header
            short_sections.append(i)
    
    if short_sections:
        issues.append({
            'type': 'SHORT_SECTIONS',
            'description': f'{len(short_sections)} very short sections found',
            'severity': 'LOW',
            'sections': short_sections
        })
    
    status = 'OK' if not any(i['severity'] in ['HIGH', 'MEDIUM'] for i in issues) else 'NEEDS_REVIEW'
    
    return {
        'status': status,
        'char_count': char_count,
        'line_count': line_count,
        'alpha_ratio': alpha_count / char_count if char_count > 0 else 0,
        'issues': issues
    }

def convert_pdf_with_marker_cli(pdf_path: Path, output_dir: Path, figs_dir: Path, marker_exe: Path) -> Dict:
    """Convert a single PDF using marker CLI"""
    print(f"\n{'='*80}")
    print(f"Converting: {pdf_path.name}")
    print(f"{'='*80}")
    
    # Prepare output path
    md_file = output_dir / f"{pdf_path.stem}.md"
    
    # Run marker_single
    cmd = [
        str(marker_exe),
        str(pdf_path),
        str(md_file),
        "--output_format", "markdown"
    ]
    
    print(f"Running marker...")
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout per file
        )
        
        if result.returncode != 0:
            print(f"  ✗ Marker failed with code {result.returncode}")
            if result.stderr:
                print(f"  Error: {result.stderr[:200]}")
            return {
                'pdf_file': pdf_path.name,
                'status': 'ERROR',
                'error': result.stderr[:500] if result.stderr else f'Exit code {result.returncode}'
            }
        
        print(f"  ✓ Conversion completed")
        
        # Read the output
        if md_file.exists():
            md_text = md_file.read_text(encoding='utf-8')
        else:
            print(f"  ✗ Output file not found: {md_file}")
            return {
                'pdf_file': pdf_path.name,
                'status': 'ERROR',
                'error': 'Output file not created'
            }
        
        # Analyze quality
        fig_folder = figs_dir / pdf_path.stem
        analysis = analyze_markdown_quality(md_text, pdf_path.name, fig_folder)
        
        # Build report
        report = {
            'pdf_file': pdf_path.name,
            'output_file': md_file.name,
            **analysis
        }
        
        if analysis['status'] == 'OK':
            print(f"  ✓ Quality check passed")
        else:
            print(f"  ⚠ Quality issues found")
        
        return report
        
    except subprocess.TimeoutExpired:
        print(f"  ✗ Timeout after 5 minutes")
        return {
            'pdf_file': pdf_path.name,
            'status': 'ERROR',
            'error': 'Conversion timeout (5 min)'
        }
    except Exception as e:
        print(f"  ✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return {
            'pdf_file': pdf_path.name,
            'status': 'ERROR',
            'error': str(e)
        }

def generate_quality_report(reports: List[Dict], output_file: Path):
    """Generate a markdown report"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# PDF Conversion Quality Report\n\n")
        f.write("---\n\n")
        
        for report in reports:
            f.write(f"## {report['pdf_file']}\n\n")
            
            if report['status'] == 'ERROR':
                f.write(f"- **Status**: ❌ ERROR\n")
                f.write(f"- **Error**: {report.get('error', 'Unknown error')}\n\n")
                f.write("---\n\n")
                continue
            
            f.write(f"- **Status**: {'✅ OK' if report['status'] == 'OK' else '⚠️ NEEDS_REVIEW'}\n")
            f.write(f"- **Output**: `{report['output_file']}`\n")
            f.write(f"- **Characters**: {report.get('char_count', 0):,}\n")
            f.write(f"- **Lines**: {report.get('line_count', 0):,}\n")
            f.write(f"- **Alpha ratio**: {report.get('alpha_ratio', 0):.1%}\n\n")
            
            if report.get('issues'):
                f.write("### Issues\n\n")
                for issue in report['issues']:
                    severity_icon = {'HIGH': '🔴', 'MEDIUM': '🟡', 'LOW': '🟢'}.get(issue['severity'], '')
                    f.write(f"- {severity_icon} **{issue['type']}**: {issue['description']}\n")
                f.write("\n")
            
            f.write("---\n\n")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert PDFs using Marker CLI')
    parser.add_argument('--test', type=str, help='Test with single PDF (filename without .pdf)')
    parser.add_argument('--first', type=int, help='Process first N PDFs')
    parser.add_argument('--all', action='store_true', help='Process all PDFs')
    args = parser.parse_args()
    
    # Paths
    pdf_dir = Path(r"d:\github\ENEL445\reference\contents")
    output_dir = Path(r"d:\github\ENEL445\reference\notes_new")
    figs_dir = Path(r"d:\github\ENEL445\figs")
    marker_exe = Path(r"d:\github\ENEL445\.venv\Scripts\marker_single.exe")
    
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
        print("  python convert_using_marker_cli.py --test 'filename'")
        print("  python convert_using_marker_cli.py --first N")
        print("  python convert_using_marker_cli.py --all")
        return
    
    print(f"\n{'='*80}")
    print(f"Processing {len(pdf_files)} PDF(s)")
    print(f"{'='*80}")
    
    # Convert all
    reports = []
    for i, pdf_path in enumerate(pdf_files, 1):
        print(f"\n[{i}/{len(pdf_files)}]")
        report = convert_pdf_with_marker_cli(pdf_path, output_dir, figs_dir, marker_exe)
        reports.append(report)
    
    # Generate report
    report_file = output_dir / "QUALITY_REPORT.md"
    generate_quality_report(reports, report_file)
    
    # Summary
    print(f"\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    ok_count = sum(1 for r in reports if r['status'] == 'OK')
    needs_review = sum(1 for r in reports if r['status'] == 'NEEDS_REVIEW')
    errors = sum(1 for r in reports if r['status'] == 'ERROR')
    
    print(f"✅ OK: {ok_count}")
    print(f"⚠️  Needs review: {needs_review}")
    print(f"❌ Errors: {errors}")
    print(f"\nOutput: {output_dir}")
    print(f"Report: {report_file}")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    main()
