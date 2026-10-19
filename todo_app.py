import streamlit as st

st.title("📝 Smart To-Do List App")

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

new_task = st.text_input("Add a new task:")
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success(f"Added task: {new_task}")
    else:
        st.warning("Please enter a task.")

st.subheader("Your Tasks:")
if st.session_state.tasks:
    for index, task in enumerate(st.session_state.tasks):
        st.write(f"{index + 1}. {task}")
    
    if st.button("Clear All Tasks"):
        st.session_state.tasks = []
        st.experimental_rerun()
else:
    st.info("No tasks added yet.")
