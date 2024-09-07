import pickle
import streamlit as st
from streamlit_option_menu import option_menu as opt

diabetes_model = pickle.load(
    open('C:\Med_Guardian\Diabetes.sav', 'rb'))
# heart_model = pickle.load(
#     open('', 'rb'))
# parkinson_model = pickle.load(
#     open('', 'rb'))
# cad_model = pickle.load(
#     open('', 'rb'))


diagnosis=""
result=""
diagnosis_C=""
diagnosis_P=""
with open('style.css') as f:
    st.markdown(f'<style> {f.read()}</style>',unsafe_allow_html=True)
    # st.markdown(cust_css,unsafe_allow_html=True)
    st.sidebar.image('logo.png', width=300)
    st.header(" :green[Med_Guardian]")

    with st.sidebar:
        selected = opt(
            'Med_Guardian',
            [
                "Diabetes Prediction",
                "Parkinson Prediction",
                'Heart Disease Prediction',
                "CAD[Coronary Artery Disease] Prediction"
            ],
            icons=['','','heart','']
        )
if(selected=="Diabetes Prediction"):
    st.title("Diabetes Prediction")
    Pregnancies_D=0
    col1, col2, col3 = st.columns(3)

    with col1:
        Gender_input_d = st.selectbox("Gender",["Male","Female","Other"])
        Gender = 1 if Gender_input_d == "Male" else 0
        if(Gender == 0):
            Pregnancies_D = st.number_input("Number of Pregnancies",0,20,0,label_visibility="visible")
        #newcomment
