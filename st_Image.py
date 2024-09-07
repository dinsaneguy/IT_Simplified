import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np

# Set the path for Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Update this path if necessary

def extract_text_from_image(image):
  # Convert the PIL image to a numpy array (OpenCV format)
  image_np = np.array(image)
  
  # Convert the image to grayscale for better OCR results
  gray_image = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
  # Use Tesseract OCR to extract text from the image
  extracted_text = pytesseract.image_to_string(gray_image)
  # Convert the extracted text into a dictionary format
  text_dict = {'content': extracted_text.strip()}
  return text_dict

def main():
  st.title("Medical Report Text Extraction")
  st.write("Upload a medical report image to extract text.")
  # File uploader in Streamlit
  uploaded_file = st.file_uploader("Input")
  if uploaded_file is not None:
    # Open the uploaded image file
    image = Image.open(uploaded_file)
  
    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Extract text from the image
    extracted_text_dict = extract_text_from_image(image)
    # Display extracted text
    st.write("Extracted Text: ")
    ext__text=st.json(extracted_text_dict)
    st.title(extracted_text_dict)

if __name__ == "__main__":
  main()