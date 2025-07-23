import streamlit as st

from home import new_code, is_logged_in

if is_logged_in == True:
  st.title("Settings")
  st.write(f"Your login code is {new_code}.")
elif is_logged_in == False:
  st.title("Please login or sign up first.")
