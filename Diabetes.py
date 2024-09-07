import streamlit as st
import pickle
from streamlit_option_menu import option_menu as opt
diabetes_model = pickle.load(
open('C:\Med_Guardian\Diabetes.sav', 'rb'))
def diabetes():
    diagnosis=""
    st.title("Diabetes Prediction")
    Pregnancies_d=0
    col1, col2, col3 = st.columns(3)

    with col1:
        Gender_input_d = st.selectbox("Gender",["Male","Female","Other"])
        Gender_d = 1 if Gender_input_d == "Male" else 0
        if(Gender_d == 0):
            Pregnancies_d = st.number_input("Number of Pregnancies",0,20,0)
        Age_d = st.number_input("Age",0,120,14,step=1)
    with col2:
        Glucose_d = st.number_input("Glucose Level (mg/dl)",0,600,100)
        Skin_Thickness_d = st.number_input("Skin Thickness in mm")
        Insulin_d = st.number_input("Insulin Level(microunits/ml)")
    with col3:
        BP_d = st.number_input("Diastolic Blood Pressure (mm hg)",40,400,180,step=1)
        BMI_d = st.number_input("BMI",0.01,100.00,20.00,step=1.0)
        DPF_d = st.number_input("DPF",0.000,3.000,1.000,step=0.005)#Diabetes Predigree Function
    if(st.button("Predict Diabetes")):

        diab_Predict = diabetes_model.predict([[Pregnancies_d,Glucose_d,BP_d,Skin_Thickness_d,Insulin_d,BMI_d,DPF_d,Age_d]])
        if (diab_Predict[0] == 1):
            diagnosis = "The person is Diabetic"
        else:
            diagnosis = "The person is not Diabetic"
    st.success(diagnosis)