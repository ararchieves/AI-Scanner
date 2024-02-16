import streamlit as st
from utils.api import call_gemini_api
from utils.preprocessing import preprocess

# from transformers import pipeline

# Streamlit application
st.title("Smart Scanner AI")
st.write("Enter text below and click 'Submit' to generate command:")

text_input = st.text_area("", placeholder="Enter your text here")
submit_button = st.button("Submit")

# Loading indicator and progress bar
loading_icon = st.empty()
progress_bar = st.empty()

if submit_button:
    with loading_icon.empty():
        st.write("Processing text...")
        progress_bar.progress(0)

        # Preprocess text
        preprocessed_text = preprocess(text_input)

        # Disable submit button and show progress bar
        progress_bar.empty()
        progress_bar = st.progress(10)

        # Call Gemini API (replace with your actual code)
        response = call_gemini_api(preprocessed_text)

        # Display results
        progress_bar.empty()
        st.success("Processing complete!")
        st.json(response)

