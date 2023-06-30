import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
  todo = st.session_state['new_todo'] + '\n'
  todos.append(todo)
  functions.write_todos(todos)

todos = functions.get_todos()

st.title("My Todo WebApp")
st.subheader("Subheader")
st.write("Write Text")

for index, todo_item in enumerate(todos):
  checkbox = st.checkbox(todo_item, key=todo_item)
  if checkbox:
    todos.pop(index)
    functions.write_todos(todos)
    del st.session_state[todo_item]
    st.experimental_rerun()

st.text_input(label='', placeholder='Enter a todo item',
              on_change=add_todo, key='new_todo')
