import streamlit as st
import requests

import hashlib
import hmac

from st_supabase_connection import SupabaseConnection

# Initialize connection.
def database_build():
  
  conn = st.experimental_connection("supabase",type=SupabaseConnection)
  for key, values in query_dict.items():
    column_name = key.replace(".", "_")  # Replacing dot with underscore in column name
    column_values = values[0]  # Assuming there's only one value for each key
    if isinstance(column_values, str):
        column_values = f"'{column_values}'"  # Enclose string values in single quotes
    if key== 'order':
      column_name= 'order_id'
# key
    query = f"INSERT INTO transactions ({column_name}) VALUES ({column_values});"
    cursor.execute(query)

# Commit the changes and close the connection
  conn.commit()
  cursor.close()
  conn.close()
  st.write("database update successful")
#B

# data

query_params = st.experimental_get_query_params()
query_dict = dict(query_params)
id= query_dict.get("id")
order_status= query_dict.get("success")
amount = query_dict.get("amount_cents")
integration_id=query_dict.get("integration_id")
order_id= query_dict.get("order") 
mobile_no = query_dict.get("source_data.pan")
payment_source = query_dict.get("source_data.type")
callback_hmac= query_dict.get("hmac")
callback_hmac= callback_hmac[0]
integration_id=query_dict.get("integration_id")
source_data_subtype=query_dict.get("source_data.sub_type")
txn_response_code=query_dict.get("txn_response_code")
#.replace("'", "")
# 1
# .get("
# ")

#
# # c

# _x


# allback_hmac= query_dict["hmac"]
                  # {
                  # }



hmac_secret = 'DE0AD1C62DEFC4DEE781FDD907FDD69F'

def concatenate_selected_values(query_dict):
    selected_keys = [
        "amount_cents", "created_at", "currency", "error_occured", "has_parent_transaction",
        "id", "integration_id", "is_3d_secure", "is_auth", "is_capture", "is_refunded",
        "is_standalone_payment", "is_voided", "order", "owner", "pending",
        "source_data.pan", "source_data.sub_type", "source_data.type", "success"
    ]
    #for key in selected_keys:
      #st.write(key,query_dict[key])
    concatenated_string = ''.join([str(query_dict[key])[1:-1].replace("'", "") for key in selected_keys if key in query_dict])
    return concatenated_string


# 
#3
# .id

concatenated_dict_values = concatenate_selected_values(query_dict)
# result
st.write(concatenated_dict_values)
#print(result)

database_build()

def calculate_hmac(concatenated_string, hmac_secret):
    hmac_digest = hmac.new(hmac_secret.encode(), concatenated_string.encode(), hashlib.sha512).hexdigest()
    st.write("the resulted hmac is ", hmac_digest)
    st.write("the callback hmac is ",callback_hmac)
    return hmac_digest.lower()

def compare_hmac ():
    calculated_hmac=calculate_hmac(concatenated_dict_values,hmac_secret)
    if calculated_hmac == callback_hmac :
        return True
    else:
        return False

# [1:-1]


#[1:-1]
# ,
    
hmac_result= compare_hmac()
st.write("The result of hmac comparison is :", hmac_result)
st.write("order id is :", order_id)
st.write("order status", order_status)
st.write("mobile no :", mobile_no)
st.write("integration id :", integration_id)
# "
#st.write(query_params)
st.write(query_dict)
