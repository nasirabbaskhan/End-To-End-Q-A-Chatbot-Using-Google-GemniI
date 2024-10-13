from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

# load the GOOGLE_API_KEY
google_api_key = os.getenv("GOOGLE_API_KEY")


# load the LANGCHAIN_API_KEY
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]= "true"


# creating the chatbot
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Answer all questions to the best of your ability.",),
        # ("user", f"Question: {{question}}"),
        ("user", "Question:{question}")
    ]
)


# Gogle Gemni API calling
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Specify the model to use
    temperature=0.2, 
)
output_parser = StrOutputParser()


# streamlit framwork
st.title("Langchain Chat Demo with Google Gemini API")
user_input = st.text_input("Search the topic you want!")

chain = prompt |llm| output_parser


if user_input:
    st.write(chain.invoke({"question": user_input}))
