"""
modules/resume_analyzer.py
──────────────────────────
Sends the resume to Groq and returns a structured analysis
covering ATS score, strengths, weaknesses, and improvements.
"""

from groq_helper import get_groq_response


SYSTEM_PROMPT = """You are an expert Resume Coach and HR Specialist with 15+ years of experience.
You have deep knowledge of ATS systems, hiring practices in India and globally,
and career development strategies. Provide detailed, actionable, and honest feedback."""


def analyze_resume(resume_text: str, target_role: str, experience_level: str) -> str:
    """
    Analyze a resume and return structured feedback.

    Parameters
    ----------
    resume_text       : Raw text extracted from the resume PDF.
    target_role       : The role the candidate is targeting (may be empty).
    experience_level  : One of the sidebar experience options.
    """
    role_line = f"Target Role: {target_role}" if target_role.strip() else "No specific target role provided."

    prompt = f"""
Analyze the following resume thoroughly and provide a detailed professional report.

{role_line}
Experience Level: {experience_level}

RESUME:
{resume_text}

━━━ ATS SCORING RUBRIC (use this to calculate the score honestly) ━━━
Score each category strictly based on what is actually present in the resume above.
Do NOT give benefit of the doubt — only award points for what is clearly visible.

| Category                        | Max Points | Award Points If...                                                        |
|---------------------------------|------------|---------------------------------------------------------------------------|
| Contact Info completeness       | 10         | Has email, phone, LinkedIn, location. Deduct 2-3 per missing item.        |
| Keywords & Role Match           | 20         | Resume contains keywords relevant to {target_role if target_role.strip() else "the candidate's apparent target role"}. Deduct heavily if generic. |
| Quantified Achievements         | 20         | Uses numbers/metrics (%, $, users, time saved). Deduct per missing metric.|
| Formatting & ATS Parseability   | 15         | No tables, graphics, headers/footers, columns. Clean bullet structure.    |
| Work Experience Quality         | 15         | Strong action verbs, clear impact statements, relevant roles.             |
| Education & Certifications      | 10         | Relevant degree/certs present and clearly formatted.                      |
| Skills Section                  | 10         | Dedicated skills section with relevant technical/soft skills listed.      |

Add up your awarded points to get the final score out of 100.
Be honest — a weak resume should score 40-60, an average one 60-75, a strong one 75-90+.

Provide your analysis in this EXACT format using markdown:

## ATS Compatibility Score: [X/100]
| Category | Points Awarded | Max |
|---|---|---|
| Contact Info | ? | 10 |
| Keywords & Role Match | ? | 20 |
| Quantified Achievements | ? | 20 |
| Formatting & ATS Parseability | ? | 15 |
| Work Experience Quality | ? | 15 |
| Education & Certifications | ? | 10 |
| Skills Section | ? | 10 |
| **Total** | **?** | **100** |

*One-line verdict on the overall score.*

---

## Strengths
List 5-7 specific strengths found in this resume with brief explanations.

---

## Weaknesses & Gaps
List 4-6 specific weaknesses or missing elements, be honest and constructive.

---

## Improvement Suggestions
Provide 6-8 specific, actionable suggestions to improve this resume.

---

## Role Fit Assessment
{'Assess how well this resume fits the target role: ' + target_role if target_role else 'Suggest 3 best-fitting job roles based on this resume.'}

---

## Key Skills Identified
List the technical and soft skills found in the resume.

---

## Critical Issues (Fix Immediately)
Highlight the top 3 things that MUST be fixed before applying to jobs.
"""

    return get_groq_response(
        prompt=prompt,
        system_prompt=SYSTEM_PROMPT,
        temperature=0.5,
        max_tokens=2500,
    )