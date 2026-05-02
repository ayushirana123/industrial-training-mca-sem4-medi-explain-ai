import streamlit as st
import time
import os
from PIL import Image
from difflib import get_close_matches

import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ocr.extract_text import extract_text_from_pdf, extract_text_from_image
from explain.explain_results import explain_medical_report
from utils.text_cleaner import clean_ocr_output
from utils.chatbot import get_chat_response
from utils.pdf_exporter import generate_pdf
from utils.charts import generate_cbc_chart
from utils.parser import parse_lab_report
from utils.hf_ner_parser import extract_lab_results_from_ner
from ml.diagnose import predict_condition

@st.cache_data(show_spinner=False)
def cached_explain(text, model):
    return explain_medical_report(text[:300], model)

st.title("🧪 AI Medical Report Explainer")

model = st.sidebar.selectbox(
    "🧠 Choose AI Model",
    ["llama3.2:1b", "tinyllama:latest", "phi3:mini"],
    index=0
)

uploaded_file = st.file_uploader(
    "Upload Lab Report",
    type=["pdf", "jpg", "jpeg", "png"]
)

if uploaded_file:

    st.success(f"Uploaded: {uploaded_file.name}")

    file_ext = uploaded_file.name.split('.')[-1].lower()

    temp_path = f"temp_upload.{file_ext}"

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    if file_ext in ["jpg", "jpeg", "png"]:
        st.image(Image.open(temp_path), width=450)

    with st.spinner("OCR running..."):
        if file_ext == "pdf":
            raw_text = extract_text_from_pdf(temp_path)
        else:
            raw_text = extract_text_from_image(temp_path)

    st.text_area("OCR Output", raw_text, height=200)

    cleaned_text = clean_ocr_output(raw_text)

    explanation = cached_explain(cleaned_text, model)

    st.subheader("AI Explanation")
    st.markdown(explanation)

    st.subheader("Parsed Values")

    parsed_results = extract_lab_results_from_ner(cleaned_text)
    if not parsed_results:
        parsed_results = parse_lab_report(cleaned_text)

    feature_map = {}

    for item in parsed_results:
        try:
            feature_map[item["name"].lower().strip()] = float(item["value"])
        except:
            pass

    st.code(feature_map)

    st.subheader("ML Diagnosis")

    cbc_required = {
        "haemoglobin": None,
        "mcv": None,
        "platelet count": None,
        "t.l.c": None
    }

    for k in cbc_required:
        key = k.lower()
        if key in feature_map:
            cbc_required[k] = feature_map[key]
        else:
            match = get_close_matches(key, feature_map.keys(), n=1, cutoff=0.6)
            if match:
                cbc_required[k] = feature_map[match[0]]

    # ✅ FIX: PASS DICT (NOT LIST)
    if all(v is not None for v in cbc_required.values()):
        result = predict_condition(cbc_required)
        st.success(f"Diagnosis: {result}")
    else:
        st.info("Insufficient CBC data")

    st.subheader("Chat AI")

    q = st.text_input("Ask question")
    if q:
        st.markdown(get_chat_response(q, explanation, model))