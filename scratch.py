from pdf2image import convert_from_path
import pytesseract
import cv2
import numpy as np

# Set up Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH=r'C:\Program Files\poppler-24.08.0\Library\bin'

def pdf_to_text(pdf_path):
    # Convert PDF to images
    images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)

    all_text = ""
    for page_num, image in enumerate(images, start=1):
        image_cv = np.array(image)
        image_cv = cv2.cvtColor(image_cv, cv2.COLOR_RGB2BGR)

        # Optional: preprocess image (increase OCR accuracy)
        gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        # OCR
        text = pytesseract.image_to_string(gray)
        all_text += f"\n\n--- Page {page_num} ---\n\n{text}"
    return all_text
