# pages/1_History.py
import streamlit as st
from utils.storage import load_history

st.title("📖 Extraction History")

history = load_history()

if not history:
    st.info("No history found yet.")
else:
    for i, entry in enumerate(history[::-1], 1):
        with st.expander(f"Case {i}"):
            st.markdown("**Findings:**")
            st.write(entry["findings"])
            st.markdown("**Extracted Concepts:**")
            st.json(entry["concepts"])
