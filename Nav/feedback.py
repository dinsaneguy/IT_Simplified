import streamlit as st

def feedback():
    # check garne ho feedback
    if 'feedback_text' not in st.session_state:
        st.session_state.feedback_text = ''
#inputing feedback
    feedback_text = st.text_area(
        "Give your Feedback to our Webapp",
        value=st.session_state.feedback_text,
        height=300,
        max_chars=400
    )

    tog=st.toggle("Did our prediction worked?",value=1)
    if(tog):
        st.write("Yes")
    else:
        st.write("No!")
        
    if st.button("Submit Feedback"):
        #session update
        st.session_state.feedback_text = feedback_text
        # Clear the text area
        st.session_state.feedback_text = ''
        st.success("Feedback submitted successfully!")
