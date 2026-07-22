import os
from dotenv import load_dotenv, find_dotenv
from pydantic import BaseModel


load_dotenv(find_dotenv())

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

model = ChatMistralAI(model ="mistral-small-2506")

prompt = ChatPromptTemplate.from_messages([
    ("system","""
You are an expert Information Extraction AI.

Your task is to careflly read a movie description and identify the most important factual information.

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

("human",  """
extract information from this paragraph :
{paragraph} 
""")

])

para = input(" Give your Pargraph :")

final_prompt = prompt.invoke(
    {"paragraph": para}
)

response = model.invoke(final_prompt)

print(response.content)