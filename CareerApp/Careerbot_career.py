from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate
import streamlit as st

from langchain.chains import SequentialChain

openai_api_key = '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'

st.title('Career Consultation Chatbot')
input_text = st.text_input('Search the career you want')

first_input_prompt = PromptTemplate(input_variables=['Profession'], template='job description of {Profession}')
llm = OpenAI(openai_api_key=openai_api_key, temperature=0.8)
chain1 = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='Job Description')

second_input_prompt = PromptTemplate(input_variables=['Profession'], template='what are the skills required for {Profession} and the qualifications required for {Profession}')
chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='Skills and Qualifications Required')

third_input_prompt = PromptTemplate(input_variables=['Profession'], template='what is the salary range for {Profession} in India')
chain3 = LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key='Expected Salary')

fourth_input_prompt = PromptTemplate(input_variables=['Profession'], template='what is the scope of {Profession} in India and steps to be a {Profession} in India')
chain4 = LLMChain(llm=llm, prompt=fourth_input_prompt, verbose=True, output_key='Scope and Steps to become one')

parent_chain=SequentialChain(chains=[chain1,chain2,chain3,chain4], input_variables=['Profession'],output_variables=['Job Description','Skills and Qualifications Required','Expected Salary','Scope and Steps to become one'], verbose=True)

if input_text:
    st.write(parent_chain({'Profession':input_text}))