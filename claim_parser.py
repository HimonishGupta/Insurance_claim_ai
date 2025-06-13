from pdf2image import convert_from_path
import pytesseract

# Step 1: Read the PDF and convert it to images
def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)  # Each page becomes an image
    full_text = ""
    for image in images:
        text = pytesseract.image_to_string(image)  # Extract text from image
        full_text += text + "\n"
    return full_text

# Step 2: Pull out important information from the text
def extract_key_fields(text):
    data = {}
    lines = text.split("\n")  # Split the full text into lines

    for line in lines:
        if "Name:" in line:
            data["name"] = line.split("Name:")[1].strip()
        elif "Hospital:" in line:
            data["hospital"] = line.split("Hospital:")[1].strip()
        elif "Diagnosis:" in line:
            data["diagnosis"] = line.split("Diagnosis:")[1].strip()
        elif "Admission Date:" in line:
            data["admission_date"] = line.split("Admission Date:")[1].strip()
        elif "Discharge Date:" in line:
            data["discharge_date"] = line.split("Discharge Date:")[1].strip()
        elif "Amount Claimed:" in line:
            data["amount_claimed"] = line.split("Amount Claimed:")[1].strip()
    return data
