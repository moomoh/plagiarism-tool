import streamlit as st
from google.oauth2 import id_token
from google.auth.transport import requests
from streamlit import session_state as state
from google_auth_oauthlib.flow import Flow
import os

#CLIENT_ID = "<your-client-id>"
CLIENT_ID = '583040091662-i7o8d2td7nb31p9h135nep4l2nddgq4q.apps.googleusercontent.com'

def get_google_signin_url():
    flow = Flow.from_client_secrets_file(
        "client_secrets.json",
        scopes=["openid", "email"],
        redirect_uri="urn:ietf:wg:oauth:2.0:oob"
    )
    auth_url, _ = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true"
    )
    return auth_url

def login_page():
    # Login form
    st.subheader("Login with Google")
    google_url = get_google_signin_url()
    code = st.text_input("Authorization Code")
    login_button = st.button("Login")

    # Perform authentication
    if login_button:
        flow = Flow.from_client_secrets_file(
            "client_secrets.json",
            scopes=["openid", "email"],
            redirect_uri="urn:ietf:wg:oauth:2.0:oob"
        )
        flow.fetch_token(code=code)
        id_info = id_token.verify_oauth2_token(flow.credentials.id_token, requests.Request(), CLIENT_ID)
        if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Invalid issuer.')
        state.logged_in = True
        st.experimental_set_query_params(logged_in=True)
        st.success("Login successful!")

    return state.logged_in

def logout():
    state.logged_in = False
    st.experimental_set_query_params()

# Decorator for protecting pages
def protected_page(func):
    def wrapper():
        if not state.logged_in:
            st.warning("Please log in to access this page.")
            login_page()
        else:
            func()
    return wrapper

# Main app
def main():
    st.title("My App")

    # Check if user is logged in
    if not state.logged_in:
        login_successful = login_page()
        if not login_successful:
            return

    # Create side menu
    pages = {
        "Home": home_page,
        "Profile": profile_page,
        "Settings": settings_page
    }
    selected_page = st.sidebar.radio("Menu", list(pages.keys()))

    # Display selected page
    pages[selected_page]()
    
    # Logout button
    st.sidebar.button("Logout", on_click=logout)

if __name__ == "__main__":
    state.logged_in = False
    if "logged_in" in st.experimental_get_query_params():
        state.logged_in = True
    main()
