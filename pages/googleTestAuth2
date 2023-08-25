import streamlit as st
from google.oauth2 import id_token
from google.auth.transport import requests
from google_auth_oauthlib.flow import Flow

CLIENT_ID = '583040091662-i7o8d2td7nb31p9h135nep4l2nddgq4q.apps.googleusercontent.com'
#CLIENT_ID = "<your-client-id>"

def get_google_signin_url():
    flow = Flow.from_client_secrets_file(
        "client_secrets.json",
        scopes=["openid", "email"],
        redirect_uri="urn:ietf:wg:oauth:2.0:oob"
    )
    authorization_url, _ = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true"
    )
    return authorization_url

def login_page():
    # Login form
    st.subheader("Login with Google")
    google_url = get_google_signin_url()
    login_button = st.button("Login with Google")

    # Perform authentication
    if login_button:
        flow = Flow.from_client_secrets_file(
            "client_secrets.json",
            scopes=["openid", "email"],
            redirect_uri="urn:ietf:wg:oauth:2.0:oob"
        )
        authorization_url, _ = flow.authorization_url(
            access_type="offline",
            include_granted_scopes="true"
        )
        st.markdown(f'<a href="{authorization_url}" target="_blank">Sign in with Google</a>', unsafe_allow_html=True)
        st.warning("After signing in, copy the authorization code and paste it below.")

        auth_code = st.text_input("Authorization Code")
        submit_button = st.button("Submit")

        if submit_button:
            flow.fetch_token(code=auth_code)
            id_info = id_token.verify_oauth2_token(flow.credentials.id_token, requests.Request(), CLIENT_ID)
            if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Invalid issuer.')
            state.logged_in = True
            st.experimental_set_query_params(logged_in=True)
            st.success("Login successful!")

    return state.logged_in

# Remaining code and functions...
