from langchain.llms import openai
from dotenv import load_dotenv
load_dotenv()
import os

import streamlit as st

api_key = os.getenv('open_ai_api')
print(api_key)

def open_ai_responst(question):
    