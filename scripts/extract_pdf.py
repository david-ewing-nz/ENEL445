import fitz  # PyMuPDF
import os
import glob
import sys
import argparse

def convert_pdf_pages_to_images(pdf_path, output_dir):
    """Convert each page of a PDF to a PNG image."""
    try:
        # Open the PDF
        doc = fitz.open(pdf_path)
        total_pages = len(doc)
        
        print(f"\nProcessing: {os.path.basename(pdf_path)} ({total_pages} pages)")
        
        # Convert each page to an image
        for page_num in range(total_pages):
            page = doc.load_page(page_num)
            
            # Render page to an image (PNG)
            # mat = fitz.Matrix(2, 2) increases resolution (2x zoom)
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            
            # Save the image
            image_name = f"page_{page_num+1:03d}.png"
            image_path = os.path.join(output_dir, image_name)
            pix.save(image_path)
            
            print(f"  - Saved page {page_num+1}/{total_pages} as {image_name}")
        
        doc.close()
        print(f"  ✓ Completed: {os.path.basename(pdf_path)}")
        return True
        
    except Exception as e:
        print(f"  ✗ Error processing {os.path.basename(pdf_path)}: {e}")
        return False

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Parse optional argument for a single PDF file
parser = argparse.ArgumentParser(description="Convert PDF pages to PNG images.")
parser.add_argument("pdf", nargs="?", help="Path to a single PDF file to convert (optional)")
args = parser.parse_args()

if args.pdf:
    # Single file mode
    pdf_path = os.path.abspath(args.pdf)
    if not os.path.isfile(pdf_path):
        print(f"Error: file not found: {pdf_path}")
        sys.exit(1)
    pdf_name_no_ext = os.path.splitext(os.path.basename(pdf_path))[0]
    output_dir = os.path.join(os.path.dirname(pdf_path), pdf_name_no_ext)
    os.makedirs(output_dir, exist_ok=True)
    convert_pdf_pages_to_images(pdf_path, output_dir)
    print(f"Images saved to: {os.path.abspath(output_dir)}")

else:
    # Batch mode — process all PDFs in contents/
    contents_dir = os.path.join(script_dir, '..', 'contents')
    fig_base_dir = os.path.join(script_dir, '..', 'figs')
    os.makedirs(fig_base_dir, exist_ok=True)

    pdf_files = glob.glob(os.path.join(contents_dir, '*.pdf'))

    if not pdf_files:
        print(f"No PDF files found in {contents_dir}")
    else:
        print(f"Found {len(pdf_files)} PDF files to process\n")
        print("=" * 60)

        success_count = 0
        for pdf_path in sorted(pdf_files):
            pdf_basename = os.path.basename(pdf_path)
            pdf_name_no_ext = os.path.splitext(pdf_basename)[0]
            output_dir = os.path.join(fig_base_dir, pdf_name_no_ext)
            os.makedirs(output_dir, exist_ok=True)
            if convert_pdf_pages_to_images(pdf_path, output_dir):
                success_count += 1

        print("=" * 60)
        print(f"\nConversion completed: {success_count}/{len(pdf_files)} PDFs processed successfully")
        print(f"Images saved to: {os.path.abspath(fig_base_dir)}")