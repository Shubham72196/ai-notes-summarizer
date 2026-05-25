from PIL import Image
import pytesseract

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"D:\tessaract-ocr\tesseract.exe"

def extract_text(image_path):

    image = Image.open(image_path)

    text = pytesseract.image_to_string(image)

    # CLEANING
    text = text.replace("\n", " ")

    text = " ".join(text.split())

    return text