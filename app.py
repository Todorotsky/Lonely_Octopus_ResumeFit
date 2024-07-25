import streamlit as st
from openai import OpenAI
import os

# api_key = os.getenv("OPENAI_API_KEY")  # Used in production - Uncomment this line when you deploy
api_key = "sk-proj-CrZptMGFfT3qHJIriKX9T3BlbkFJUC4i6M6emy33nTxJsf1v" # Used in development - Delete this line when you deploy - This api_key is only made for demonstration purposes

st.title('🤖 AI Data Interview Assistant')
st.markdown('I was made to you answer Data interview questions. This app demonstrates how to use OpenAI GPT-3.5 to answer data-related interview questions in a deployed envionment. Remember, always verify AI-generated responses.')

# Input field for the resume
resume_text = input("Paste your resume here: ")

# Input field for the job description
job_description_text = input("Paste the job description here: ")
