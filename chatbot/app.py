from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

import os
os.environ["OPENAI_API_KEY"] = "sk-WcNbA8gDXwsE0G10eq_sZX3zJDFq7wJtb8Had0zhJBT3BlbkFJF6-ayLj-4SeMyIroDVLYv4uHEAhvt3j0FFBIG_BkYA"
# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
import os
os.environ["LANGCHAIN_API_KEY"] = "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"
# os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Topic Search AI')
input_text=st.text_input("Search the topic you want")

# openAI LLm 
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))