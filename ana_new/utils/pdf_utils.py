import PyPDF2

def extract_chunks_from_pdf(file, chunk_size=1000):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    # Chunking the text
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks
