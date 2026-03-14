import streamlit as st
import pandas as pd
import numpy as np


##Title of the application
st.title("Hello Streamlit")


##Display a simple text
st.write("This is a simple text")


## Create a simple DataFrame
df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

