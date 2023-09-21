import streamlit as st
import requests

query_params = st.experimental_get_query_params()
query_dict = vars(query_params)
                  # {
                  # }
st.write(query_params)
st.write(query_dict)
