import streamlit as st

st.title("Welcome to ITA AI")
st.write("Ask your questions below:")

user_input = st.text_input("Your question:")
if user_input:
    st.write(f"Question: {user_input}")
