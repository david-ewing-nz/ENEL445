"""
Simple test to figure out the new Marker API
"""
import sys

# Try to import marker and see what's available
try:
    import marker
    print("Marker package found")
    print("Marker location:", marker.__file__)
    print("Marker attributes:", [x for x in dir(marker) if not x.startswith('_')])
    
    # Try converters
    from marker.converters import pdf
    print("\nPDF converter found")
    print("PDF attributes:", [x for x in dir(pdf) if not x.startswith('_')])
    
    # Try to find the main converter class
    if hasattr(pdf, 'PdfConverter'):
        print("\nPdfConverter class found!")
        converter = pdf.PdfConverter()
        print("PdfConverter methods:", [x for x in dir(converter) if not x.startswith('_')])
    
    # Check for convert function
    if hasattr(pdf, 'convert'):
        print("\nconvert function found!")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
