"""
Convert all PDFs to markdown with LaTeX using Marker, then to .tex using Pandoc
"""
import sys
sys.path.insert(0, 'D:\\Python_Packages')

import os
import subprocess
from pathlib import Path
from marker.convert import convert_single_pdf
from marker.models import load_all_models

def convert_all_pdfs():
    # Paths
    pdf_dir = Path(r"d:\github\ENEL445\reference\contents")
    md_output_dir = Path(r"d:\github\ENEL445\reference\notes_new")
    tex_output_dir = Path(r"d:\github\ENEL445\reference\tex_files")
    md_output_dir.mkdir(exist_ok=True)
    tex_output_dir.mkdir(exist_ok=True)
    
    # Find all PDFs
    pdf_files = sorted(pdf_dir.glob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files to convert")
    
    # Load models once (they're large, so we reuse them)
    print("Loading Marker models (this may take a minute)...")
    model_lst = load_all_models()
    
    # Convert each PDF
    for i, pdf_path in enumerate(pdf_files, 1):
        print(f"\n[{i}/{len(pdf_files)}] Converting: {pdf_path.name}")
        
        try:
            # Step 1: Convert PDF to markdown using Marker
            full_text, images, out_meta = convert_single_pdf(
                str(pdf_path),
                model_lst,
                max_pages=None,
                langs=["English"],
                batch_multiplier=2
            )
            
            # Save markdown
            md_file = md_output_dir / f"{pdf_path.stem}.md"
            md_file.write_text(full_text, encoding='utf-8')
            print(f"  ✓ Saved markdown: {md_file.name}")
            
            # Save images if any
            if images:
                img_dir = md_output_dir / f"{pdf_path.stem}_images"
                img_dir.mkdir(exist_ok=True)
                for img_name, img_data in images.items():
                    img_path = img_dir / img_name
                    img_path.write_bytes(img_data)
                print(f"  ✓ Saved {len(images)} images")
            
            # Step 2: Convert markdown to .tex using Pandoc
            tex_file = tex_output_dir / f"{pdf_path.stem}.tex"
            pandoc_cmd = [
                r"C:\Program Files\Pandoc\pandoc.exe",
                str(md_file),
                "-f", "markdown",
                "-t", "latex",
                "--pdf-engine=xelatex",
                "-s",  # standalone document
                "-o", str(tex_file)
            ]
            
            result = subprocess.run(pandoc_cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"  ✓ Saved LaTeX: {tex_file.name}")
            else:
                print(f"  ⚠ Pandoc warning: {result.stderr[:100]}")
            
        except Exception as e:
            print(f"  ✗ Error: {e}")
            continue
    
    print(f"\n✓ Conversion complete!")
    print(f"  Markdown files: {md_output_dir}")
    print(f"  LaTeX files: {tex_output_dir}")

if __name__ == "__main__":
    convert_all_pdfs()
