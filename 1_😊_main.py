import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Multiple Pages App",
    page_icon=":memo:"
)

# Main page title
st.title("Main Page")
st.sidebar.success("Select a page to view")

# Initialize session state if not already done
if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

# Text input field
my_input = st.text_input("Input a text here...", st.session_state["my_input"])

# Submit button
submit = st.button("Submit")

if submit:
    st.session_state["my_input"] = my_input
    st.balloons()
    st.success("Form submitted!")

# Display the input value from session state
st.write("You have entered: ", st.session_state["my_input"])
