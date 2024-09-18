import streamlit as st

st.title("hej första gången streamlit")
st.header("hej!")
st.subheader("programmera med streamlit")

import streamlit as st

if st.button("tryck här"):
    st.write("skriv ett namn")

import streamlit as st

namn = st.text_input("Vad heter du?")
if namn:
    st.write(f"Hej, {namn}! Välkommen till Streamlit.")
