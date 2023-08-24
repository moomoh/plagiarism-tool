import streamlit as st
from streamlit import session_state as state

def login_page():
    # Login form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

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

# Main app
def main():
    st.title("My App")
    
    # Check if user is logged in
    if not state.logged_in:
        login_successful = login_page()
        if not login_successful:
            return

    # Display app content
    st.write("Welcome to the app!")
    st.button("Logout", on_click=logout)
    # ... Rest of your app code ...

if __name__ == "__main__":
    state.logged_in = False
    if "logged_in" in st.experimental_get_query_params():
        state.logged_in = True
    main()
