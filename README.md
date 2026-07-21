# CineSage: LangChain Movie Info Extractor

**CineSage** is a LangChain-powered application designed to act as an expert Information Extraction AI. It processes movie descriptions and accurately extracts factual information such as title, release year, genres, director, cast, and more.

## UI Screenshot

<!-- USER: PASTE YOUR UI SCREENSHOT HERE ON GITHUB --><img width="1919" height="821" alt="image" src="https://github.com/user-attachments/assets/a0b6fe12-2111-488e-aff0-6efe07dd6d1c" /><img width="1899" height="807" alt="image" src="https://github.com/user-attachments/assets/e00f8018-8c9d-4a37-b6d7-5203989181cd" />




## Features
- **Information Extraction**: Extracts structured data from unstructured movie paragraphs.
- **Powered by Mistral AI**: Uses `ChatMistralAI` with the `mistral-small-2506` model.
- **LangChain Integration**: Built using `langchain-core` and `langchain-mistralai`.

## Prerequisites
- Python 3.12+ (or compatible version)
- A Mistral AI API key (configured in your `.env` file)

## Setup and Installation

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repository-url>
   cd Project__Langchain
   ```

2. **Set up the virtual environment**:
   This project uses `uv` for dependency management.
   ```bash
   # Create a virtual environment
   uv venv

   # Activate the virtual environment
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install Dependencies**:
   Install from `requirements.txt` or `pyproject.toml` (if you are using uv):
   ```bash
   pip install -r requirements.txt
   # OR
   uv pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Create a `.env` file in the root directory and add your API keys:
   ```env
   MISTRAL_API_KEY=your_mistral_api_key_here
   ```

## Usage

You can run CineSage via its cinematic web interface or as a command-line script.

### Web UI (Recommended)
To run the Streamlit application:
```bash
uv run streamlit run CineSage/UIcore.py
```

### Command Line
To run the core extraction logic in the terminal:
```bash
python CineSage/core.py
```
When prompted, paste a paragraph describing a movie to get the extracted details.

---

## 📈 Project Progress

We will use this section to track the progress of the project as we add new features and make improvements.

- [x] Initialized project and virtual environment with `uv`.
- [x] Set up Git repository.
- [x] Created the basic `CineSage/core.py` LangChain prompt for movie information extraction.
- [x] Fixed the message type capitalization error (`System` -> `system`, `Human` -> `human`).
- [ ] Implement robust error handling for missing API keys.
- [ ] Add support for extracting data into structured JSON output (Pydantic).
- [ ] (Add more tasks here as we progress)

## Troubleshooting & Learnings

### Mistral API "Unauthorized" Error
If you encounter an `httpx.HTTPStatusError: 401 Unauthorized` (with detail: `{"detail":"Unauthorized"}`) when running the script, it means the `MISTRAL_API_KEY` is either invalid or not being picked up from the `.env` file.

**Learning**: Even if you import `load_dotenv` from the `python-dotenv` package, you must actually call `load_dotenv(find_dotenv())` before initializing the LangChain models (like `ChatMistralAI`). Without executing `load_dotenv()`, the environment variables remain unloaded, leading to API authentication failures.

### Streamlit "ModuleNotFoundError"
If you encounter `ModuleNotFoundError: No module named 'langchain_mistralai'` when running the Streamlit app, it means you are using the global system Python instead of the project's virtual environment.

**Learning**: When using a virtual environment manager like `uv`, always prefix your commands with `uv run` (e.g., `uv run streamlit run CineSage/UIcore.py`). This ensures the command executes within the virtual environment where all your project dependencies (like `langchain-mistralai` and `streamlit`) are installed, rather than falling back to the global Python environment.
