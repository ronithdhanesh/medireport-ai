import pytesseract
from PIL import Image
import cv2
import os
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

def clean_ocr_text(raw_text):
    # Remove excessive whitespace and line breaks
    text = re.sub(r'\n+', '\n', raw_text)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # remove non-ASCII chars
    text = re.sub(r'\s{2,}', ' ', text)         # extra spaces

    # Optional: remove lines that are just headers or page numbers
    lines = text.split('\n')
    lines = [line.strip() for line in lines if len(line.strip()) > 3]  # filter short lines

    return '\n'.join(lines)

