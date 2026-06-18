import streamlit as st
import os
from dotenv import load_dotenv
from modules.resume_parser import extract_text_from_pdf
from modules.resume_analyzer import analyze_resume
from modules.job_matcher import match_job_description
from modules.interview_prep import generate_interview_questions
from modules.cover_letter import generate_cover_letter
from modules.career_roadmap import generate_career_roadmap
from modules.linkedin_summary import generate_linkedin_summary

load_dotenv()

# ─── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Career Coach",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .hero-banner {
        background: linear-gradient(135deg, #0d1b3e 0%, #1a3a6e 40%, #1565c0 70%, #1e88e5 100%);
        border-radius: 16px;
        padding: 2.8rem 2rem 2.4rem 2rem;
        margin-bottom: 1.8rem;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(13, 27, 62, 0.45);
    }
    .hero-banner::before {
        content: "";
        position: absolute;
        top: -60px; left: -60px;
        width: 220px; height: 220px;
        background: rgba(255,255,255,0.04);
        border-radius: 50%;
    }
    .hero-banner::after {
        content: "";
        position: absolute;
        bottom: -80px; right: -40px;
        width: 280px; height: 280px;
        background: rgba(255,255,255,0.03);
        border-radius: 50%;
    }
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 0.4rem;
        letter-spacing: 0.5px;
        position: relative;
        z-index: 1;
    }
    .sub-header {
        color: rgba(255, 255, 255, 0.78);
        font-size: 1rem;
        margin: 0;
        position: relative;
        z-index: 1;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.22);
        color: #90caf9;
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        border-radius: 20px;
        padding: 0.2rem 0.9rem;
        margin-bottom: 0.9rem;
        position: relative;
        z-index: 1;
    }
    .feature-card {
        background: rgba(26, 115, 232, 0.08);
        border-left: 5px solid #1a73e8;
        border-radius: 8px;
        padding: 1rem 1.2rem;
        margin: 0.5rem 0;
        color: var(--text-color);
    }
    .feature-card h4 {
        color: var(--text-color);
        margin-bottom: 0.4rem;
    }
    .feature-card p {
        color: var(--text-color);
        opacity: 0.85;
    }
    .success-box {
        background: rgba(52, 168, 83, 0.12);
        border-left: 5px solid #34a853;
        border-radius: 8px;
        padding: 1rem;
        color: var(--text-color);
    }
    .stButton>button {
        background: linear-gradient(90deg, #1a73e8, #0d47a1);
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #0d47a1, #1a73e8);
    }

    /* ── Prevent horizontal scrolling in AI-generated output ── */

    /* Force all markdown tables to fit inside the column */
    .stMarkdown table {
        width: 100% !important;
        table-layout: fixed !important;
        word-wrap: break-word !important;
        font-size: 0.82rem;
    }
    .stMarkdown th,
    .stMarkdown td {
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
        white-space: normal !important;
        padding: 5px 8px !important;
        hyphens: auto;
    }

    /* Wrap text inside st.code() blocks — no horizontal scroll */
    .stCode > div,
    .stCode pre,
    .stCode code {
        white-space: pre-wrap !important;
        word-break: break-word !important;
        overflow-x: hidden !important;
    }

    /* Prevent the markdown container itself from overflowing */
    .stMarkdown {
        max-width: 100%;
        overflow-x: hidden;
    }
</style>
""", unsafe_allow_html=True)

# ─── Header ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
    <div class="main-header">AI Career Coach</div>
    <div class="sub-header">Your personal AI-powered career development assistant</div>
</div>
""", unsafe_allow_html=True)

# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("Navigation")
    st.markdown("---")

    page = st.radio(
        "Choose a Feature",
        options=[
            "Home",
            "Resume Analyzer",
            "Job Description Matcher",
            "Interview Prep",
            "Cover Letter Generator",
            "Career Roadmap",
            "LinkedIn Summary",
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("### Upload Resume")
    uploaded_file = st.file_uploader(
        "Upload your resume (PDF)",
        type=["pdf"],
        help="Upload a PDF resume to use across all features"
    )

    resume_text = ""
    if uploaded_file:
        resume_text = extract_text_from_pdf(uploaded_file)
        if resume_text:
            st.success(f"Resume loaded! ({len(resume_text.split())} words)")
            st.session_state["resume_text"] = resume_text
        else:
            st.error("Could not extract text. Try another PDF.")
    elif "resume_text" in st.session_state:
        resume_text = st.session_state["resume_text"]
        st.info("Using previously uploaded resume.")

    st.markdown("---")
    st.markdown("### Settings")
    experience_level = st.selectbox(
        "Your Experience Level",
        ["Fresher (0-1 yr)", "Junior (1-3 yrs)", "Mid-level (3-6 yrs)", "Senior (6+ yrs)"]
    )

# ─── Home Page ────────────────────────────────────────────────────────────────
if page == "Home":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="feature-card">
        <h4>Resume Analyzer</h4>
        <p>Get a detailed AI analysis of your resume — strengths, weaknesses, ATS score, and improvement tips.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="feature-card">
        <h4>Interview Prep</h4>
        <p>Generate role-specific interview questions with model answers based on your resume and target job.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="feature-card">
        <h4>LinkedIn Summary</h4>
        <p>Generate a compelling LinkedIn About section that gets you noticed by recruiters.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="feature-card">
        <h4>Job Matcher</h4>
        <p>Paste any job description and get a match score, skill gap analysis, and tailored resume tips.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="feature-card">
        <h4>Cover Letter</h4>
        <p>Generate a personalized, professional cover letter tailored to each job application.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="feature-card">
        <h4>Career Roadmap</h4>
        <p>Get a personalized career development roadmap with skills to learn and goals to achieve.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("### 🎯 How to Get Started")
        st.markdown("""
        1. **Upload your resume** from the sidebar (PDF format)
        2. **Choose a feature** from the navigation menu
        3. **Fill in any extra details** if required
        4. **Click Generate** and get AI-powered results instantly!
        """)
        st.markdown("---")
        st.info("Tip: Upload your resume first to unlock personalized results across all features!")

# ─── Resume Analyzer ──────────────────────────────────────────────────────────
elif page == "Resume Analyzer":
    st.header("Resume Analyzer")
    st.markdown("Get a comprehensive AI-powered analysis of your resume.")

    target_role = st.text_input("Target Job Role (optional)", placeholder="e.g., Data Scientist, Software Engineer")

    if st.button("Analyze My Resume"):
        if not resume_text:
            st.warning("Please upload your resume from the sidebar first.")
        else:
            with st.spinner("Analyzing your resume..."):
                result = analyze_resume(resume_text, target_role, experience_level)
            st.markdown("---")
            st.markdown(result)

# ─── Job Description Matcher ──────────────────────────────────────────────────
elif page == "Job Description Matcher":
    st.header("Job Description Matcher")
    st.markdown("Paste a job description to see how well your resume matches and what skills you need.")

    job_description = st.text_area(
        "Paste the Job Description here",
        height=300,
        placeholder="Paste the full job description from LinkedIn, Naukri, or any job portal..."
    )
    company_name = st.text_input("Company Name (optional)", placeholder="e.g., Google, TCS, Infosys")

    if st.button("Match & Analyze"):
        if not resume_text:
            st.warning("Please upload your resume from the sidebar first.")
        elif not job_description.strip():
            st.warning("Please paste a job description.")
        else:
            with st.spinner("Matching your profile with the job..."):
                result = match_job_description(resume_text, job_description, company_name)
            st.markdown("---")
            st.markdown(result)

# ─── Interview Prep ───────────────────────────────────────────────────────────
elif page == "Interview Prep":
    st.header("Interview Preparation")
    st.markdown("Generate customized interview questions and model answers for your target role.")

    col1, col2 = st.columns(2)
    with col1:
        job_role = st.text_input("Target Job Role", placeholder="e.g., Backend Developer, Data Analyst")
        interview_type = st.selectbox(
            "Interview Type",
            ["Technical Interview", "HR / Behavioral Interview", "System Design", "Mixed (All Types)"]
        )
    with col2:
        num_questions = st.slider("Number of Questions", min_value=5, max_value=20, value=10)
        company_type = st.selectbox("Company Type", ["Startup", "Mid-size Company", "MNC / FAANG", "Government / PSU"])

    if st.button("Generate Interview Questions"):
        if not resume_text:
            st.warning("Please upload your resume from the sidebar first.")
        elif not job_role.strip():
            st.warning("Please enter your target job role.")
        else:
            with st.spinner(f"Generating {num_questions} interview questions..."):
                result = generate_interview_questions(
                    resume_text, job_role, interview_type, num_questions, company_type, experience_level
                )
            st.markdown("---")
            st.markdown(result)

# ─── Cover Letter Generator ───────────────────────────────────────────────────
elif page == "Cover Letter Generator":
    st.header("Cover Letter Generator")
    st.markdown("Generate a professional, personalized cover letter for any job application.")

    col1, col2 = st.columns(2)
    with col1:
        company = st.text_input("Company Name", placeholder="e.g., Infosys, Google")
        job_title = st.text_input("Job Title", placeholder="e.g., Software Developer")
    with col2:
        hiring_manager = st.text_input("Hiring Manager's Name (optional)", placeholder="e.g., Mr. Rajesh Kumar")
        tone = st.selectbox("Letter Tone", ["Professional & Formal", "Friendly & Enthusiastic", "Concise & Direct"])

    job_desc_cl = st.text_area("Job Description (optional but recommended)", height=150,
                                placeholder="Paste the job description for a more personalized letter...")

    if st.button("Generate Cover Letter"):
        if not resume_text:
            st.warning("Please upload your resume from the sidebar first.")
        elif not company or not job_title:
            st.warning("Please enter the company name and job title.")
        else:
            with st.spinner("Writing your cover letter..."):
                result = generate_cover_letter(
                    resume_text, company, job_title, hiring_manager, tone, job_desc_cl
                )
            st.markdown("---")
            st.code(result, language=None)
            st.download_button("Download Cover Letter", result, file_name="cover_letter.txt")

# ─── Career Roadmap ───────────────────────────────────────────────────────────
elif page == "Career Roadmap":
    st.header("Personalized Career Roadmap")
    st.markdown("Get a step-by-step career development plan tailored to your profile and goals.")

    col1, col2 = st.columns(2)
    with col1:
        dream_role = st.text_input("Dream Job / Target Role", placeholder="e.g., AI Engineer, Product Manager")
        timeline = st.selectbox("Timeline Goal", ["6 months", "1 year", "2 years", "5 years"])
    with col2:
        focus_area = st.multiselect(
            "Areas to Focus On",
            ["Technical Skills", "Certifications", "Projects", "Networking", "Soft Skills", "Higher Education"],
            default=["Technical Skills", "Projects"]
        )

    if st.button("Generate My Career Roadmap"):
        if not resume_text:
            st.warning("Please upload your resume from the sidebar first.")
        elif not dream_role.strip():
            st.warning("Please enter your dream job role.")
        else:
            with st.spinner("Creating your personalized career roadmap..."):
                result = generate_career_roadmap(
                    resume_text, dream_role, timeline, focus_area, experience_level
                )
            st.markdown("---")
            st.markdown(result)

# ─── LinkedIn Summary ─────────────────────────────────────────────────────────
elif page == "LinkedIn Summary":
    st.header("LinkedIn Summary Generator")
    st.markdown("Create a compelling LinkedIn 'About' section that attracts recruiters and opportunities.")

    col1, col2 = st.columns(2)
    with col1:
        target_industry = st.text_input("Target Industry", placeholder="e.g., IT, Finance, Healthcare")
        summary_length = st.selectbox("Summary Length", ["Short (150 words)", "Medium (250 words)", "Detailed (400 words)"])
    with col2:
        summary_tone = st.selectbox("Summary Tone", ["Professional", "Storytelling", "Achievement-focused", "Passion-driven"])
        include_cta = st.checkbox("Include Call-to-Action (CTA)", value=True)

    if st.button("Generate LinkedIn Summary"):
        if not resume_text:
            st.warning("Please upload your resume from the sidebar first.")
        else:
            with st.spinner("Crafting your LinkedIn summary..."):
                result = generate_linkedin_summary(
                    resume_text, target_industry, summary_length, summary_tone, include_cta
                )
            st.markdown("---")
            st.code(result, language=None)
            st.download_button("Copy Summary", result, file_name="linkedin_summary.txt")

# ─── Footer ───────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color: var(--text-color); opacity: 0.5;'>AI Career Coach | Built with Python, Streamlit & Groq LLM | "
    "Powered by Llama 3.3 70B</p>",
    unsafe_allow_html=True
)