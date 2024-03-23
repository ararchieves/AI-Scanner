import os
import google.generativeai as genai

# Load Gemini API client (replace with your actual API client code)
def call_gemini_api(text):

    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(text)
    return response

def configure_gemini_api(api_key):
    if not api_key:
        raise Exception("Enter GEMINI_API_KEY in .env to continue")
    genai.configure(api_key=api_key
    )