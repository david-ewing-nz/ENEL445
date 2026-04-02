"""
PDF to Text Converter
Extracts all text from PDF files in the contents folder
Saves each PDF as a corresponding .txt file in a context folder for AI reference
Skips files that already have .txt versions unless forced via command line
Author: David Ewing
"""

import os
import sys
import argparse

try:
    import fitz  # PyMuPDF
except ImportError:
    print("PyMuPDF not installed. Installing now...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyMuPDF"])
    import fitz

def extract_text_from_pdf(pdf_path, output_path):
    """
    Extract all text from a PDF file and save to text file

    Args:
        pdf_path: path to the PDF file
        output_path: path to save the extracted text
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Open the PDF
        doc = fitz.open(pdf_path)

        # Extract text from all pages
        full_text = []
        full_text.append(f"{'='*80}\n")
        full_text.append(f"SOURCE: {os.path.basename(pdf_path)}\n")
        full_text.append(f"PAGES: {len(doc)}\n")
        full_text.append(f"{'='*80}\n\n")
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            full_text.append(f"\n{'─'*80}\n")
            full_text.append(f"PAGE {page_num + 1}\n")
            full_text.append(f"{'─'*80}\n\n")
            full_text.append(text)

        # Close the document
        doc.close()

        # Write to output file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(''.join(full_text))

        print(f"✓ Extracted: {os.path.basename(pdf_path)}")
        return True

    except Exception as e:
        print(f"✗ Error processing {os.path.basename(pdf_path)}: {str(e)}")
        return False

def main():
    """
    Process all PDF files in the contents folder
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Extract text from PDF files')
    parser.add_argument('--force', action='store_true', 
                       help='Force re-extraction even if .txt file exists')
    parser.add_argument('--file', type=str, 
                       help='Process only a specific PDF file (by name)')
    args = parser.parse_args()

    # Get the script directory and construct paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    contents_dir = os.path.join(project_root, 'contents')
    context_dir = os.path.join(project_root, 'context')

    # Create context directory if it doesn't exist
    os.makedirs(context_dir, exist_ok=True)

    print(f"\nPDF to Text Converter")
    print(f"{'='*80}")
    print(f"Source folder: {contents_dir}")
    print(f"Output folder: {context_dir}")
    print(f"Force mode: {'ON' if args.force else 'OFF'}\n")

    # Find all PDF files
    if args.file:
        # Process specific file
        if not args.file.lower().endswith('.pdf'):
            args.file += '.pdf'
        pdf_path = os.path.join(contents_dir, args.file)
        if os.path.exists(pdf_path):
            pdf_files = [args.file]
        else:
            print(f"Error: File not found: {args.file}")
            return
    else:
        # Process all PDFs
        pdf_files = [f for f in os.listdir(contents_dir) if f.lower().endswith('.pdf')]

    if not pdf_files:
        print("No PDF files found.")
        return

    print(f"Found {len(pdf_files)} PDF file(s)\n")

    # Process each PDF
    processed = 0
    skipped = 0
    failed = 0

    for pdf_file in sorted(pdf_files):
        pdf_path = os.path.join(contents_dir, pdf_file)
        txt_file = pdf_file[:-4] + '.txt'  # Replace .pdf with .txt
        txt_path = os.path.join(context_dir, txt_file)

        # Check if already extracted (unless forced)
        if not args.force and os.path.exists(txt_path):
            print(f"⊙ Skipped: {pdf_file} (already extracted)")
            skipped += 1
            continue

        # Extract text
        if extract_text_from_pdf(pdf_path, txt_path):
            processed += 1
        else:
            failed += 1

    print(f"\n{'='*80}")
    print(f"Conversion completed:")
    print(f"  - Processed: {processed}")
    print(f"  - Skipped: {skipped}")
    print(f"  - Failed: {failed}")
    print(f"  - Total: {len(pdf_files)}")
    print(f"\nExtracted text saved to: {context_dir}")

if __name__ == "__main__":
    main()
