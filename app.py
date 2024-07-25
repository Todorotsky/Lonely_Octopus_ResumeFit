import streamlit as st
from openai import OpenAI
import os


# api_key = os.getenv("OPENAI_API_KEY")  # Used in production - Uncomment this line when you deploy
api_key = "sk-proj-CrZptMGFfT3qHJIriKX9T3BlbkFJUC4i6M6emy33nTxJsf1v" # Used in development - Delete this line when you deploy - This api_key is only made for demonstration purposes


def compare_resume_to_job_description(resume_text, job_description_text):
    # Ensure your OPENAI_API_KEY is set as an environment variable
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return
    client = OpenAI(api_key=api_key)
    model = "gpt-3.5-turbo"  # Using the GPT-3.5 model
    return

st.title('📄 ResumeFit: Compare Your Resume to Job Descriptions')
st.markdown('I was made to to analyze and compare resumes with job postings to identify skill gaps and areas for improvement. Remember, always verify AI-generated responses.')

# Input field for the resume
resume_text = st.text_area("Paste your resume here:")

# Input field for the job description
job_description_text = st.text_area("Paste the job description here:")

if st.button('Compare'):
    # Code to process the inputs and compare the resume with the job description
    if resume_text and job_description_text:
        st.write("Comparing the resume with the job description...")
        comparison_result = compare_resume_to_job_description(resume_text, job_description_text)
        st.write(comparison_result)
    else:
        st.warning("Please enter both the resume and the job description.")