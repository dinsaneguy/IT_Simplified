import streamlit as st
from streamlit_option_menu import option_menu as opt
from Nav.home import home_page
from Nav.hospitals import hospital
from Nav.GetMeds import getmeds
from Nav.Consult import consult
from Nav.feedback import feedback


def nav():
    css_file_path = 'C:/Med_Guardian/Nav/nav.css'
    # Correct path to the CSS file and syntax for reading it

    # Read CSS from file and apply it
    with open(css_file_path, 'r') as css_file:
        css = css_file.read()
        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

    # Create the option menu with desired settings
    select_nav = opt(
        menu_title="",  # No menu title
        options=["Home","Hospitals", "GetMeds", "Consult", "Feedback"],
        default_index=0,  # Default selection
        orientation="horizontal",  # Horizontal orientation
    )

    if(select_nav=="Home"):
        home_page()
    if select_nav == "Hospitals":
        hospital()
    elif select_nav == "GetMeds":
        getmeds()
    elif select_nav == "Consult":
        consult()
    elif select_nav == "Feedback":
        feedback()
