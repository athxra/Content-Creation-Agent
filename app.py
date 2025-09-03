import os
import requests
import streamlit as st
import textwrap
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet

# --- Streamlit Setup ---
st.set_page_config(page_title="Insights Gulfstore Agents", page_icon="🛠", layout="wide")
st.title("🛠 Insights Gulfstore – Content, Analysis & Social Media Agent")

# --- API Config ---
API_KEY = "Your-Google-API"  # replace with your Google Gemini API key
MODEL = "gemini-2.0-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

# --- API Helper ---
def generate_response(prompt):
    headers = {"Content-Type": "application/json"}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return f"API Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Request failed: {e}"

# --- PDF Generator ---
def create_pdf(content_text, analysis_text, social_text, filename="combined_report.pdf"):
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(filename)
    elements = []

    # Title
    elements.append(Paragraph("Insights Gulfstore – Combined Report", styles["Title"]))
    elements.append(Spacer(1, 20))

    def add_section(title, text):
        elements.append(Paragraph(title, styles["Heading2"]))
        lines = text.split("\n")
        bullets = []
        for line in lines:
            line = line.strip()
            if line.startswith("-") or line.startswith("*"):  # bullet point
                bullets.append(ListItem(Paragraph(line[1:].strip(), styles["Normal"])))
            elif line:  # paragraph
                if bullets:
                    elements.append(ListFlowable(bullets, bulletType="bullet"))
                    bullets = []
                elements.append(Paragraph(line, styles["Normal"]))
        if bullets:
            elements.append(ListFlowable(bullets, bulletType="bullet"))
        elements.append(Spacer(1, 12))

    if content_text:
        add_section("Generated Content", content_text)
    if analysis_text:
        add_section("Analysis Output", analysis_text)
    if social_text:
        add_section("Social Media Posts", social_text)

    doc.build(elements)
    return filename

# --- Tabs ---
tab1, tab2, tab3, tab4 = st.tabs([
    "✍ Content Creation Agent",
    "📊 Analyze Content Performance",
    "📱 Social Media Agent",
    "📄 Combined Report"
])

# ------------------ TAB 1: CONTENT CREATION ------------------ #
with tab1:
    st.header("✍ Content Creation Agent")

    topic = st.text_input("Enter topic or product name")
    content_type = st.selectbox("Select Content Type", ["Blog Post", "Product Description"])
    word_count = st.slider("Word Count", 100, 1000, 300)

    if st.button("Generate Content"):
        with st.spinner("Generating content..."):
            if content_type == "Blog Post":
                prompt = f"""
                Generate a detailed {content_type} of about {word_count} words for Insights Gulfstore. 
                Topic: {topic}. Use SEO-friendly style.
                Rules:
                - Do not provide explanations or mention optimization explicitly.
                - At the end of each response, include an optimization score out of 100.
                - The blog must be detailed, informative, and relevant to www.insightsgulfstore.com 
                """
            else:
                prompt = f"""
                Generate a {content_type} of about {word_count} words for Insights Gulfstore. 
                Topic: {topic}. Use SEO-friendly style.
                Rules:
                - Do not provide explanations or mention optimization explicitly.
                - At the end of each response, include an optimization score out of 100.
                """

            content_output = generate_response(prompt)
            st.session_state["generated_content"] = content_output

        st.subheader("📝 Generated Content")
        st.write(content_output)

        st.download_button("⬇ Download Content", content_output, file_name="generated_content.txt")

