# Day8: Select Slider Example
import streamlit as st
from datetime import time, datetime

# Header
st.header("Select Slider Example")
# Sub-header
st.subheader("Slider")

# Example 1
age = st.slider('Select Your age: ', 0, 130, 25)
st.write(f"You are {age} years old!")

# Example 2
st.subheader('Range Slider')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

st.write(f"Values: {values}")

# Example 3
st.subheader('Range time slider')
appointment = st.slider(
    "Schedule your appointment: ",
    value=(time(11, 30), time(12, 45))
)

st.write(f"You're Scheduled for: {appointment}")

# Example 4

st.subheader('DateTime Slider')
start_time = st.slider(
    "When do you start?",
    value = datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm"
)

st.write(f"Start time: {start_time}")

