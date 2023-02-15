import streamlit as st
import functions


todos = functions.get_todos()
def add_todo():
    todo = st.session_state["newtodo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my to-do app!")
st.write("This is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="newtodo")

st.session_state