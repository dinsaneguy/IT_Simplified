import streamlit as st

def feedback():
    # check garne ho feedback
    if 'feedback_text' not in st.session_state:
        st.session_state.feedback_text = ''
#inputing feedback
    feedback_text = st.text_area(
        "Give your Feedback to our Webapp",
        value=st.session_state.feedback_text,
        height=400,
        max_chars=400
    )

    # submitbtn
    if st.button("Submit Feedback"):
        #session update
        st.session_state.feedback_text = feedback_text
        # Clear the text area
        st.session_state.feedback_text = ''
        st.success("Feedback submitted successfully!")
