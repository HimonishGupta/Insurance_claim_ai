import streamlit as st
from claim_parser import extract_text_from_pdf, extract_key_fields

st.title("🧾 AI Insurance Claim Parser")

uploaded_file = st.file_uploader("Upload your claim PDF", type="pdf")

if uploaded_file:
    with open("uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())  # Save the uploaded PDF

    st.write("🔍 Reading and analyzing document...")

    # Step 1: Extract raw text
    raw_text = extract_text_from_pdf("uploaded.pdf")

    # Step 2: Extract key fields
    extracted = extract_key_fields(raw_text)

    st.subheader("✅ Extracted Claim Info:")
    for key, value in extracted.items():
        st.write(f"**{key.replace('_', ' ').title()}**: {value}")
