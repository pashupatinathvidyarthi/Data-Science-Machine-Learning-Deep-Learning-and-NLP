import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache
def load_data():
    iris=load_iris()
    df=pd.DataFrame(iris.data,columns=iris.feature_names)
    df['species']=iris.target
    return df,iris.target_names

df,target_name=load_data()

model=RandomForestClassifier()
model.fit(df.iloc[:,:-1],df['species'])

st.slider.title("Input Features")
sepal_length=st.sidebar.slider("Sepal Length", float(df['sepal length (cm)'].min()),float)
sepal_width=st.sidebar.slider("Sepal Width", float(df['sepal width (cm)'].min()),float)
sepal_length=st.sidebar.slider("Sepal Length", float(df['sepal length (cm)'].min()),float)