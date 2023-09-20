import requests
import streamlit as st

# Define the API endpoint
auth_url = "https://accept.paymob.com/api/auth/tokens"

# Define your API key
api_key = "ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmpiR0Z6Y3lJNklrMWxjbU5vWVc1MElpd2ljSEp2Wm1sc1pWOXdheUk2T1RBeE1ESXlMQ0p1WVcxbElqb2lhVzVwZEdsaGJDSjkuZElnVGc5Nm9rYkpTUC13ZFBtMXdLY0tHZTJrRkI2U0ZkblhsTUN5TEEzcFNiR1drZy1JNlJfN3JheXM2NkJkOFhvQmZhb2E3eTA0ZDNJZ3hPSW1oUnc="
## Your API Key"

# Create the request payload
payload = {
    "api_key": api_key
}

# Send the authentication request
response = requests.post(auth_url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Extract the authentication token from the response
    token = response.json().get("token")

    # Display the authentication token in your Streamlit app
    st.write("Authentication Token:", token)
else:
    # Display an error message if the request failed
    st.error("Authentication request failed. Please check your API key.")

# Continue with the rest of your Streamlit app
# ...
