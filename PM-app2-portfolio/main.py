import streamlit as st

st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("August Trillanes")
    content = """
    I'm a aspiring Python developer and DevOps engineer, a life-long tinkerer
    and learner, I also practice Aikido regularly at a local dojo. Currently
    working for a Fortune 500 company."""
    st.info(content)

#st.subheader("Below you will find my other projects, feel free to contact me.")
content = """
Below you will find my other projects, feel free to contact me."""
st.write(content)