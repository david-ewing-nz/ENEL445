"""
Minimal test of Marker PdfConverter
"""
from marker.converters.pdf import PdfConverter
from pathlib import Path

print("Creating PdfConverter...")
try:
    # Try with minimal kwargs
    converter = PdfConverter(
        artifact_dict={}
    )
    print("✓ PdfConverter created with artifact_dict={}")
    
    # Try converting
    test_pdf = Path(r"d:\github\ENEL445\reference\contents\2025-05-16 Introduction to GP.pdf")
    print(f"\nConverting: {test_pdf.name}...")
    
    result = converter(str(test_pdf))
    
    print(f"✓ Conversion completed!")
    print(f"Result type: {type(result)}")
    
    # Try to export the result
    if hasattr(result, '__dict__'):
        print("Result attributes:", list(result.__dict__.keys())[:10])
    
    # Check common output attributes
    for attr in ['markdown', 'text', 'content', 'output', 'data']:
        if hasattr(result, attr):
            val = getattr(result, attr)
            if isinstance(val, str):
                print(f"\n✓ Found {attr}: {len(val)} characters")
                print("Preview:")
                print(val[:300])
                break
    else:
        print("\nResult object:", result)
        
except TypeError as e:
    print(f"TypeError: {e}")
    print("\nTrying to inspect PdfConverter.__init__...")
    import inspect
    sig = inspect.signature(PdfConverter.__init__)
    print(f"Parameters: {sig}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
