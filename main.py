from ocr_utils import extract_text_from_image
from ocr_utils import clean_ocr_text

if __name__ == "__main__":
    image_path = r"Files\Screenshot 2025-01-03 125132.png"  
    extracted_text = extract_text_from_image(image_path)

    print("\n--- Extracted Text ---\n")
    print(extracted_text)

    clean_text = clean_ocr_text(extracted_text)
    print("""
the cleaned text ---
          
          
          """)
    print(clean_text)
