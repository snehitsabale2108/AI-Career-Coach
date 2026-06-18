"""
modules/interview_prep.py
─────────────────────────
Generates customised interview Q&A pairs based on the
candidate's resume, target role, and interview type.
"""

from groq_helper import get_groq_response


SYSTEM_PROMPT = """You are an expert Interview Coach with experience at top tech companies
and consulting firms. You know what interviewers from startups, MNCs, and FAANG companies
ask, and you craft questions that are highly relevant to each candidate's background."""


def generate_interview_questions(
    resume_text: str,
    job_role: str,
    interview_type: str,
    num_questions: int,
    company_type: str,
    experience_level: str,
) -> str:
    """
    Generate personalised interview questions with model answers.

    Parameters
    ----------
    resume_text      : Candidate's resume text.
    job_role         : Target job title.
    interview_type   : Technical / HR / System Design / Mixed.
    num_questions    : How many Q&As to generate.
    company_type     : Startup / Mid-size / MNC / Government.
    experience_level : Fresher / Junior / Mid-level / Senior.
    """

    type_instructions = {
        "Technical Interview": "Focus on domain-specific technical questions, coding problems, and tools/frameworks mentioned in the resume.",
        "HR / Behavioral Interview": "Focus on behavioral questions using STAR method, culture fit, strengths/weaknesses, and situational questions.",
        "System Design": "Focus on system design, architecture decisions, scalability, and high-level design questions.",
        "Mixed (All Types)": "Include a balanced mix of technical, behavioral, and situational questions.",
    }

    instruction = type_instructions.get(interview_type, "Mix of all question types.")

    prompt = f"""
Generate exactly {num_questions} interview questions with detailed model answers for:

Role: {job_role}
Interview Type: {interview_type}
Company Type: {company_type}
Experience Level: {experience_level}

Special Instructions: {instruction}

━━━ CANDIDATE'S RESUME ━━━
{resume_text}

━━━ INSTRUCTIONS ━━━
- Make questions SPECIFIC to this candidate's actual experience shown in the resume
- Reference their actual projects, technologies, and skills
- For HR questions, refer to their actual work history
- Provide model answers that the CANDIDATE THEMSELVES could use based on their background

Format EXACTLY like this for each question:

---

### Q[N]: [Question Text]

**Why This Is Asked:**
[1-2 sentences on what the interviewer is testing]

**Model Answer:**
[A detailed, personalized answer the candidate can adapt based on their resume]

**Pro Tip:**
[One key tip to nail this specific question]

---

Generate all {num_questions} questions following this format.
End with a section:

## Final Interview Tips for {job_role} at a {company_type}
[5 bullet points of specific advice for this role/company type]
"""

    return get_groq_response(
        prompt=prompt,
        system_prompt=SYSTEM_PROMPT,
        temperature=0.7,
        max_tokens=3000,
    )