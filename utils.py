import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import cv2
from pypdf import PdfReader

reader = PdfReader('Blood report.pdf')

# print(len(reader.pages))

page = reader.pages[0]

# extracting text from page
text = page.extract_text()
print(text)

# image_path = r"C:\Users\USER\Pictures\Screenshots\Screenshot 2025-04-08 231057.png"

# img = cv2.imread(image_path)

# cv2.imshow("Image",img)
# cv2.waitKey(0)

# extracted_text = pytesseract.image_to_string(img)

# print(extracted_text)