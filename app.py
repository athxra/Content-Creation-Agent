import streamlit as st
import requests

# --- Config ---
API_KEY = "YOUR_GOOGLE_API_KEY"  # Replace with your actual API key
MODEL = "gemini-2.0-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

def seo_agent(user_input: str):
    prompt = f"""
            You are the content optimization assistant for www.insightsgulfstore.com
            , specializing in products such as hard drives and related accessories.
            For the input: {user_input}, generate the following:
            If the input refers to a product name, code, and keywords, create a compelling, search-friendly product description optimized for e-commerce.
            If the input refers to a blog topic, create:
            A well-structured blog title
            An engaging meta description
            Relevant keywords
            Appropriate tags
            High-quality, detailed content
            Do not provide explanations or mention optimization explicitly in the output.
            At the end of each response, include an optimization score out of 100.
    """

    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    response = requests.post(API_URL, json=data)
    result = response.json()

    try:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"Error: {e}\n\nFull response: {result}"

# --- Streamlit UI ---
st.set_page_config(page_title="SEO Content Agent", page_icon="🔍")

st.title("🔍 SEO Content Creation Agent")
st.write("Enter a topic, product, or blog idea and get SEO suggestions.")

user_input = st.text_input("Enter your topic (e.g., 'handmade candles blog')")

if st.button("Generate SEO Suggestions"):
    if user_input.strip():
        with st.spinner("Generating SEO recommendations..."):
            seo_suggestions = seo_agent(user_input)
        st.subheader("✅ SEO Suggestions")
        st.write(seo_suggestions)
    else:
        st.warning("Please enter a topic first.")
