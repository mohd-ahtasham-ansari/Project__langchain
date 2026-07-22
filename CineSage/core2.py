import os
from dotenv import load_dotenv, find_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List,Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv(find_dotenv())

model = ChatMistralAI(model ="mistral-small-2506")

class Movie(BaseModel):
    Title : str
    Year : int
    Genre : list[str]
    Director : str
    Cast : list[str]
    Summary : str
    Language : str
    Country : str
    Runtime : str
    Rating : float

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    ("system","""
    extract the information from the paragraph
    {format_instruction}
     """),
     ("human","""
    {paragraph}
    """)
]    
)

para = input(" Give your Pargraph :")

final_prompt = prompt.invoke(
    {"paragraph": para,
    "format_instruction": parser.get_format_instructions()
    }
)

response = model.invoke(final_prompt)

print(response.content)