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
                "Diabetes Prediction",
                "Parkinson Prediction",
                'Heart Disease Prediction',
                "CAD[Coronary Artery Disease] Prediction",
            ],
            icons=['house', 'droplet', 'brilliance', 'heart', 'heart', 'artery']
        )
if(selected_sidebar=="Home"):
    nav()
#checking camera input to test all diseases 


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