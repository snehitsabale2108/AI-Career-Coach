"""
modules/cover_letter.py
───────────────────────
Generates a polished, personalised cover letter
tailored to a specific company and job title.
"""

from groq_helper import get_groq_response


SYSTEM_PROMPT = """You are a professional cover letter writer and career consultant
with expertise in crafting compelling cover letters that land interviews.
You write cover letters that are human, specific, and avoid generic clichés."""


def generate_cover_letter(
    resume_text: str,
    company: str,
    job_title: str,
    hiring_manager: str,
    tone: str,
    job_description: str,
) -> str:
    """
    Generate a tailored cover letter.

    Parameters
    ----------
    resume_text      : Candidate's resume text.
    company          : Target company name.
    job_title        : Job title applying for.
    hiring_manager   : Name of the hiring manager (optional).
    tone             : Writing style / tone.
    job_description  : Job description text (optional).
    """

    tone_map = {
        "Professional & Formal":     "Write in a formal, professional tone. Be respectful and authoritative.",
        "Friendly & Enthusiastic":   "Write in an enthusiastic, warm tone. Show genuine excitement for the role.",
        "Concise & Direct":          "Write in a brief, to-the-point style. No filler — every sentence must add value.",
    }

    tone_instruction = tone_map.get(tone, "Write in a professional tone.")
    manager_line = hiring_manager if hiring_manager.strip() else "Hiring Manager"
    jd_section = f"\n━━━ JOB DESCRIPTION ━━━\n{job_description}" if job_description.strip() else ""

    prompt = f"""
Write a complete, ready-to-send cover letter for the following:

Candidate Applying To: {job_title} at {company}
Addressing: {manager_line}
Tone: {tone}

{tone_instruction}
{jd_section}

━━━ CANDIDATE RESUME ━━━
{resume_text}

━━━ INSTRUCTIONS ━━━
1. Write a COMPLETE cover letter (not a template — a fully written letter)
2. Include proper header with [Candidate Name], [Email], [Phone], [Date]
3. Opening paragraph: Hook the reader, mention the specific role and company
4. Body (2 paragraphs): 
   - Highlight 2-3 SPECIFIC achievements from their resume with numbers/impact
   - Show why THIS company specifically (not generic praise)
5. Closing paragraph: Confident call-to-action, express enthusiasm
6. Professional sign-off
7. Keep it to 300-400 words
8. DO NOT use clichés like "I am writing to express my interest" or "I believe I am a great fit"
9. Use specific details from the resume — mention actual technologies, projects, or achievements

Write the complete letter now. No preamble or explanation — just the letter itself.
"""

    return get_groq_response(
        prompt=prompt,
        system_prompt=SYSTEM_PROMPT,
        temperature=0.8,
        max_tokens=1500,
    )