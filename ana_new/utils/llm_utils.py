import google.generativeai as genai

def ask_gemini(api_key, query, chunks):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")

    # Build prompt
    prompt = "You are an AI assistant. Use the following PDF content to answer the question accurately.\n\n"
    for chunk in chunks:
        prompt += chunk + "\n"

    prompt += f"\nQuestion: {query}\nAnswer:"

    response = model.generate_content(prompt)
    return response.text.strip()
