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

    st.toggle("Experience",value="Good",on_change="Bad")

    labels = ["Worked", "Didn't Work"]
    values = {label: i for i, label in enumerate(labels)}

# Create a slider with numerical values
    selected_value = st.slider("How are you?", min_value=0, max_value=len(labels)-1, step=1)
    st.write(labels[selected_value])
    # submitbtn
    if st.button("Submit Feedback"):
        #session update
        st.session_state.feedback_text = feedback_text
        # Clear the text area
        st.session_state.feedback_text = ''
        st.success("Feedback submitted successfully!")
