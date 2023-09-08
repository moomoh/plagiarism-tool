# "بسم الله الرحمن الرحيم"
# "وفوق كل ذي علم عليم"
# Import required libraries
import os
from dotenv import load_dotenv
from itertools import zip_longest
import streamlit.components.v1 as components
from streamlit import session_state as state

import streamlit as st



import asyncio
from auth import *



# Set streamlit page configuration
st.set_page_config(page_title="ChatBot Starter")
#st.title("ChatBot Starter")




def login_page():
    # Login form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")
    login_page_google()
    #st.write(get_login_str(), unsafe_allow_html=True)
    
        
    #if st.button("display user"):  
      #  display_user()

    # Perform authentication
    if login_button:
        if username == "admin" and password == "password":
            #state.logged_in =
            state["logged_in"] =True
            st.experimental_set_query_params(logged_in=True)
            st.success("Login successful!")
            st.experimental_rerun()
            
            #login_placeholder.empty()
           # home_page()
    return state.logged_in

def login_page_google():
    glogin_button = st.button("Login")
    auth_code = get_code()
    if auth_code is not None:
        state.logged_in = True
        st.experimental_set_query_params(logged_in=True)
        st.success("Login successful!")
    return state.logged_in


def logout():
    #state["logged_in"] = False
    #st.experimental_set_query_params(logged_in=False)
    #login_placeholder.empty()
    state.logged_in = False
    st.experimental_set_query_params()

def home_page():
    st.write("Welcome to the Home Page!")
    st.write("And happy journey!")
    import chatbot
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
    
    st.write("بسم الله الرحمن الرحيم")
    st.title("My App")

    #Check if user is logged in
    if not state.logged_in:
        login_successful = login_page()
        if not login_successful:
            return
        #st.empty()
        #login_placeholder.empty()
    else :
        st.write("You are already logged in.")


#def main():
#    state = st.session_state.get("state", {})
#    if not state.get("logged_in", False):
#        login_successful = login_page()
#        if not login_successful:
#            return
        #login_placeholder.empty()
#        state["logged_in"] = True
#        st.session_state["state"] = state
#    else:
#        st.write("You are already logged in.")


    #home_page()

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
    # "بسم الله الرحمن الرحيم"
    #
    state.logged_in = False
    if "logged_in" in st.experimental_get_query_params():
        state.logged_in = True
   # state.setdefault("logged_in", False)
   # if "logged_in" in st.experimental_get_query_params():
   #     state["logged_in"] = True
    login_placeholder = st.empty()
    main()










#if __name__ == '__main__':
 #   main()
#    state.logged_in = False
#    if "logged_in" in st.experimental_get_query_params():
#        state.logged_in = True
    #google_loginTest()
    
    # st.title("Streamlit Oauth Login")
 #   st.write(get_login_str(), unsafe_allow_html=True)
    
        
#    if st.button("display user"):  
#        display_user()

 #   login_page()

