import streamlit as st

def home():
  global is_logged_in
  def integer(x: int):
    if x is "":
      x = 0
    else:
      x = int(x)
    return x
  @st.dialog("Your login code")
  def number(new_code: int):
    st.write(f"Copy or save the bellow code so you can paste it when login. You can also find this code in the settings tab.\n{new_code}")
    if st.button(label="close"):
      st.rerun()
  try:
    if is_logged_in == True:
      pass
  except NameError:
    st.title("Login")
    global new_code
    code = st.text_input(label="Enter your login code:", placeholder="e.g. 0123456789")
    login = st.button(label="Login")
    if login:
      try:
        global f
        with open(f"{code}.txt", "r") as f:
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
        new_code = integer(f.readline().strip()) + 1
      with open(f"{new_code}.txt", "x") as f:
        pass
      with open("codes.txt", "w") as f:
        f.write(f"{new_code}")
      number(new_code)
      is_logged_in = True
  else:
    pass
pages = [
  st.Page(page=home(), title="Home", icon=":material/home:"),
  st.Page(page="settings.py", title="Settings", icon=":material/settings:")
]
