import os
import requests
import streamlit as st
import textwrap
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet

# --- Streamlit Setup ---
st.set_page_config(page_title="Insights Gulfstore Agents", page_icon="🛠️", layout="wide")
st.title("🛠️ Insights Gulfstore – Content & Analysis Agent")

# --- API Config ---
API_KEY = "YOUR_GOOGLE_API_KEY"
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
def create_pdf(content_text, analysis_text, filename="combined_report.pdf"):
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

    doc.build(elements)
    return filename

# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["✍️ Content Creation Agent", "📊 Analyze Content Performance", "📄 Combined Report"])

# ------------------ TAB 1: CONTENT CREATION ------------------ #
with tab1:
    st.header("✍️ Content Creation Agent")

    topic = st.text_input("Enter topic or product name")
    content_type = st.selectbox("Select Content Type", ["Blog Post", "Product Description"])
    word_count = st.slider("Word Count", 100, 1000, 300)

    if st.button("Generate Content"):
        with st.spinner("Generating content..."):
            if content_type == "Blog Post":
                prompt = f"""
                Generate a detailed {content_type} of about {word_count} words for Insights Gulfstore. Topic: {topic}. Use SEO-friendly style.

                Example Blog Post:
                Blog Title: Why External Hard Drives Are Essential for Modern Data Storage
                Meta Description: Discover why external hard drives remain one of the best solutions for secure, portable, and affordable data storage. Learn key benefits and tips before buying.
                Keywords: external hard drives, portable hard disk, best storage solutions, HDD vs SSD, Seagate hard drives
                Tags: Storage, Hard Drives, Data Backup, Technology Tips

                Blog Content (Intro + Sample Section):
                In today’s digital world, managing data securely and efficiently has become a necessity. Whether you’re a student storing projects, a gamer saving progress, or a professional safeguarding files, an external hard drive offers reliability and convenience.

                Benefits of External Hard Drives
                - High Capacity at Low Cost: External HDDs provide terabytes of storage at a fraction of SSD costs.
                - Portability: Slim and lightweight, making them easy to carry for work or travel.
                - Compatibility: Works seamlessly with Windows, macOS, and even gaming consoles.
                - Backup & Security: A reliable option for creating backups and protecting data from system failures.

                By choosing trusted brands like Seagate or Western Digital, you ensure durability, warranty coverage, and peace of mind.

                Rules:
                - Do not provide explanations or mention optimization explicitly.
                - At the end of each response, include an optimization score out of 100.
                - The blog must be detailed, informative, and relevant to www.insightsgulfstore.com (Gulf-based e-commerce specializing in hard disks & storage).
                """
            else:
                prompt = f"""
                Generate a {content_type} of about {word_count} words for Insights Gulfstore. Topic: {topic}. Use SEO-friendly style.

                Example Product Description:
                Product: Seagate 1TB External Hard Drive (USB 3.0, Portable)
                Description:
                Upgrade your storage with the Seagate 1TB External Hard Drive, designed for speed, reliability, and portability. With USB 3.0 support, you can transfer large files, movies, and backups in seconds. Its slim, lightweight design makes it perfect for students, professionals, and gamers who need data on the go. Compatible with Windows, Mac, and gaming consoles, this hard drive is an all-in-one storage solution for work and entertainment. Comes with a 2-year warranty for peace of mind.

                Highlights:
                - 1TB capacity for photos, videos, games, and documents
                - USB 3.0 interface (backward compatible with USB 2.0)
                - Plug-and-play, no software required
                - Slim and portable design for travel
                - Reliable Seagate build quality with 2-year warranty

                Keywords/Tags: Seagate 1TB external hard drive, portable hard disk, USB 3.0 storage device, external HDD for PC, Mac, PS4

                Rules:
                - Do not provide explanations or mention optimization explicitly.
                - At the end of each response, include an optimization score out of 100.
                - The description must match the genre of www.insightsgulfstore.com (Gulf-based e-commerce specializing in hard disks & storage).
                """

            content_output = generate_response(prompt)
            st.session_state["generated_content"] = content_output

        st.subheader("📝 Generated Content")
        st.write(content_output)

        st.download_button("⬇️ Download Content", content_output, file_name="generated_content.txt")

# ------------------ TAB 2: ANALYSIS ------------------ #
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

    # Switch for analysis type
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
            Analytics Framework (Day 2):
            1) Monitoring User Behavior – clicks, navigation paths, scroll depth, forms, cohorts, anomalies.
            2) Tracking KPIs – define 5–7 strategic & behavioral KPIs with owners and cadence.
            3) Visualizing User Activity – funnels, dashboards, alerts, filters.
            4) Analyzing Performance Trends – seasonal effects, correlations, guided analytics.
            5) Supporting Decision-Making – recommendations, ROI, priorities, accessibility.
            6) Best Practices – avoid over-tracking, integrate feedback, ensure privacy.
            """).strip()

            if use_generated:
                context = f"Insights Gulfstore – Analyze this generated content: {st.session_state['generated_content']}"
            else:
                context = "Insights Gulfstore – E-commerce website specializing in hard disks and storage devices. Analyze at site-level"

            prompt = f"{points}\n\nMode: {mode}\nContext: {context}\nOutput Format: Plain Text"

            analysis_output = generate_response(prompt)
            st.session_state["analysis_output"] = analysis_output

            st.subheader("📑 Analysis Result")
            st.write(analysis_output)

            st.download_button("⬇️ Download Analysis", analysis_output, file_name="analysis_output.txt")


# ------------------ TAB 3: COMBINED REPORT ------------------ #
with tab3:
    st.header("📄 Combined Report")

    content_text = st.session_state.get("generated_content", "")
    analysis_text = st.session_state.get("analysis_output", "")

    if not content_text and not analysis_text:
        st.info("⚠️ Please generate content or analysis before creating a report.")
    else:
        combined_text = ""
        if content_text:
            combined_text += f"--- Generated Content ---\n\n{content_text}\n\n"
        if analysis_text:
            combined_text += f"--- Analysis Output ---\n\n{analysis_text}"

        st.text_area("📖 Preview Report", combined_text, height=400)

        # PDF Export
        pdf_file = create_pdf(content_text, analysis_text)
        with open(pdf_file, "rb") as f:
            st.download_button("⬇️ Download Combined Report (PDF)", f, file_name="combined_report.pdf", mime="application/pdf")

        # TXT Export
        st.download_button("⬇️ Download Combined Report (TXT)", combined_text, file_name="combined_report.txt")
