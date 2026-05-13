from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

def analyze_jobs(jobs_data,role, years, current_role, skills):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    prompt = f"""
    I am aiming for {role} role with {years} of experience {current_role}.These are the skills I have
    {skills}

    Jobs:
    {jobs_data}

    1. Suggest best 5 jobs
    2. What skills I need
    3. How to improve resume
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text