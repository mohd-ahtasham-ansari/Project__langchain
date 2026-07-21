import os
import streamlit as st
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="CineExtract | Movie Info Extractor",
    page_icon="🎬",
    layout="centered",
)

# ---------------------------------------------------------------------------
# Cinematic styling
# ---------------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;600&display=swap');

.stApp {
    background: radial-gradient(ellipse at top, #1a1a2e 0%, #0a0a0f 60%, #000000 100%);
    color: #eae6df;
}

/* Hide default streamlit chrome */
#MainMenu, footer, header {visibility: hidden;}

.hero-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 4.2rem;
    letter-spacing: 0.35em;
    text-align: center;
    background: linear-gradient(180deg, #f5d982 0%, #d4a017 45%, #8b6b1f 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0;
    padding-top: 1rem;
    text-shadow: 0 0 40px rgba(212, 160, 23, 0.25);
}

.hero-subtitle {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-size: 1.15rem;
    text-align: center;
    color: #9c9788;
    letter-spacing: 0.08em;
    margin-top: -0.5rem;
    margin-bottom: 2rem;
}

.film-divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, #d4a017, transparent);
    margin: 1.5rem 0 2rem 0;
    opacity: 0.6;
}

.stTextArea textarea {
    background-color: rgba(20, 20, 28, 0.85) !important;
    border: 1px solid #3a3527 !important;
    border-radius: 8px !important;
    color: #eae6df !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.98rem !important;
    box-shadow: inset 0 0 20px rgba(0,0,0,0.4);
}

.stTextArea textarea:focus {
    border: 1px solid #d4a017 !important;
    box-shadow: 0 0 12px rgba(212, 160, 23, 0.35) !important;
}

.stButton > button {
    font-family: 'Bebas Neue', sans-serif;
    letter-spacing: 0.2em;
    font-size: 1.1rem;
    width: 100%;
    background: linear-gradient(180deg, #d4a017 0%, #8b6b1f 100%);
    color: #0a0a0f;
    border: none;
    border-radius: 6px;
    padding: 0.7rem 0;
    box-shadow: 0 4px 20px rgba(212, 160, 23, 0.3);
    transition: all 0.2s ease;
}

.stButton > button:hover {
    box-shadow: 0 6px 28px rgba(212, 160, 23, 0.55);
    transform: translateY(-1px);
    color: #0a0a0f;
}

.result-card {
    background: linear-gradient(160deg, rgba(24,24,32,0.9) 0%, rgba(12,12,16,0.9) 100%);
    border: 1px solid #3a3527;
    border-radius: 12px;
    padding: 2rem 2.2rem;
    margin-top: 1.5rem;
    box-shadow: 0 8px 40px rgba(0,0,0,0.5), inset 0 0 60px rgba(212,160,23,0.03);
    font-family: 'Inter', sans-serif;
    line-height: 1.75;
    white-space: pre-wrap;
}

.result-card h4 {
    font-family: 'Bebas Neue', sans-serif;
    letter-spacing: 0.15em;
    color: #d4a017;
    margin-top: 0;
}

.reel-icon {
    text-align: center;
    font-size: 1.8rem;
    opacity: 0.7;
    margin-bottom: -0.5rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.markdown('<div class="reel-icon">🎞️</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">CINEEXTRACT</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">— an AI reader for the stories behind the screen —</div>', unsafe_allow_html=True)
st.markdown('<div class="film-divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Model + Prompt (unchanged logic from the original script)
# ---------------------------------------------------------------------------
model = ChatMistralAI(model="mistral-small-2506")

prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are an expert Information Extraction AI.

Your task is to carefully read a movie description and identify the most important factual information.

Extract information such as:
- Movie title
- Release year
- Genre(s)
- Director (if mentioned)
- Main cast
- A short summary of the plot
- Language (if mentioned)
- Country (if mentioned)
- Runtime (if mentioned)
- IMDb or other ratings (if mentioned)

Guidelines:
- Extract only information present in the given text.
- Never guess or invent missing information.
- Ignore unnecessary details that are unrelated to the movie.
- Keep the plot summary short and informative.
- Be accurate and concise.
"""),
    ("human", """
extract information from this paragraph :
{paragraph} 
"""),
])

# ---------------------------------------------------------------------------
# Input + action
# ---------------------------------------------------------------------------
para = st.text_area(
    "Paste your movie description below",
    height=200,
    placeholder="e.g. Inception is a 2010 science fiction thriller directed by Christopher Nolan, starring Leonardo DiCaprio...",
)

extract_clicked = st.button("🎬  Extract Movie Details")

if extract_clicked:
    if not para or not para.strip():
        st.warning("Please give your paragraph first.")
    else:
        with st.spinner("Rolling the reel... analyzing the scene..."):
            final_prompt = prompt.invoke({"paragraph": para})
            response = model.invoke(final_prompt)

        st.markdown('<div class="film-divider"></div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="result-card"><h4>EXTRACTED DETAILS</h4>{response.content}</div>',
            unsafe_allow_html=True,
        )