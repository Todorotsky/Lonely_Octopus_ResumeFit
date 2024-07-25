import streamlit as st
from openai import OpenAI
import os


api_key = os.getenv("OPENAI_API_KEY")  # Used in production - Uncomment this line when you deploy


def compare_resume_to_job_description(resume_text, job_description_text):
    # Ensure your OPENAI_API_KEY is set as an environment variable
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return
    client = OpenAI(api_key=api_key)
    model = "gpt-3.5-turbo"  # Using the GPT-3.5 model
    # Instructions for the AI (adjust if needed)
    prompt = f"""
    You are a professional career recruiter for the company. 
    In the top, give a statement in bold of your decision whether you would hire the user or not and give your qualification percentage of the user. Talk to them in second person.
    The user has given you their resume. Analyze and compare the resume to the job description. Identify skill gaps and areas for improvement if needed.
    Resume: {resume_text}
    Job Description: {job_description_text}
    """
    messages = [
        {
        "role": "system", 
        "content": prompt
        }
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0  # Lower temperature for less random responses
    )
    return response.choices[0].message.content

st.title('📄 ResumeFit: Compare Your Resume to Job Descriptions')
st.markdown('I was made to to analyze and compare resumes with job postings to identify skill gaps and areas for improvement. Remember, always verify AI-generated responses.')

# File uploader for the resume
uploaded_file = st.file_uploader("Upload your resume file (PDF or TXT):", type=['pdf', 'txt'])

# Input field for the resume
resume_text = st.text_area("Paste your resume here:")

# Input field for the job description
job_description_text = st.text_area("Paste the job description here:")

# Read the uploaded file if it exists
if uploaded_file is not None:
    if uploaded_file.type == "text/plain":
        resume_text = str(uploaded_file.read(), 'utf-8')
    elif uploaded_file.type == "application/pdf":
        import PyPDF2
        pdf_reader = PyPDF2.PdfFileReader(uploaded_file)
        resume_text = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            resume_text += page.extract_text()

if st.button('Compare'):
    # Code to process the inputs and compare the resume with the job description
    if (resume_text or uploaded_file) and job_description_text:
        st.write("Comparing the resume with the job description...")
        comparison_result = compare_resume_to_job_description(resume_text, job_description_text)
        if comparison_result:
            st.write(comparison_result)
    else:
        st.warning("Please enter both the resume and the job description.")