import subprocess
import streamlit as st
import json

def execute_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    text_container = st.empty()
    complete_text = ""
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while True:
            output = process.stdout.readline().decode()
            if output:
                complete_text += (output.rstrip() + '\n')
                text_container.code(complete_text, language='textile')  # Write output line by line (stream)
            if process.poll() is not None:  # Check if process finished
                break
        if process.returncode == 0:
            return None  # Successful execution
        else:
            return f"Error: {process.stderr.read().decode()}"  # Return error message
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"


def generate_prompt(text):
    text = text.lower() 

    prompt = f'''
Generate a ping or nmap command for the following task given in triple quotes, 
if the task is not possible with ping return command as 'Invalid task' and status code of 0, else 1
set all the flags based on the information provided. 
Don't use flags that require admin privileges if possibe. The command must be for windows. 
Return the command and status as json object. No comments or explanation. 

"""
{text} 
"""
    '''
    return prompt


def parse_response(response):
    text = response.text.replace("json", '').replace('```', '')
    obj = json.loads(text)
    
    return obj

