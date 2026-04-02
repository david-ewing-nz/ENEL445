"""
PowerPoint to Text Converter
Extracts all text from PPTX files in the contents folder
Saves each PPTX as a corresponding .txt file in a context folder for AI reference
Skips files that already have .txt versions unless forced via command line
Author: David Ewing
"""

import os
import sys
import argparse
import zipfile
import xml.etree.ElementTree as ET

def extract_text_from_pptx(pptx_path, output_path):
    """
    Extract all text from a PowerPoint file and save to text file

    Args:
        pptx_path: path to the PPTX file
        output_path: path to save the extracted text
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # PPTX files are ZIP archives
        with zipfile.ZipFile(pptx_path, 'r') as zip_ref:
            # Get list of slide XML files
            slide_files = [f for f in zip_ref.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
            slide_files.sort()
            
            full_text = []
            full_text.append(f"{'='*80}\n")
            full_text.append(f"SOURCE: {os.path.basename(pptx_path)}\n")
            full_text.append(f"SLIDES: {len(slide_files)}\n")
            full_text.append(f"{'='*80}\n\n")
            
            # Extract text from each slide
            for idx, slide_file in enumerate(slide_files, 1):
                slide_xml = zip_ref.read(slide_file)
                
                # Parse XML
                root = ET.fromstring(slide_xml)
                
                # Find all text elements (a:t tags in the namespace)
                # PowerPoint uses various namespaces
                texts = []
                for elem in root.iter():
                    # Check if it's a text element
                    if elem.tag.endswith('}t'):  # Matches any namespace with tag 't'
                        if elem.text:
                            texts.append(elem.text)
                
                full_text.append(f"\n{'─'*80}\n")
                full_text.append(f"SLIDE {idx}\n")
                full_text.append(f"{'─'*80}\n\n")
                
                if texts:
                    full_text.append('\n'.join(texts))
                else:
                    full_text.append("[No text content]")
                
                full_text.append('\n')
        
        # Write to output file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(''.join(full_text))
        
        print(f"✓ Extracted: {os.path.basename(pptx_path)}")
        return True
    
    except Exception as e:
        print(f"✗ Error processing {os.path.basename(pptx_path)}: {str(e)}")
        return False

def main():
    """
    Process all PPTX files in the contents folder
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Extract text from PowerPoint files')
    parser.add_argument('--force', action='store_true', 
                       help='Force re-extraction even if .txt file exists')
    parser.add_argument('--file', type=str, 
                       help='Process only a specific PPTX file (by name)')
    args = parser.parse_args()

    # Get the script directory and construct paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    contents_dir = os.path.join(project_root, 'contents')
    context_dir = os.path.join(project_root, 'context')

    # Create context directory if it doesn't exist
    os.makedirs(context_dir, exist_ok=True)

    print(f"\nPowerPoint to Text Converter")
    print(f"{'='*80}")
    print(f"Source folder: {contents_dir}")
    print(f"Output folder: {context_dir}")
    print(f"Force mode: {'ON' if args.force else 'OFF'}\n")

    # Find all PPTX files
    if args.file:
        # Process specific file
        if not args.file.lower().endswith('.pptx'):
            args.file += '.pptx'
        pptx_path = os.path.join(contents_dir, args.file)
        if os.path.exists(pptx_path):
            pptx_files = [args.file]
        else:
            print(f"Error: File not found: {args.file}")
            return
    else:
        # Process all PPTX files
        pptx_files = [f for f in os.listdir(contents_dir) if f.lower().endswith('.pptx')]

    if not pptx_files:
        print("No PPTX files found.")
        return

    print(f"Found {len(pptx_files)} PPTX file(s)\n")

    # Process each PPTX
    processed = 0
    skipped = 0
    failed = 0

    for pptx_file in sorted(pptx_files):
        pptx_path = os.path.join(contents_dir, pptx_file)
        txt_file = pptx_file[:-5] + '.txt'  # Replace .pptx with .txt
        txt_path = os.path.join(context_dir, txt_file)

        # Check if already extracted (unless forced)
        if not args.force and os.path.exists(txt_path):
            print(f"⊙ Skipped: {pptx_file} (already extracted)")
            skipped += 1
            continue

        # Extract text
        if extract_text_from_pptx(pptx_path, txt_path):
            processed += 1
        else:
            failed += 1

    print(f"\n{'='*80}")
    print(f"Conversion completed:")
    print(f"  - Processed: {processed}")
    print(f"  - Skipped: {skipped}")
    print(f"  - Failed: {failed}")
    print(f"  - Total: {len(pptx_files)}")
    print(f"\nExtracted text saved to: {context_dir}")

if __name__ == "__main__":
    main()
