from dotenv import load_dotenv
load_dotenv() ## loading .env variables
import os
import streamlit as st
import google.generativeai as genai

API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=API_KEY)

# Function to load gemini pro model and get response
model = genai.GenerativeModel('gemini-pro')
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text
st.set_page_config(page_title='Q&A Demo Application')
st.header('Gemini LLM Application')

input = st.text_input('Input: ', key='input')
submit = st.button('Ask the question')

if submit:
    response = get_gemini_response(input)
    st.write(response)




