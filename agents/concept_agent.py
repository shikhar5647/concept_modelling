# agents/concept_agent.py
import os
import google.generativeai as genai
from agents.concepts import pneumonia_concepts, covid19_concepts, normal_concepts

SYSTEM = """You are a radiology concept extraction agent.
You will ONLY output valid JSON. 
Your job is to convert FINDINGS into a structured set of medical concepts.
"""

USER_TEMPLATE = """
Task: Extract radiology "concepts" from the FINDINGS section.

Definition: A concept is a short, human-interpretable imaging observation (few words that together mean one clinical idea).  
Examples: "pleural effusion present", "cardiomegaly", "no acute cardiopulmonary disease".

Reference concept lists:
- Pneumonia concepts: {PNEUMONIA}
- COVID-19 concepts: {COVID}
- Normal concepts: {NORMAL}

Output schema (strict JSON only):
{{
  "concepts": [
    {{
      "label": "...",          # short concept (<=5 words)
      "description": "...",    # concise 1-sentence explanation
      "keywords": [...],       # 3-6 synonyms or terms from text
      "confidence": 0.00       # float between 0 and 1
    }},
    ...
  ]
}}

Rules:
1. Only return JSON.
2. If no abnormality → return "no acute cardiopulmonary disease".
3. Do not hallucinate outside radiology domain.
4. Confidence uses 2 decimals.

FINDINGS:
---
{FINDINGS}
---
"""

def extract_concepts(findings: str, model: str = None, api_key: str = None) -> str:
    if api_key:
        genai.configure(api_key=api_key)
    else:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    chosen_model = model or os.getenv("GEMINI_MODEL", "gemini-2.5-pro")

    user_prompt = USER_TEMPLATE.format(
        FINDINGS=findings.strip(),
        PNEUMONIA=", ".join(pneumonia_concepts[:8]), # partial list for context
        COVID=", ".join(covid19_concepts[:8]),
        NORMAL=", ".join(normal_concepts[:8])
    )

    resp = genai.chat.create(
        model=chosen_model,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.0,
        max_output_tokens=800
    )

    if isinstance(resp, dict):
        if "candidates" in resp:
            c0 = resp["candidates"][0]
            if isinstance(c0, dict) and "content" in c0:
                return c0["content"]
        return str(resp)
    return str(resp)
