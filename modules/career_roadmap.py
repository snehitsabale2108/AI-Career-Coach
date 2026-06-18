"""
modules/career_roadmap.py
─────────────────────────
Builds a personalised, phased career development roadmap
for the candidate based on their current profile and dream role.
"""

from groq_helper import get_groq_response


SYSTEM_PROMPT = """You are an experienced Career Development Coach and Mentor
who has guided hundreds of professionals from entry-level to senior positions.
You give realistic, detailed, and motivating career roadmaps with specific action items."""


def generate_career_roadmap(
    resume_text: str,
    dream_role: str,
    timeline: str,
    focus_areas: list,
    experience_level: str,
) -> str:
    """
    Generate a phased career development roadmap.

    Parameters
    ----------
    resume_text      : Candidate's resume text.
    dream_role       : Target / dream job title.
    timeline         : Time horizon (6 months, 1 year, etc.)
    focus_areas      : List of areas to focus on.
    experience_level : Current experience level.
    """

    focus_str = ", ".join(focus_areas) if focus_areas else "Technical Skills, Projects, Networking"

    prompt = f"""
Create a detailed, actionable career roadmap for this candidate.

Dream Role: {dream_role}
Timeline: {timeline}
Current Level: {experience_level}
Focus Areas: {focus_str}

━━━ CANDIDATE RESUME ━━━
{resume_text}

━━━ INSTRUCTIONS ━━━
Analyze the gap between the candidate's current profile and the dream role.
Create a phased roadmap broken down by the timeline: {timeline}.

Format EXACTLY as follows:

## Career Goal: {dream_role}
**Current Status:** [Assess where they are now based on resume]
**Gap Analysis:** [What's missing to reach the dream role]

---

## Where You Are vs. Where You Need to Be

| Skill Area | Current Level | Required Level | Gap |
|------------|--------------|----------------|-----|
[Fill in 6-8 relevant skill areas]

---

## Your {timeline} Roadmap

[Divide timeline into logical phases. For each phase:]

### Phase 1: [Phase Name] ([Time period])
**Goal:** [What to achieve]

**Action Items:**
- [ ] [Specific task with resource/tool]
- [ ] [Specific task]
... (5-7 items)

**Resources:**
- [Specific courses, books, platforms]

**Milestone:** [How to know this phase is complete]

[Repeat for each phase]

---

## Skills to Build (Priority Order)
Rank the top 8 skills to learn, with specific resources for each:
1. **[Skill]** — [Why important] | [Resource: specific course/book/platform]
...

---

## Certifications Recommended
List 3-5 relevant certifications with estimated cost and time.

---

## Projects to Build
Suggest 3 portfolio projects that would impress hiring managers for {dream_role}.
For each: project name, tech stack, what it demonstrates.

---

## Networking Strategy
5 specific networking actions (LinkedIn tips, communities, events) for this role/industry.

---

## Weekly Action Plan (First 4 Weeks)
Give a concrete week-by-week plan for the first month.

---

## Motivational Note
End with a brief, personalized motivational message based on their actual background.
"""

    return get_groq_response(
        prompt=prompt,
        system_prompt=SYSTEM_PROMPT,
        temperature=0.6,
        max_tokens=3000,
    )