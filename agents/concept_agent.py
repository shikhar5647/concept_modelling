import os
import google.generativeai as genai

# Configure Gemini with API key from environment
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY environment variable is not set. Please set it before running the app."
    )

genai.configure(api_key=GEMINI_API_KEY)

def extract_concepts(findings: str) -> list:
    """
    Given the findings section of a medical report,
    extract clinically meaningful concepts using Gemini.
    """
    prompt = f"""
    You are an expert radiologist AI.
    Extract key medical imaging CONCEPTS (not sentences, not paraphrasing)
    from the following 'Findings' text.
    A concept is a medically meaningful phrase, such as
    'ground-glass opacities', 'pleural effusion', 'air bronchograms', etc.
    Return them as a bullet-point list, no explanations.

    Findings:
    {findings}
    """

    # Load Gemini model
    model = genai.GenerativeModel("gemini-2.5-pro")

    # Single-shot generation
    response = model.generate_content(prompt)

    # Extract text and clean to list
    text = response.text.strip()
    concepts = [line.lstrip("-• ").strip() for line in text.splitlines() if line.strip()]

    return concepts
