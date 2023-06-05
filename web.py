import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    # st.session_state is a dictionary type which is used to
    # append new items in the todos

    functions.write_todos(todos)
    # calls the write_todos from function.py which edits the new_todo

# steps to create web page


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your <b>productivity</b>.",
         unsafe_allow_html=True)

# creates checkboxes for todos list
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# to create new input box
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

