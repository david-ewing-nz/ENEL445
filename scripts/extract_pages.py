"""Extract first N pages from a PDF"""
import sys
import fitz  # PyMuPDF

if len(sys.argv) < 3:
    print("Usage: python extract_pages.py input.pdf output.pdf [num_pages]")
    sys.exit(1)

input_pdf = sys.argv[1]
output_pdf = sys.argv[2]
num_pages = int(sys.argv[3]) if len(sys.argv) > 3 else 20

print(f"Extracting first {num_pages} pages from {input_pdf}...")

doc = fitz.open(input_pdf)
print(f"Total pages in PDF: {len(doc)}")

new_doc = fitz.open()
for i in range(min(num_pages, len(doc))):
    new_doc.insert_pdf(doc, from_page=i, to_page=i)
    print(f"  Extracted page {i+1}/{num_pages}")

new_doc.save(output_pdf)
new_doc.close()
doc.close()

print(f"✓ Saved first {num_pages} pages to {output_pdf}")
