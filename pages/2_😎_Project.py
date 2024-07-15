import streamlit as st

st.title("Projects")

# Ensure session state is initialized
if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

# Display the input value from session state
st.write("You have entered: ", st.session_state["my_input"])
