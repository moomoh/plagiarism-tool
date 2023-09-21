import streamlit as st
import requests

query_params = st.experimental_get_query_params()
query_dict = dict(query_params)
id= query_dict.get("id")
order_status= query_dict.get("success")
amount = query_dict.get("amount_cents")
integration_id=query_dict.get("integration_id")
order_id= query_dict.get("order") 
mobile_no = query_dict.get("source_data.pan")
payment_source = query_dict.get("source_data.type")
hmac= query_dict.get("hmac")


                  # {
                  # }
st.write("order id is :", order_id)
st.write("order status", order_status)
st.write("mobile no :", mobile_no)
#st.write(query_params)
st.write(query_dict)
