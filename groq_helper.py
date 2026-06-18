"""
groq_helper.py
──────────────
Central Groq API client.  Every module calls get_groq_response() so that
model name and key are configured in exactly one place.
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

_client = None


def _get_client() -> Groq:
    """Lazy-initialise the Groq client (reads GROQ_API_KEY from .env)."""
    global _client
    if _client is None:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise EnvironmentError(
                "GROQ_API_KEY not found. "
                "Please add it to your .env file:\n  GROQ_API_KEY=your_key_here"
            )
        _client = Groq(api_key=api_key)
    return _client


def get_groq_response(
    prompt: str,
    system_prompt: str = "You are an expert AI Career Coach.",
    model: str = "llama-3.3-70b-versatile",
    temperature: float = 0.7,
    max_tokens: int = 2048,
) -> str:
    """
    Send a prompt to Groq and return the assistant's reply as a string.

    Parameters
    ----------
    prompt        : The user-facing question / instruction.
    system_prompt : Role / persona for the model.
    model         : Groq model identifier.
    temperature   : 0 = deterministic, 1 = creative.
    max_tokens    : Maximum response length.
    """
    try:
        client = _get_client()
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": prompt},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content.strip()

    except Exception as exc:
        return f" Error communicating with Groq API: {exc}"