import pickle
import streamlit as st
from streamlit_option_menu import option_menu as opt
from sidebar.Diabetes import diabetes
from sidebar.Heart import heart
from sidebar.Parkinson import park
from sidebar.CAD import cad
from Nav.home import home_page
from Nav.Nav import nav
from streamlit_navigation_bar import st_navbar
from Ocr_reader import *



#import sab mathi ni garne 

#pickle loaders
diabetes_model = pickle.load(
    open('C:\Med_Guardian\Diabetes.sav', 'rb'))
heart_model = pickle.load(
    open('C:\Med_Guardian\Heart.sav', 'rb'))
parkinson_model = pickle.load(
    open('C:\Med_Guardian\Parkinsons.sav', 'rb'))
cad_model = pickle.load(
    open('C:\Med_Guardian\Cad.sav', 'rb'))
# page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])



#initializing variables paxi error na aaos bhanera
diagnosis=""
result=""
diagnosis_C=""
diagnosis_P=""



with open('style.css') as f: #style add garne from style.css
    st.markdown(f'<style> {f.read()}</style>',unsafe_allow_html=True)#style given
    st.sidebar.image('logo.png')     #logo added to sidebar
    st.header(" :green[Med_Guardian]")


    #only sidebar elements
    with st.sidebar:
        selected_sidebar = opt(
            'Med_Guardian',
            [   "Home",
                "Test All",
                "Diabetes Prediction",
                "Parkinson Prediction",
                'Heart Disease Prediction',
                "CAD[Coronary Artery Disease] Prediction",
            ],
            icons=['home', 'test-tube', 'blood-drop', 'brain', 'heart', 'artery']
        )
if(selected_sidebar=="Home"):
    nav()
#checking camera input to test all diseases 
if(selected_sidebar=="Test All"):
    select_inp = st.selectbox(
        "Select input Method",[
            # 'Choose Option',
            "Upload Photo",
            "Mannual Input",
            "Open Camera"
        ]
    )
    if(select_inp=="Open Camera"):
        camera_inp = st.camera_input("Click Photo of Report")
        if(camera_inp is not None):
            st.image(camera_inp, caption="Captured Image", use_column_width=True)
    elif (select_inp=='Upload Photo'):
        MainMethod()
    elif (select_inp=='Mannual Input'):
        st.write("Navigate through Sidebar")


#diabetes prediction
if(selected_sidebar=="Diabetes Prediction"):
    diabetes()
#heart disease prediction
if selected_sidebar == 'Heart Disease Prediction':
    heart()
        
#parkinson prediciton
if selected_sidebar == 'Parkinson Prediction':
    park()


#FOR CAD
if (selected_sidebar == 'CAD[Coronary Artery Disease] Prediction'):
    cad()