# Import required libraries
import os
from dotenv import load_dotenv
from itertools import zip_longest
import streamlit.components.v1 as components

import streamlit as st
from streamlit_chat import message

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

from google.oauth2 import id_token
from google.auth.transport import requests
from google.oauth2 import id_token
#from google.auth.transport import requests
from google_auth_oauthlib.flow import Flow
from httpx_oauth.clients.google import GoogleOAuth2
import asyncio
from auth import *



# Set streamlit page configuration
st.set_page_config(page_title="ChatBot Starter")
st.title("ChatBot Starter")




CLIENT_ID = '583040091662-i7o8d2td7nb31p9h135nep4l2nddgq4q.apps.googleusercontent.com'  # Replace with your actual client ID
# 583040091662-i7o8d2td7nb31p9h135nep4l2nddgq4q.apps.googleusercontent.com
CLIENT_SECRET='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'
#"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"
url='https://plagiarism.streamlit.app'

client_id = CLIENT_ID
# os.environ['GOOGLE_CLIENT_ID']
client_secret = CLIENT_SECRET
# os.environ['GOOGLE_CLIENT_SECRET']
redirect_uri = url
#os.environ['REDIRECT_URI']

def login_page():
    # Login form
    st.subheader("Login with Google")
    token=get_token()
    #token = st.text_input("ID Token")
    login_button = st.button("Login")

    # Perform authentication
    if login_button:
        try:
            id_info = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
            if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Invalid issuer.')
            state.logged_in = True
            st.experimental_set_query_params(logged_in=True)
            st.success("Login successful!")
        except ValueError as e:
            st.error("Login failed. Please try again.")

    return state.logged_in



if __name__ == '__main__':
    #google_loginTest()
    
    # st.title("Streamlit Oauth Login")
    st.write(get_login_str(), unsafe_allow_html=True)
    
        
    if st.button("display user"):  
        display_user()

    login_page()

load_dotenv('openai.env')
api_key = os.getenv('OPENAI_API_KEY')



# Initialize session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []  # Store AI generated responses

if 'past' not in st.session_state:
    st.session_state['past'] = []  # Store past user inputs

if 'entered_prompt' not in st.session_state:
    st.session_state['entered_prompt'] = ""  # Store the latest user input

# Initialize the ChatOpenAI model
# openai_api_key="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",

chat = ChatOpenAI(
    openai_api_key=api_key,
    temperature=0.5,
    model_name="gpt-3.5-turbo"
)


def build_message_list():
    """
    Build a list of messages including system, human and AI messages.
    """
    # Start zipped_messages with the SystemMessage
    zipped_messages = [SystemMessage(
        content="You are a helpful AI assistant talking with a human. If you do not know an answer, just say 'I don't know', do not make up an answer.")]

    # Zip together the past and generated messages
    for human_msg, ai_msg in zip_longest(st.session_state['past'], st.session_state['generated']):
        if human_msg is not None:
            zipped_messages.append(HumanMessage(
                content=human_msg))  # Add user messages
        if ai_msg is not None:
            zipped_messages.append(
                AIMessage(content=ai_msg))  # Add AI messages

    return zipped_messages


def generate_response():
    """
    Generate AI response using the ChatOpenAI model.
    """
    # Build the list of messages
    zipped_messages = build_message_list()

    # Generate response using the chat model
    ai_response = chat(zipped_messages)

    return ai_response.content


# Define function to submit user input
def submit():
    # Set entered_prompt to the current value of prompt_input
    st.session_state.entered_prompt = st.session_state.prompt_input
    # Clear prompt_input
    st.session_state.prompt_input = ""


# Create a text input for user
st.text_input('YOU: ', key='prompt_input', on_change=submit)


if st.session_state.entered_prompt != "":
    # Get user query
    user_query = st.session_state.entered_prompt

    # Append user query to past queries
    st.session_state.past.append(user_query)

    # Generate response
    output = generate_response()

    # Append AI response to generated responses
    st.session_state.generated.append(output)

# Display the chat history
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        # Display AI response
        message(st.session_state["generated"][i], key=str(i))
        # Display user message
        message(st.session_state['past'][i],
                is_user=True, key=str(i) + '_user')


# Add credit
st.markdown("""
---
Made with 🤖 by [Austin Johnson](https://github.com/AustonianAI)""")
