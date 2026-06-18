# 🤖 AI Career Coach

An AI-powered career assistant built with Streamlit & Groq LLaMA 3.3 70B — upload your resume and instantly get ATS analysis, JD matching, interview prep, cover letters, career roadmaps, and LinkedIn summaries.

---

## ✨ Overview

**AI Career Coach** is a full-featured career development platform built with Python, Streamlit, and the Groq API (LLaMA 3.3 70B). Upload your resume once and instantly access six AI-powered tools that give you personalized, actionable career guidance — no generic advice, no templates, just intelligence tailored to *your* background.

---

## 🚀 Features

| Feature | Description |
|---|---|
| 📄 **Resume Analyzer** | ATS compatibility scoring across 7 rubric categories, strengths, weaknesses, and critical fixes |
| 🎯 **Job Description Matcher** | Paste any JD and get a match score, skill gap analysis, and tailored resume tweaks |
| 🎤 **Interview Prep** | Role-specific questions with model answers for Technical, HR, System Design, or Mixed interviews |
| ✉️ **Cover Letter Generator** | Personalized, cliché-free cover letters in your chosen tone — with a download button |
| 🗺️ **Career Roadmap** | Phased action plan from your current profile to your dream role, with resources and milestones |
| 💼 **LinkedIn Summary** | SEO-optimised LinkedIn "About" sections in four distinct tones, three lengths |

---

## 🛠️ Tech Stack

- **Frontend / UI** — [Streamlit](https://streamlit.io/) with custom CSS
- **LLM Backend** — [Groq API](https://groq.com/) running **LLaMA 3.3 70B Versatile**
- **PDF Parsing** — PyPDF2 (multi-page, with per-page error handling)
- **Environment Management** — python-dotenv

---

## 📁 Project Structure

```
ai-career-coach/
│
├── app.py                    # Main Streamlit application & UI routing
├── groq_helper.py            # Centralised Groq API client
├── requirements.txt          # Python dependencies
├── .env                      # API key (not committed — see .gitignore)
├── .gitignore
│
└── modules/
    ├── __init__.py
    ├── resume_parser.py      # PDF → plain text extractor
    ├── resume_analyzer.py    # ATS scoring & resume feedback
    ├── job_matcher.py        # Resume ↔ JD match analysis
    ├── interview_prep.py     # Interview Q&A generator
    ├── cover_letter.py       # Personalised cover letter writer
    ├── career_roadmap.py     # Phased career development planner
    └── linkedin_summary.py   # LinkedIn "About" section writer
```

---

### Workflow

1. **Upload your resume** (PDF) from the sidebar — it persists across all features in the session.
2. **Set your experience level** in the sidebar Settings panel.
3. **Select a feature** from the navigation menu.
4. **Fill in any required fields** (target role, job description, company name, etc.).
5. **Click Generate** and receive AI-powered, personalised results instantly.

---

## Application Link
[AI Career Coach](https://aicareercoachh.streamlit.app/)

---

## 🗺️ Roadmap

- [ ] Support for DOCX resume uploads
- [ ] Side-by-side resume comparison (before vs. after suggestions)
- [ ] Exportable career roadmap as PDF
- [ ] Multi-language cover letter generation
- [ ] Persistent session history with download-all option

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add: description of feature"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please make sure your code follows the existing module structure and includes docstrings for any new functions.

---

## Author

**Snehit Sabale**
[GitHub](https://github.com/snehitsabale2108)

---


<div align="center">
  Built with ❤️ using Python, Streamlit & Groq LLM
</div>
