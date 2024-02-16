import os 

import streamlit as st
from utils.api import call_gemini_api
from utils.preprocessing import generate_prompt
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

gemimi_api_key = os.environ.get("GEMINI_API_KEY")
if not gemimi_api_key:
    raise Exception("Enter GEMINI_API_KEY in .env to continue")

genai.configure(api_key=gemimi_api_key)
# from transformers import pipeline

# Streamlit application
st.title("Smart Scanner AI")
st.write("Enter text below and click 'Submit' to generate command: ")
st.write("Example Useage: ```Continuous ping google.com```")

text_input = st.text_area("Write Here:", placeholder="Enter youe text here")
submit_button = st.button("Generate")

# Loading indicator and progress bar
loading_icon = st.empty()
progress_bar = st.empty()

if submit_button:
    with loading_icon.empty():
        st.write("Processing text...")
        progress_bar.progress(0)

        # Preprocess text
        preprocessed_text = generate_prompt(text_input)

        # Disable submit button and show progress bar
        progress_bar.empty()
        progress_bar = st.progress(10)

        # Call Gemini API (replace with your actual code)
        response = call_gemini_api(preprocessed_text)

        # Display results
        progress_bar.empty()
        st.success("Processing complete!")
        st.write(response.text)

