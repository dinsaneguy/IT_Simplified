import streamlit as st

def home_page():
    # k ho
    st.header("What is Med_Guardian?")
    st.write("""
    **Med_Guardian** is a cutting-edge platform designed to assist you in understanding and managing your health. Our tool uses advanced prediction models to analyze various health indicators and provide insights into potential health conditions.
    """)

    # kaise kaam karta
    st.header("How It Works")
    st.write("""
    **Predictive Analysis:** 
    Enter your health data or upload a report to receive predictive insights. Please note that these predictions are not medical diagnoses but are intended to provide preliminary information based on the data provided.

    **Consult Professionals:** 
    If the predictions suggest a possible health concern, we strongly recommend consulting a healthcare professional. You can use our website to find and contact physicians or visit the nearest hospital for a thorough evaluation.
    """)

    # Features
    st.header("Features")
    st.write("""
    - **User-Friendly Interface:** Easy to navigate and interact with, whether you're uploading data or manually entering information.
    - **Comprehensive Analysis:** Gain insights into potential health risks based on your input.
    - **Professional Guidance:** Follow-up with medical experts through our platform or at a nearby healthcare facility.
    """)

    # Conclusion
    st.write("""
    At **Med_Guardian**, your health and well-being are our top priorities. While our tool provides valuable predictive insights, it is not a substitute for professional medical advice. Always seek the guidance of qualified healthcare providers for any health-related concerns.

    Thank you for choosing Med_Guardian. We are committed to helping you stay informed and proactive about your health.
    """)
