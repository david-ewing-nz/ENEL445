"""
Test Marker PdfConverter with proper initialization
"""
from marker.converters.pdf import PdfConverter
from marker.output import OutputFormat

# Try to create a converter properly
print("Creating PdfConverter...")
try:
    # PdfConverter needs an artifact_dict, check if we can pass empty dict
    converter = PdfConverter(
        artifact_dict={},
        output_format=OutputFormat.MARKDOWN
    )
    print("✓ PdfConverter created!")
    print("Methods:", [m for m in dir(converter) if not m.startswith('_') and callable(getattr(converter, m))])
    
    # Try converting a PDF
    from pathlib import Path
    test_pdf = Path(r"d:\github\ENEL445\reference\contents\2025-05-16 Introduction to GP.pdf")
    
    if test_pdf.exists():
        print(f"\nTrying to convert: {test_pdf.name}")
        result = converter(str(test_pdf))
        print(f"✓ Conversion successful!")
        print(f"Result type: {type(result)}")
        print(f"Result attributes: {[x for x in dir(result) if not x.startswith('_')][:10]}")
        
        # Try to get the markdown
        if hasattr(result, 'markdown'):
            md_text = result.markdown
            print(f"\n✓ Got markdown: {len(md_text)} chars")
            print("First 500 chars:")
            print(md_text[:500])
        elif hasattr(result, 'text'):
            print(f"\n✓ Got text: {len(result.text)} chars")
        else:
            print(f"\nResult: {result}")
    else:
        print(f"PDF not found: {test_pdf}")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