# ------------------ TAB 2: ANALYSIS ------------------ #
with tab2:
    st.header("📊 Analyze Content Performance")

    modes = [
        "Audit Current Analytics Setup",
        "Define & Prioritize KPIs",
        "Design Dashboards",
        "Analyze Performance Trends",
        "Decision Support Recommendations",
        "Best Practices Checklist",
        "Full Plan (All Sections)"
    ]
    mode = st.selectbox("🎯 Select Analysis Mode", modes)

    use_generated = False
    if "generated_content" in st.session_state and st.session_state["generated_content"]:
        use_generated = st.radio(
            "Select Analysis Type",
            ["Use Generated Content from Tab 1", "Website-Level Analysis"],
            horizontal=True
        ) == "Use Generated Content from Tab 1"

    if st.button("🚀 Run Analysis"):
        with st.spinner("Analyzing content performance..."):
            points = textwrap.dedent("""
            Analytics Framework:
            1) Monitoring User Behavior – clicks, navigation paths, scroll depth.
            2) Tracking KPIs – define 5–7 strategic KPIs.
            3) Visualizing User Activity – dashboards, funnels, alerts.
            4) Analyzing Performance Trends – seasonality and correlations.
            5) Decision Support – ROI and recommendations.
            6) Best Practices – privacy and simplicity.
            """).strip()

            if use_generated:
                context = f"Insights Gulfstore – Analyze this generated content: {st.session_state['generated_content']}"
            else:
                context = "Insights Gulfstore – E-commerce website specializing in hard disks and storage devices."

            prompt = f"{points}\n\nMode: {mode}\nContext: {context}\nOutput Format: Plain Text"
            analysis_output = generate_response(prompt)
            st.session_state["analysis_output"] = analysis_output

            st.subheader("📑 Analysis Result")
            st.write(analysis_output)

            st.download_button("⬇ Download Analysis", analysis_output, file_name="analysis_output.txt")

# ------------------ TAB 3: SOCIAL MEDIA AGENT ------------------ #
with tab3:
    st.header("📱 Social Media Agent")

    platform = st.selectbox("Select Social Media Platform", ["Instagram", "Facebook", "LinkedIn", "Twitter (X)"])
    campaign_goal = st.selectbox("Campaign Goal", ["Brand Awareness", "Product Promotion", "Event Marketing", "Engagement Boost"])
    topic = st.text_input("Enter topic, product, or campaign theme")
    post_count = st.slider("Number of Posts", 1, 5, 3)

    if st.button("✨ Generate Social Media Content"):
        with st.spinner("Creating optimized posts..."):
            prompt = f"""
            You are a Social Media Agent for Insights Gulfstore (Gulf-based e-commerce specializing in storage devices).
            Generate {post_count} {platform} posts for campaign goal: {campaign_goal}.
            Topic/Theme: {topic}.
            Requirements:
            - Each post should include a catchy caption (2–3 sentences).
            - Add 5–10 relevant hashtags.
            - Suggest best posting time for Gulf region audience.
            - Style must be engaging, concise, and aligned with SEO/branding.
            Output format:
            Post #:
            Caption:
            Hashtags:
            Recommended Posting Time:
            """

            posts_output = generate_response(prompt)
            st.session_state["social_posts"] = posts_output

        st.subheader("📑 Generated Social Media Posts")
        st.write(posts_output)

        st.download_button("⬇ Download Posts (TXT)", posts_output, file_name="social_media_posts.txt")

        if "analysis_output" in st.session_state or "generated_content" in st.session_state:
            st.info("✅ Social media posts will also be included in the combined report.")

# ------------------ TAB 4: COMBINED REPORT ------------------ #
with tab4:
    st.header("📄 Combined Report")

    content_text = st.session_state.get("generated_content", "")
    analysis_text = st.session_state.get("analysis_output", "")
    social_text = st.session_state.get("social_posts", "")

    if not content_text and not analysis_text and not social_text:
        st.info("⚠ Please generate content, analysis, or social posts before creating a report.")
    else:
        combined_text = ""
        if content_text:
            combined_text += f"--- Generated Content ---\n\n{content_text}\n\n"
        if analysis_text:
            combined_text += f"--- Analysis Output ---\n\n{analysis_text}\n\n"
        if social_text:
            combined_text += f"--- Social Media Posts ---\n\n{social_text}"

        st.text_area("📖 Preview Report", combined_text, height=400)

        # PDF Export
        pdf_file = create_pdf(content_text, analysis_text, social_text)
        with open(pdf_file, "rb") as f:
            st.download_button("⬇ Download Combined Report (PDF)", f, 
                               file_name="combined_report.pdf", mime="application/pdf")

        # TXT Export
        st.download_button("⬇ Download Combined Report (TXT)", combined_text, 
                           file_name="combined_report.txt")
