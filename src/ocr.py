import easyocr
import cv2

reader = easyocr.Reader(['en'])

def extract_raw_text(image_path):
    img = cv2.imread(image_path)
    result = reader.readtext(img, detail=0)
    return " ".join(result)
