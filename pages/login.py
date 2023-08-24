import streamlit as st
import asyncio
from auth import *

# st.markdown("# login")
st.sidebar.markdown("# login")
# import streamlit as st

"""
if __name__ == '__main__':
    # st.title("Streamlit Oauth Login")
    st.write(get_login_str(), unsafe_allow_html=True)
        
    if st.button("display user"):  
        display_user()
"""

def main():
    st.title("Login Page")
    st.write("Please enter your credentials to log in.")

    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Login"):
        # Validate user credentials
        if validate_credentials(username, password):
            st.success("Logged in successfully!")
            # Redirect to the main app page or perform other actions
        else:
            st.error("Invalid username or password. Please try again.")

    # Login with Google button
    st.write("Or login with Google:")
    st.write(get_login_str(), unsafe_allow_html=True)
    if st.button("display user"):  
        display_user()
    if st.button("Login with Google"):
        st.write("login success")
        # Implement the logic to authenticate with Google
        # This can involve using the Google Sign-In API or an authentication library
        # Once authenticated, you can redirect the user to the main app page or perform other actions

def validate_credentials(username, password):
    # Implement your logic to validate the user credentials here
    # This can involve checking against a user database or any other authentication method
    # Return True if the credentials are valid, False otherwise
    return True

if __name__ == "__main__":
    main()
