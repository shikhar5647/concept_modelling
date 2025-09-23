# app.py
import streamlit as st
from agents.concept_agent import extract_concepts
from utils.storage import save_history

st.set_page_config(page_title="Radiology Concept Extractor", layout="wide")

st.title("🩻 Radiology Concept Extractor (Gemini)")

findings = st.text_area("Paste FINDINGS section:", height=200)

if st.button("Extract Concepts"):
    if findings.strip():
        with st.spinner("Extracting concepts..."):
            output = extract_concepts(findings)
            st.json(output)
            save_history(findings, output)
    else:
        st.warning("Please enter findings text.")
