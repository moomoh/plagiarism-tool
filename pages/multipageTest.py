import streamlit as st
import streamlit.components.v1 as components
from streamlit import session_state as state
from auth import *

def login_page():
    # Login form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")
    st.markdown(get_login_str(), unsafe_allow_html=True)
    
    # Perform authentication
    if login_button:
        if username == "admin" and password == "password":
            state.logged_in = True
            st.experimental_set_query_params(logged_in=True)
            st.success("Login successful!")
    
    return state.logged_in

def logout():
    state.logged_in = False
    st.experimental_set_query_params()

def home_page():
    st.write("Welcome to the Home Page!")
    # ... Add content for the home page ...

def profile_page():
    st.write("Welcome to the Profile Page!")
    # ... Add content for the profile page ...

def settings_page():
    st.write("Welcome to the Settings Page!")
    # ... Add content for the settings page ...

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
