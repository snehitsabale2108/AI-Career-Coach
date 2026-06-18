"""
modules/job_matcher.py
──────────────────────
Compares resume text against a pasted job description.
Returns a match score, skill gap analysis, and tailored advice.
"""

from groq_helper import get_groq_response


SYSTEM_PROMPT = """You are a senior Talent Acquisition Specialist and ATS expert.
You understand exactly what recruiters and hiring managers look for when matching
candidates to job descriptions. Provide precise, actionable analysis."""


def match_job_description(resume_text: str, job_description: str, company_name: str) -> str:
    """
    Match a resume to a job description and return a detailed report.

    Parameters
    ----------
    resume_text      : Plain text of the candidate's resume.
    job_description  : Full text of the target job description.
    company_name     : Optional company name for personalisation.
    """
    company_line = f"Target Company: {company_name}" if company_name.strip() else ""

    prompt = f"""
You are analyzing how well a candidate's resume matches a specific job description.

{company_line}

━━━ RESUME ━━━
{resume_text}

━━━ JOB DESCRIPTION ━━━
{job_description}

Provide your analysis in this EXACT format using markdown:

## Overall Match Score: [X%]
*One-line verdict on the match.*

---

## Matching Skills & Keywords
List all skills, technologies, and keywords that appear in BOTH the resume and JD.
Format as a bullet list.

---

## Missing Skills & Keywords
List all required skills/keywords from the JD that are MISSING from the resume.
Mark each as:
- 🔴 Critical (must-have)
- 🟡 Important (good to have)
- 🟢 Bonus (nice to have)

---

## How to Improve Your Match Score
Give 5-7 specific, actionable steps to improve the match for this job.
Include which resume sections to update and what to add.

---

## Keywords to Add to Resume
List exact keywords from the JD that the candidate should incorporate into their resume.

---

## Should You Apply?
Give a clear recommendation with reasoning:
- If match ≥ 70%: Encourage applying with suggested tweaks
- If match 40–69%: Apply after making improvements, explain what to fix
- If match < 40%: Advise on whether to apply and what skills to build first

---

## Quick Resume Tweaks for This Job
List 3-5 immediate changes to the resume that would increase the match score for this specific JD.
"""

    return get_groq_response(
        prompt=prompt,
        system_prompt=SYSTEM_PROMPT,
        temperature=0.4,
        max_tokens=2500,
    )