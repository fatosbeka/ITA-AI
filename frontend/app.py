import streamlit as st
import requests

BACKEND_URL = "https://romantic-sparkle-production-5f52.up.railway.app"

st.title("Welcome to ITA AI")
st.write("Ask your questions below:")

user_input = st.text_input("Your question:")
if user_input:
    response = requests.get(f"{BACKEND_URL}", params={"question": user_input})
    if response.status_code == 200:
        st.write(f"Backend Response: {response.text}")
    else:
        st.write("Error: Could not fetch response from backend")
