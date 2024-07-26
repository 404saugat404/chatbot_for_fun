from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os

import streamlit as st

api_key = os.getenv('open_ai_api')


def open_ai_responst(question):
    llm=OpenAI(openai_api_key=api_key,model_name='gpt-3.5-turbo-instruct',temperature=0.6)
    response=llm(question)
    return response

st.set_page_config("Q&A")
st.header('langchain application')
input=st.text_input("input",key="input")
response=open_ai_responst(input)
submit_button=st.button('ask the question')
if submit_button:
    st.subheader('response is :')
    st.write(response)