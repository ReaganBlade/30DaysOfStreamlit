# Example to use st.write in streamlit
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('Example for st.write');

# Example 1
st.write("Hello, *World!* : sun glasses");

# example 2 for int
st.write(1234)

# example 3 for dataframe
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })

st.write(df)

# Example 4
# When using a block element like a dataframe, all of the other outputs are shown in another line

st.write("Below is a DataFrame: ", df, 'Above is a dataframe');


# Example 5
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df2).mark_circle().encode(
    x = 'a', y = 'b', size = 'c', color = 'c', tooltip = ['a', 'b', 'c']
)

st.write(c)