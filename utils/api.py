import google.generativeai as genai

# Load Gemini API client (replace with your actual API client code)
def call_gemini_api(text):

    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(text)
    return response