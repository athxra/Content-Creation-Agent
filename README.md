SEO Agents
An AI-powered content creation and analysis tool for e-commerce, built with Streamlit and Google Gemini (Generative Language API). This app helps you generate SEO-friendly content, analyze content performance, and export comprehensive reports.

## Features

- **Content Creation Agent:** Generate detailed blog posts or product descriptions tailored for Gulf-based e-commerce (hard disks & storage focus).
- **Content Performance Analysis:** Audit analytics setup, define KPIs, design dashboards, analyze performance, and get decision support recommendations.
- **Combined Reporting:** Export generated content and analysis as a single PDF or TXT file.
- **SEO Optimization:** Each generated content includes an optimization score out of 100.
- **Web Interface:** User-friendly tabbed UI powered by Streamlit.

## Requirements

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [Requests](https://pypi.org/project/requests/)
- [reportlab](https://pypi.org/project/reportlab/) (for PDF export)

Install dependencies with:

```bash
pip install streamlit requests reportlab
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
     API_KEY = "YOUR_GOOGLE_API_KEY"
     ```
   - Replace `"YOUR_GOOGLE_API_KEY"` with your actual API key.

4. **(Optional) Add a requirements file:**
   - If not present, create `requirements.txt` with:
     ```
     streamlit
     requests
     reportlab
     ```

## Usage

Run the app with:

```bash
streamlit run app.py
```

### App Structure

- **Tab 1: Content Creation Agent**
  - Input topic/product name, select content type (Blog Post/Product Description), set word count.
  - Click "Generate Content" to receive SEO-optimized text and a score.
  - Download generated content as TXT.

- **Tab 2: Analyze Content Performance**
  - Choose analysis mode (e.g. Audit Analytics, KPIs, Dashboard Design, Trends, Recommendations, Best Practices, or Full Plan).
  - Analyze generated content (from Tab 1) or perform website-level analysis.
  - Download analysis output as TXT.

- **Tab 3: Combined Report**
  - Preview and export combined content + analysis as PDF or TXT.

## Example Workflow

1. **Generate Content:**  
   Topic: `Seagate external hard drive`  
   Output: SEO blog or product description about the product, including benefits, keywords, tags, and an optimization score.

2. **Analyze Performance:**  
   Mode: `Full Plan (All Sections)`  
   Output: Analytics framework covering KPIs, dashboards, trends, recommendations, and best practices for content or site.

3. **Export Report:**  
   Download the combined results as PDF or TXT for sharing or record-keeping.

---

For questions or contributions, please open an issue or pull request!
