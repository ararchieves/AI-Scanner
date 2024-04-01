import os 

import streamlit as st
from utils.api import call_gemini_api, configure_gemini_api
from utils.general import execute_command, generate_prompt, parse_response
import utils.ui as ui

import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()


def main():
    ## State Management
    st.session_state.setdefault('submit', False)
    st.session_state.setdefault('verify', False)
    st.session_state.setdefault('exec', False)

    ## Input Section
    text_input, submit_button, warning_container = ui.input_section()
    main = st.container()
    ## Command Generation Section
    if submit_button or st.session_state["submit"]:
        if text_input == '':
            warning_container.error("Please enter text to generate command!")
            st.stop()

        # Generate Command Logic
        loading = st.empty()
        loading.progress(10)

        request = generate_prompt(text_input)
        loading.progress(20)

        response = call_gemini_api(request)
        loading.progress(90)
        result = parse_response(response)
        loading.progress(100)

        loading.empty()

        print(f"result: {result}")
        # Check if command generation was successful
        if result.get('status') == 0:
            warning_container.error(result.get('command'))
            st.stop()

        st.session_state['command'] = result.get('command')
        st.session_state["verify"] = True


    if st.session_state['verify']:
        with main.container():
            st.subheader("Verify Command:")
            st.text_input("Comfirm or Edit Command:", value=st.session_state['command'], key='command')

            if st.button('Verify'):
                st.session_state['verify'] = False
                st.session_state['exec'] = True

                st.rerun()

    elif st.session_state['exec']:
        with main.container():
            st.subheader('Result:')
            execute_command(st.session_state['command'])

            if st.button('clear'):
                st.session_state['exec'] = False
                st.session_state['submit'] = False

                st.rerun()
    

if __name__ == "__main__":
  GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
  configure_gemini_api(GEMINI_API_KEY)

  main()