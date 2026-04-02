"""
Extract text from PDF using PyMuPDF
Simple text extraction without OCR
"""

import sys
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path, output_path):
    """Extract text from PDF and save to markdown file."""
    doc = fitz.open(pdf_path)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# Extracted from: {pdf_path}\n\n")
        f.write(f"Total pages: {len(doc)}\n\n")
        f.write("---\n\n")
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            
            f.write(f"## Page {page_num + 1}\n\n")
            f.write(text)
            f.write("\n\n---\n\n")
    
    doc.close()
    print(f"Extracted text to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_pdf_text.py <input_pdf> <output_md>")
        sys.exit(1)
    
    extract_text_from_pdf(sys.argv[1], sys.argv[2])
