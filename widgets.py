import streamlit as st
import pandas as pd
st.title("Streamlit Text input")

name = st.text_input("Enter your name:")



age = st.slider("Select your age:", 0,100,25)

st.write(f"Your age is {age}.")

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"You selected {choice}.")

if name:
    st.write(f"Hello, {name}")

data = {
        "Name":["John", "Jane", "Jake", "Jill"],
        "Age":[28,24,26,28],
        "City": ["Ny", "LA", "Ch", "Tx"]
}

df = pd.DataFrame(data)
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV File", type="csv")

if uploaded_file is not None:
 df= pd.read_csv(uploaded_file)
 st.write(df)