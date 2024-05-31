import streamlit as st
from app import my_chatbot

st.title("A Bedrock Chatbot with Streamlit")

language = st.sidebar.selectbox("Language", ["english", "spanish"])

if language:
    Question = st.sidebar.text_area(label="what is your question?",
                                         max_chars=100)

if Question:
    response = my_chatbot(language, Question)
    st.write(response['text'])