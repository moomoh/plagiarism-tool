import requests
import streamlit as st

# Define the API endpoint
auth_url = "https://accept.paymob.com/api/auth/tokens"

# Define your API key
#Your API Key"

##x
# Create the request payload


# Send the authentication request

def auth_token():
    api_key = "ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmpiR0Z6Y3lJNklrMWxjbU5vWVc1MElpd2ljSEp2Wm1sc1pWOXdheUk2T1RBeE1ESXlMQ0p1WVcxbElqb2lhVzVwZEdsaGJDSjkuZElnVGc5Nm9rYkpTUC13ZFBtMXdLY0tHZTJrRkI2U0ZkblhsTUN5TEEzcFNiR1drZy1JNlJfN3JheXM2NkJkOFhvQmZhb2E3eTA0ZDNJZ3hPSW1oUnc="
    payload = {
    "api_key": api_key 
    
              }
    response = requests.post(auth_url, json=payload)
    auth_token = response.json().get("token")
    st.write("Authentication Token:", auth_token)
    # print

    return auth_token


def order_id():
    order_url="https://accept.paymob.com/api/ecommerce/orders"
    auth_tokenx = auth_token()
#    auth_token=auth_token
    payload = {
        "auth_token": auth_tokenx,
    "delivery_needed": "false",
    "amount_cents": "10000",
    "currency": "EGP",
    "items": [],
        }
    response = requests.post(order_url, json=payload)
    order_id= response.json().get("id")
    st.write("Order id:", order_id)
    # print
    return order_id
    
    # auth
        # auth_token
# order_id(token)

def payment_key():
    payment_url="https://accept.paymob.com/api/acceptance/payment_keys"
    auth_tokenx = auth_token()
    order_idx ="151954915"
    
    #order_id()
    #order_id()
    email="claudette09@exa.com"
    first_name="Clifford"
    phone_number="+86(8)9135210487"
    last_name="Nicolas"
    payload = {
        "auth_token": auth_tokenx,
        "amount_cents": "10000",
        "expiration": "3600",
        "order_id": order_idx,

        "billing_data": {
            "apartment": "NA", 
            "email": email, 
            "floor": "NA", 
            "first_name": first_name, 
            "street": "NA", 
            "building": "NA", 
            "phone_number": phone_number, 
            "shipping_method": "NA", 
            "postal_code": "NA", 
            "city": "NA", 
            "country": "NA", 
            "last_name": last_name, 
            "state": "NA"
              },
        "currency": "EGP",
        "integration_id":"4227594",
        # kiosk id "4228625",
        # 4227594",
        "lock_order_when_paid": "false"
              }
    response = requests.post(payment_url, json=payload)
    payment_token= response.json().get("token")
    st.write("payment token:", payment_token)
  # print
    # order
    # id
    # Order id
    # order_id
    # order_id
    # order_id
    # order_id
    # 1

    return payment_token

# payment_key()

def wallet_pay():
    pay_url="https://accept.paymob.com/api/acceptance/payments/pay"
    payment_tokenx = payment_key()
    payload = {
        "source": {
    "identifier": "01010101010"
   # wallet mobile number", 
    "subtype": "WALLET"
  },
        "payment_token": payment_tokenx
                }
    response = requests.post(pay_url, json=payload)
    wallet_response= response.json().get("iframe_redirection_url")
    wallet_response1= response.json().get("pending")
    wallet_response2= response.json().get("success")
    # redirect_url
    # wallet_response= response.json()
    # iframe_redirection_url
    st.write("pending", wallet_response1,"success", wallet_response2)
    # redirect url :
    # print
    # "pending","success",

    return wallet_response

wallet_pay()

def kiosk_pay():
    pay_url="https://accept.paymob.com/api/acceptance/payments/pay"
    payment_tokenx = payment_key()
    payload = {
            "source": {
    "identifier": "AGGREGATOR", 
    "subtype": "AGGREGATOR"
              },
    "payment_token": payment_tokenx
                }
    response = requests.post(pay_url, json=payload)
    wallet_response= response.json().get("iframe_redirection_url")
    wallet_response= response.json()
    
    wallet_response3= response.json().get("data",{}).get("bill_reference")
    # bill_reference
    wallet_response1= response.json().get("pending")
    wallet_response2= response.json().get("success")
    print("pending", wallet_response1,"success", wallet_response2)
    print("bill reference" , wallet_response3)
    print("kiosk token :", wallet_response)
    
    return wallet_response

#kiosk_pay()
    # payment
 # 803
 # token
  # 42
        # Ethan Land
        # 8028
        # PKG
        # 01898
        # Jaskolskiburgh
        # CR
        # Utah

# Check if the request was successful
# if response.status_code == 200:
    # Extract the authentication token from the response
  #  token = response.json().get("token")

    # Display the authentication token in your Streamlit app
   # print("Authentication Token:", token)
    # st.write
#else:
    # Display an error message if the request failed
#    print("Authentication request failed. Please check your API key.")
    #st.error

# Continue with the rest of your Streamlit app
# ...
