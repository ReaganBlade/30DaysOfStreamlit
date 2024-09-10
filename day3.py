import streamlit as st

st.button("Reset", type='primary')

if st.button("Greet", type='secondary'):
    st.write("Hello World!")
else:
    st.write("Bye World!")