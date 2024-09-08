import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np
import json

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image):
    image_np = np.array(image)
    gray_image = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    extracted_text = pytesseract.image_to_string(gray_image)
    extracted_text = extracted_text.upper()
    
    return extracted_text

def parse_text_to_dict(text):
    info_dict = {}
    lines = text.split("\n")
    for line in lines:
        if ':' in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            info_dict[key] = value 
    return info_dict


def save_to_json(data, filename='user_data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    st.success(f"Data saved to {filename}")


def MainMethod():
    st.title("Medical Report Text Extraction")
    st.write("Upload a medical report image to extract the text.")
    uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        extracted_text = extract_text_from_image(image)
        extracted_info = parse_text_to_dict(extracted_text)
        st.write("Extracted Text:")
        st.text(extracted_text)
        st.write("Extracted Information:")
        st.json(extracted_info)
        save_to_json(extracted_info)

MainMethod()
