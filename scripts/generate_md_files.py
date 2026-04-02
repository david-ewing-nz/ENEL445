"""
Generate markdown files with embedded images for all PDFs
Creates one .md file per PDF with all pages as embedded images
"""

import os
from pathlib import Path
from urllib.parse import quote

# Paths
script_dir = Path(__file__).parent
project_root = script_dir.parent
figs_dir = project_root / "figs"
contents_dir = project_root / "reference" / "contents"

def generate_md_for_document(doc_name):
    """Generate markdown file with all pages for a document"""
    
    # Get all PNG files for this document
    doc_fig_dir = figs_dir / doc_name
    if not doc_fig_dir.exists():
        print(f"⚠️  No figs folder for: {doc_name}")
        return False
    
    png_files = sorted(doc_fig_dir.glob("page_*.png"))
    if not png_files:
        print(f"⚠️  No images found for: {doc_name}")
        return False
    
    # Generate markdown content
    md_content = [f"# {doc_name}\n"]
    md_content.append(f"**Course:** ENEL445 - Applied Engineering Optimisation\n")
    md_content.append(f"**Pages:** {len(png_files)}\n")
    
    # URL encode the document name for the PDF link
    pdf_name_encoded = quote(f"{doc_name}.pdf")
    md_content.append(f"**Source:** [{doc_name}.pdf]({pdf_name_encoded})\n\n")
    md_content.append("---\n\n")
    
    # Add each page
    for i, png_file in enumerate(png_files, 1):
        # URL encode the path for the image
        rel_path = f"../../figs/{doc_name}/{png_file.name}"
        rel_path_encoded = quote(rel_path, safe='/')
        
        md_content.append(f"## Page {i}\n")
        md_content.append(f"![Page {i}]({rel_path_encoded})\n\n")
        md_content.append(f"### Notes\n\n\n---\n\n")
    
    # Add summary section
    md_content.append("## Summary\n\n")
    md_content.append("### Key Topics\n\n\n")
    md_content.append("### Important Equations\n\n\n")
    md_content.append("### Key Takeaways\n\n\n")
    
    # Write to file
    output_file = contents_dir / f"{doc_name}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(''.join(md_content))
    
    print(f"✓ Created: {doc_name}.md ({len(png_files)} pages)")
    return True

def main():
    """Generate .md files for all documents in figs/"""
    
    print("\nGenerating Markdown Files with Embedded Images")
    print("=" * 60)
    print(f"Source: {figs_dir}")
    print(f"Output: {contents_dir}\n")
    
    # Get all subdirectories in figs (each is a document)
    doc_folders = [d for d in figs_dir.iterdir() if d.is_dir()]
    doc_folders.sort()
    
    success_count = 0
    for doc_folder in doc_folders:
        doc_name = doc_folder.name
        if generate_md_for_document(doc_name):
            success_count += 1
    
    print("\n" + "=" * 60)
    print(f"Completed: {success_count}/{len(doc_folders)} markdown files created")
    print(f"Location: {contents_dir}")

if __name__ == "__main__":
    main()
