import streamlit as st
import requests

# --- Config ---
API_KEY = "YOUR_API_KEY_HERE"
MODEL = "gemini-2.0-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

def seo_agent(user_input: str):
    prompt = f"""
    You are an SEO assistant of www.insightsgulfstore.com. 
    For the input: "{user_input}", generate:
    1. How SEO can be implemented (content ideas, structure, etc.)
    2. A list of suggested keywords
    3. Example meta/page tags
    4. A few reference links (useful guides or tools)
    5. Provide an SEO score (0–100) with a short explanation.
    Keep it short, clear, and beginner friendly.
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
