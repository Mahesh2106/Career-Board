import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate
import streamlit as st

# Assign the OpenAI API key
openai_api_key = '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'

st.title('Career Consultation Chatbot')
input_text = st.text_input('Search your query')

first_input_prompt = PromptTemplate(input_variables=['query'], template='career information about {query}')

# Create an instance of the OpenAI class with the API key as a named parameter
llm = OpenAI(openai_api_key=openai_api_key, temperature=0.8)
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True)

if input_text:
    st.write(chain.run(input_text))