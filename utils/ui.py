import streamlit as st

def show_title_and_tagline():
    # Info
    st.title("Deep Threat")
    # Tagline 
    st.subheader("An Intelligent Network Vulnerability Scanner Tool")



def input_section():
    st.title("Deep Threat")
    st.subheader("An Intelligent Network Vulnerability Scanner Tool")

    st.markdown('---')

    st.write("Enter text below and click 'Submit' to generate command: ")
    st.write("Example Useage: `Continuous ping google.com`")
    warning_message_container = st.empty()

    text_input = st.text_area("Enter your query:", placeholder="Enter your text here")
    submit_button = st.button("Generate")

    return text_input, submit_button, warning_message_container


def command_generation_section(text_input):
    if text_input == '':
        return False, "Please enter text to generate command!"
    
    loading = st.empty()
