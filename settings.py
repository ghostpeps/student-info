import streamlit as st

from home import new_code, is_logged_in

import os

@st.dialog("Are you sure?")
def delete(new_code: int):
  col1, col2 = st.columns(2)
  st.write("By deleting your account, your login code and your students along with their data, gets deleted.")
  with col1:
    cancel = st.button(label="Cancel", icon=":material/cancel:")
  with col2:
    delete_for_real = st.button(label="Delete", type="Primary", icon=":material/delete:")
    if delete_for_real:
      with open("codes.txt", "w") as f:
        if int(f.readline().strip()) == new_code:
          f.write("0")
      os.remove(f"{new_code}.csv")

if is_logged_in == True:
  st.title("Settings")
  st.write(f"Your login code is {new_code}.")
  delete = st.button(label="Delete Account", type="Primary", icon=":material/delete:")
  if delete:
    delete(new_code)
elif is_logged_in == False:
  st.title("Please login or sign up first.")
