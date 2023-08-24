import streamlit as st
from google.oauth2 import id_token
from google.auth.transport import requests
import os
import asyncio
from authlib import *


st.sidebar.markdown("# google login")


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

# CLIENT_ID = "<your_google_client_id>"

def main():
    st.title("Login Page")
    st.write("printing trying now")
    st.write("printing trying now")

    st.write("Please log in with your Google account.")

    # Google login button
    if st.button("Login with Google"):
        
        #token = get_google_token()
        token = get_token()


        if token:
            # Validate the Google token and retrieve user information
            user_info = validate_google_token(token)
            if user_info:
                st.success("Logged in successfully!")
                st.write("User information:", user_info)
                # Redirect to the main app page or perform other actions


def get_google_token():
    """
    Retrieves the Google token using the Google Sign-In API.
    """
    # Implement the logic to retrieve the Google token
    # This can involve using the Google Sign-In API or an authentication library
    # Return the token if obtained successfully, None otherwise
    st.write("printing trying now , now")

    token = None
    
    # The implementation to obtain the token varies depending on your setup
    # Here's a basic example using the Google Sign-In API
    try:
        from google_signin import GoogleSignIn

        # Create an instance of GoogleSignIn with your client ID
        google_signin = GoogleSignIn(CLIENT_ID)

        # Call the `authenticate()` method to initiate the sign-in flow
        google_signin.authenticate()

        # Retrieve the token from the authenticated user
        token = google_signin.get_token()

    except ImportError:
        st.error("Failed to import the Google Sign-In library.")
    except Exception as e:
        st.error(f"Failed to obtain the Google token: {str(e)}")

    return token


def validate_google_token(token):
    try:
        # Verify the token using Google's API
        id_info = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
        if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Invalid token.')

        # Return user information
        return {
            'name': id_info['name'],
            'email': id_info['email'],
            'picture': id_info['picture']
        }
    except ValueError:
        st.error("Failed to validate the Google token.")
        return None

if __name__ == "__main__":
    main()
