# Import required libraries
import os
from dotenv import load_dotenv
from itertools import zip_longest

import streamlit as st
from streamlit_chat import message

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
import streamlit as st
from google.oauth2 import id_token
from google.auth.transport import requests

# Define your Google OAuth credentials
# YOUR_CLIENT_ID
CLIENT_ID = '583040091662-i7o8d2td7nb31p9h135nep4l2nddgq4q.apps.googleusercontent.com'

# Create a login button
def login():
    st.title("Login with Google")
    login_button = st.button("Login")

    if login_button:
        # Request user authentication
        auth_code = st.experimental_get_query_params().get('code', None)
        if auth_code:
            try:
                # Exchange the authorization code for an access token
                token = id_token.fetch_id_token(requests.Request(), CLIENT_ID, auth_code)
                # Validate the token and extract user information
                # You can use `token` to authenticate the user and store session state
                st.write("Login successful!")
            except ValueError as e:
                st.error("Authentication failed. Please try again.")
        else:
            # Redirect the user to the Google Sign-In page
            auth_url = f"https://accounts.google.com/o/oauth2/auth?client_id={CLIENT_ID}&response_type=code&scope=openid%20email&redirect_uri={st.experimental_get_url()}&access_type=offline"
            st.experimental_set_query_params(code="")
            st.experimental_rerun()
            st.experimental_redirect(auth_url)

# Main app logic
def main():
    login()

if __name__ == "__main__":
    main()

# Load environment variables
# load_dotenv()
load_dotenv('openai.env')
api_key = os.getenv('OPENAI_API_KEY')

# Set streamlit page configuration
st.set_page_config(page_title="ChatBot Starter")
st.title("ChatBot Starter")

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
