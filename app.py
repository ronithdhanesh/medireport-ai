import streamlit as st 
from llm_utils import extract_data, evaluate_data
from scratch import pdf_to_text
import tempfile
#C:/Python313/python.exe -m streamlit run app.py

st.title("MEDICAL REPORT ANALYZER")

st.subheader("""Lets get a medical report analysis of your blood report""")
st.write("Please dont mind the basic UI, ive just started learning streamlit ")

st.write("Okay so without any further ado lets get started, please upload your blood report")

uploaded_file = st.file_uploader("Upload files")


if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_pdf_path = tmp_file.name

    # extracted_text = pdf_to_text(temp_pdf_path)
    
    # extracted_data = extract_data(extracted_text)

    button = st.button("Analyze")

    if button:
        with st.spinner("evaluating report.."):
            extracted_text = pdf_to_text(temp_pdf_path)
    
            extracted_data = extract_data(extracted_text)
            st.write(evaluate_data(extracted_data))
