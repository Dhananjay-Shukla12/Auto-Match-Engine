import streamlit as st
from fpdf import FPDF
import time
from scraper import all_data
from ai import analyze_jobs
# ---------------------------------------------------------
# 1. THE PDF GENERATOR
# ---------------------------------------------------------
def clean_text(text):
    return text.replace("—", "-").replace("’", "'")
def create_pdf(feedback_text):
    clean = clean_text(feedback_text)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf_bytes = pdf.output(dest='S').encode('latin-1', errors='replace')
    
    # Add Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Job Market Analysis Report", ln=True, align='C')
    pdf.ln(10) # Line break
    
    # Add Feedback Text
    pdf.set_font("Arial", size=12)
    # Multi_cell handles text wrapping automatically
    pdf.multi_cell(0, 10, txt=clean) 
    
    # Output as string of bytes for Streamlit to download
    return pdf.output(dest='S').encode('latin-1')

# ---------------------------------------------------------
# 2. THE STREAMLIT UI
# ---------------------------------------------------------
# Page Config
st.set_page_config(page_title="Resume to Job Matching Engine", page_icon="📈", layout="centered")

st.title("Market Analysis Engine")
st.markdown("Enter a job query to scrape live postings and generate an AI feedback report.")

# User Inputs
current_role = st.text_input("Current Designation", placeholder="e.g., AI Engineer")
experience = st.text_input("Experience in current role", placeholder="e.g., 2 year")
current_skills = st.text_area("Your Current Skills", placeholder="e.g., Python, Playwright, Automation Testing")
job_query = st.text_input("Target Role", placeholder="e.g., Full Stack Developer")

# The Action Button
if st.button("Analyze Market"):
    if not job_query or not current_skills:
        st.warning("Please enter both a query and your skills.")
    else:
        with st.spinner("Initializing Playwright... Scrape in progress..."):
            live_job_data = all_data(job_query)
            result = analyze_jobs(live_job_data,job_query, experience, current_role, current_skills)
            
            # --- 🚀 YOUR CODE GOES HERE ---
            # 1. Call your Playwright script here, passing 'job_query'
            # time.sleep(2) # Fake scraping time
            # scraped_data = "Simulated scraped job data: Requires Python, Docker, and CI/CD."
            
            # # 2. Call Gemini here, passing 'scraped_data' and 'current_skills'
            # time.sleep(2) # Fake AI thinking time
            # ai_feedback = f"""Based on your skills ({current_skills}), here is your feedback for '{job_query}':
            
            # st.success("Analysis Complete!")
            
            # Display the result to the user
            # st.subheader("AI Feedback")
            st.write(result)
            
            # ---------------------------------------------------------
            # 3. THE PDF DOWNLOAD BUTTON
            # ---------------------------------------------------------
            pdf_bytes = create_pdf(result)
            
            st.download_button(
                label="📄 Download Report as PDF",
                data=pdf_bytes,
                file_name="Job_Analysis_Report.pdf",
                mime="application/pdf"
            )