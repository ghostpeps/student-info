import streamlit as st

def home():
  try:
    if is_logged_in == True:
      pass
  except NameError:
    st.title("Login")
    global is_logged_in
    global code
    code = st.text_input(label="Enter your login code:", placeholder="e.g. 0123456789")
    try:
      global f
      with open(f"t{code}.txt", "r") as f:
        pass
    except FileNotFoundError:
      st.markdown("Please enter a valid login code or sign up.")
      is_logged_in = False
    else:
      is_logged_in = True
    st.title("Sign Up")
    sign_up = st.button(label="Sign Up")
    if sign_up:
      with open("codes.txt", "r") as f:
        new_code = 0
        global c
        c = f.readline().strip()
        while c != "":
          if int(c) > new_code:
            new_code = c
          c = f.readline().strip()
        new_code += 1
      with open(f"{new_code}.txt", "x") as f:
        pass
      with open("codes.txt", "a") as f:
        f.write(f"{new_code}\n")
      is_logged_in = True
  else:
    
