
def generate_prompt(text):
    text = text.lower() 

    prompt = f'''
Generate a ping command for the following task given in triple quotes, if the task is not possible with ping return 'Unable to Generate Command' text, set all the flags based on the information provided. Don't use flags that require admin privileges if possibe. Return the command no comments or explanation. 

"""
{text} 
"""
    '''

    return prompt

