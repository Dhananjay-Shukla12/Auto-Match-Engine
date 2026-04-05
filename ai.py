from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

def analyze_jobs(jobs_data):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    prompt = f"""
    I am a beginner aiming for AI Engineer role with three years of experience in TOSCA testing.

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