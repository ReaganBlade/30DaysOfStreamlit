import streamlit as st
import pandas as pd
import numpy as np

st.header('Line Chart')
st.subheader('This is a line chart example by 30 Days of Streamlit')

# no of data points
data = st.slider("Select Number of Data Points: ", 5, 100, 20)

# streamlit line_chart
chart_data = pd.DataFrame(
    np.random.randn(data, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)