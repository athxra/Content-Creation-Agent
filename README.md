# Content-Creation-Agent

Content-Creation-Agent is an AI-powered SEO content suggestion tool built with Streamlit and Google Gemini (Generative Language API). It generates actionable SEO strategies, keyword ideas, meta tags, and more for any topic—ideal for marketers, bloggers, and e-commerce managers.

## Features

- Generate SEO content ideas and structure for any topic
- Get keyword suggestions and meta/page tags
- Receive reference links to guides and tools
- Simple, beginner-friendly recommendations and SEO score
- Web interface powered by Streamlit

## Requirements

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [Requests](https://pypi.org/project/requests/)

Install dependencies with:

```bash
pip install streamlit requests
```

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/athxra/Content-Creation-Agent.git
    cd Content-Creation-Agent
    ```

2. **Get a Google Generative Language API key:**
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey) to generate an API key for Gemini.
   - Copy your API key.

3. **Add your API key:**
   - Open `app.py` in a text editor.
   - Find the line:
     ```python
     API_KEY = "YOUR_API_KEY_HERE"
     ```
   - Replace `"YOUR_API_KEY_HERE"` with your actual API key.
   - **Note:** The placeholder is intentionally left for you to securely add your private API key.

4. **(Optional) Add a requirements file:**
   - If not present, create `requirements.txt` with:
     ```
     streamlit
     requests
     ```

## Usage

Run the app with:

```bash
streamlit run app.py
```

- Enter your topic, product, or blog idea.
- Click "Generate SEO Suggestions" to receive tailored recommendations, keywords, meta tags, links, and a quick SEO score.

## Example

Input: `handmade candles blog`

Output includes:
- SEO content ideas and structure
- Suggested keywords like "handmade candles," "natural fragrance," etc.
- Example meta/page tags
- Reference links to SEO guides/tools
- SEO score (0–100) with short explanation

---

For questions or contributions, please open an issue or pull request!
