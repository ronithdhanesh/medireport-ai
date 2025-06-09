from ocr_utils import extract_text_from_image

if __name__ == "__main__":
    image_path = "Files\Screenshot 2025-01-03 125132.png"  
    extracted_text = extract_text_from_image(image_path)

    print("\n--- Extracted Text ---\n")
    print(extracted_text)
