import streamlit as st
import requests

st.title("ITA AI Chatbot")

question = st.text_input("Ask ITA AI a question:")

if st.button("Ask"):
    response = requests.post("https://your-backend-url/ask", json={"question": question})
    st.write("Response:", response.json().get("answer", "No response"))
