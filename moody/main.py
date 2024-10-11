import os
import openai 
import mykey
import streamlit as st
st.title('Aman app for message generator')

#user_input1 = st.text_input('please enter your first ingredient')
#user_input2 = st.text_input('please enter your second ingredient')

option1 = st.selectbox(
    'Please enter your relation',
    ('Mother', 'Father', 'Sibling', 'Boss', 'Wife'))

option2 = st.selectbox(
    'Please select your context',
    ('Thank you', 'Plan Holiday', 'Apology', 'Applying leave'))

OPENAI_API_KEY = mykey.OPENAI_API_KEY
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

from openai import OpenAI
client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

prompt = "Write a message to my " + option1 + "about " + user_input2
response = client.completions.create(model = "gpt- 3.5- turbo-instruct", 
                                     prompt =prompt, max_tokens = 3000, temperature=0.4)

generated_text = response.choices[0].text
#print(generated_text)
st.write(generated_text)



