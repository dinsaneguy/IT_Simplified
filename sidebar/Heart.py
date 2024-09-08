import streamlit as st
import pickle
from Ocr_reader import *

heart_model = pickle.load(
    open('C:\Med_Guardian\Heart.sav', 'rb'))
def heart():
    st.title("Heart Disease Prediction System")
    col1, col2 = st.columns(2)
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
        with col1:
            # Input fields in the first column
            Age_H = st.text_input("Age of the person")
            Cp_input_H = st.selectbox("Select Your Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
            Cp_mapping_H = {
                "Typical Angina": 0,
                "Atypical Angina": 1,
                "Non-Anginal Pain": 2,
                "Asymptomatic": 3
            }
            Cp_H = Cp_mapping_H[Cp_input_H]

            Chol_H = st.text_input("(Chol) Serum cholesterol in mg/dl")
            Restecg_input_H = st.selectbox("Resting ecg results", ["Normal", "ST-T wave abnormality", "left ventricular hypertrophy"])
            Restecg_mapping_H= {
                "Normal": 0,
                "ST-T wave abnormality":1,
                "left ventricular hypertrophy":2
            }
            Restecg_H = Restecg_mapping_H[Restecg_input_H]

            Exang_input_H = st.selectbox("(exang) Exercise induced angina", ["Yes", "No"])
            Exang_H = 1 if Exang_input_H == "Yes" else 0
            Slope_input_H = st.selectbox("Slope of the peak exercise ST segment)", ["Upsloping", "Flat", "Downsloping"])
            Slope_mapping_H = {
                "Upsloping":0,
                "Flat":1,
                "Downsloping":2
            }
            Slope_H = Slope_mapping_H[Slope_input_H]
            Thal_input_H = st.selectbox("(thal) Thalassemia", ["Normal", "Fixed Defect", "reversible Defect"])
            Thal_mapping_H = {
                "Normal":1,
                "Fixed Defect":2,
                "Reversible Defect":3
            }
            Thal_H = Thal_mapping_H[Thal_input_H]
        with col2:
            # Input fields in the second column
            Sex_input_H = st.selectbox("Sex", ["Male", "Female","Others"])
            Sex_H = 1 if Sex_input_H == "Male" else 0
            Trestbps_H = st.text_input("(trestbps) Resting blood pressure (in mm Hg)")
            Fbs_input_H = st.selectbox("(fbs) Fasting blood sugar > 120 mg/dl", ["Yes", "No"])
            Fbs_H = 1 if Fbs_input_H == "Yes" else 0
            Thalach_H = st.text_input("(thalach) Maximum heart rate achieved")
            Oldpeak_H = st.text_input("(oldpeak) ST depression induced")
            Ca_H = st.text_input("(ca) Number of major vessels (0-3) colored by fluoroscopy")
        
        # Initialize result variable
        result = ''

        # Button for prediction
        if st.button("Heart Disease Test Result"):
            # Convert inputs to numeric types
            try:
                Age_H = int(Age_H)
                Trestbps_H = float(Trestbps_H)
                Chol_H = float(Chol_H)
                Thalach_H = float(Thalach_H)
                Oldpeak_H = float(Oldpeak_H)
                Ca_H = float(Ca_H)

                # Make prediction
                heart_Predict = heart_model.predict(
                    [[Age_H, Sex_H, Cp_H, Trestbps_H, Chol_H, Fbs_H, Restecg_H, Thalach_H, Exang_H, Oldpeak_H, Slope_H, Ca_H, Thal_H]]
                )

                # Display result based on prediction
                if heart_Predict[0] == 0:
                    result = "Our system estimates Heart Disease risk but can't guarantee results"
                else:
                    result = "Our system predicts you do not have Heart Disease, but this is not a guarantee"
            
            except ValueError:
                st.error("Please enter valid numeric values for all fields.")

        st.success(result)
