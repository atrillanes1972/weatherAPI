import streamlit as st
import pandas as pd


content="""
Theres some latin description here on the company catalog below, and then the 
site is supposed to display probably the top level executives, and their short
bios along some function, they do for the company."""

st.title("The Best company")
st.write(content)
st.subheader("Our team")

df = pd.read_csv("data.csv")
col1, empty_col1,col2,empty_col2,col3 = st.columns([1.5,0.5,1.5,0.5,1.5])

with col1:
    for index,row in df[:4].iterrows():
        st.header(row["first name"] + " " + row["last name"])
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index,row in df[4:8].iterrows():
        st.header(row["first name"] + " " + row["last name"])
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index,row in df[8:12].iterrows():
        st.header(row["first name"] + " " + row["last name"])
        st.write(row["role"])
        st.image("images/" + row["image"])


