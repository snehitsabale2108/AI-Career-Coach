"""
modules/linkedin_summary.py
────────────────────────────
Generates a compelling LinkedIn 'About' section
tailored to the candidate's background and goals.
"""

from groq_helper import get_groq_response


SYSTEM_PROMPT = """You are a LinkedIn branding expert and professional copywriter
who has helped thousands of professionals craft LinkedIn profiles that attract
recruiters and opportunities. You write authentic, compelling 'About' sections
that rank well in LinkedIn search and get noticed."""


def generate_linkedin_summary(
    resume_text: str,
    target_industry: str,
    summary_length: str,
    summary_tone: str,
    include_cta: bool,
) -> str:
    """
    Generate a LinkedIn 'About' section.

    Parameters
    ----------
    resume_text      : Candidate's resume text.
    target_industry  : Industry the candidate is targeting.
    summary_length   : Short / Medium / Detailed.
    summary_tone     : Professional / Storytelling / Achievement / Passion.
    include_cta      : Whether to include a call-to-action at the end.
    """

    length_map = {
        "Short (150 words)":    "Write exactly 130-160 words.",
        "Medium (250 words)":   "Write exactly 230-270 words.",
        "Detailed (400 words)": "Write exactly 380-420 words.",
    }

    tone_map = {
        "Professional":         "Use a polished, formal tone. Focus on expertise and credibility.",
        "Storytelling":         "Tell a compelling story of the candidate's journey. Use narrative structure.",
        "Achievement-focused":  "Lead with measurable achievements and quantified impact. Be results-driven.",
        "Passion-driven":       "Show genuine enthusiasm for the field. Let personality shine through.",
    }

    length_instruction = length_map.get(summary_length, "Write 200-250 words.")
    tone_instruction = tone_map.get(summary_tone, "Write professionally.")
    industry_line = f"Target Industry: {target_industry}" if target_industry.strip() else ""
    cta_instruction = (
        "End with a clear call-to-action (e.g., 'Feel free to connect' / 'Open to opportunities in...')."
        if include_cta else "No call-to-action needed."
    )

    prompt = f"""
Write a LinkedIn 'About' section for this candidate.

{industry_line}
Tone: {summary_tone}
Length: {summary_length}

━━━ CANDIDATE RESUME ━━━
{resume_text}

━━━ INSTRUCTIONS ━━━
1. {length_instruction}
2. {tone_instruction}
3. {cta_instruction}
4. Start with a STRONG hook — NOT "I am a..." or "My name is..."
5. Naturally weave in keywords relevant to {target_industry if target_industry else "their field"} for LinkedIn SEO
6. Highlight 2-3 SPECIFIC achievements with numbers from the resume
7. Show what makes this person unique
8. Use first person ("I"), not third person
9. No bullet points — write in flowing paragraphs
10. Do NOT use overused phrases like "passionate professional", "results-driven", "team player"

Write ONLY the LinkedIn About section — no preamble, no explanation, no labels.
Start directly with the hook sentence.
"""

    return get_groq_response(
        prompt=prompt,
        system_prompt=SYSTEM_PROMPT,
        temperature=0.85,
        max_tokens=700,
    )