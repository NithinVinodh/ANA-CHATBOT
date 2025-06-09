import streamlit as st
from utils.pdf_utils import extract_chunks_from_pdf
from utils.llm_utils import ask_gemini

st.title("📄 PDF Chat with Gemini LLM")

api_key = st.secrets.get("GEMINI_API_KEY") or st.text_input("Enter your Gemini API Key", type="password")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file and api_key:
    with st.spinner("Reading and chunking PDF..."):
        chunks = extract_chunks_from_pdf(uploaded_file)
        st.success("PDF processed. You can now ask questions!")

    query = st.text_input("Ask a question based on the PDF")
    if query:
        with st.spinner("Thinking..."):
            result = ask_gemini(api_key, query, chunks)
            st.write("### 📌 Answer:")
            st.markdown(result)
