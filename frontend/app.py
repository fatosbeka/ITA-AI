import streamlit as st
import requests  # Import requests to call the backend API

# Define the backend API URL (Replace with your Railway backend URL)
BACKEND_URL = "https://romantic-sparkle-production-5f52.up.railway.app"

st.title("Welcome to ITA AI")
st.write("Ask your questions below:")

user_input = st.text_input("Your question:")

if user_input:
    # Send the user input to the backend API
    response = requests.get(f"{BACKEND_URL}", params={"question": user_input})
    
    if response.status_code == 200:
        # Display the response from backend
        st.write(f"Backend Response: {response.text}")
    else:
        st.write("Error: Could not fetch response from backend")
