## Radiology Concept Extractor (Gemini)

A simple Streamlit app that extracts clinically meaningful concepts from the FINDINGS section of a radiology report using Google Gemini.

### Features
- Extracts key imaging concepts (e.g., "ground-glass opacities", "pleural effusion")
- Saves input/output pairs to `concept_history.json`
- Clean UI via Streamlit

### Requirements
- Python 3.9+
- A Google Gemini API key

### Setup
1. Clone the repository and navigate into the project directory.
2. (Recommended) Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Configure API Key
Set your Gemini API key via environment variable `GEMINI_API_KEY` before running the app.

- Windows PowerShell:
```powershell
$env:GEMINI_API_KEY = "YOUR_KEY_HERE"
```

- macOS/Linux (bash):
```bash
export GEMINI_API_KEY="YOUR_KEY_HERE"
```

The app will raise a clear error if the variable is not set.

### Run
Start the Streamlit app from the project root:

```bash
streamlit run app.py
```

Open the provided local URL in your browser. Paste the FINDINGS text and click "Extract Concepts".

### Project Structure
- `app.py`: Streamlit UI
- `agents/concept_agent.py`: Gemini client and concept extraction
- `utils/storage.py`: Save/load history to `concept_history.json`
- `pages/`: Streamlit multipage files (if any)

### Notes
- Your API key is read only from the environment; it is not stored in code.
- History is stored locally in `concept_history.json` in the project directory.

### License
MIT
