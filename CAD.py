import streamlit as st
import pickle



cad_model = pickle.load(
    open('C:\Med_Guardian\Cad.sav', 'rb'))
def cad():
    
    # page title
    st.title("CAD[Coronary Artery Disease] Prediction")
    col1, col2 = st.columns(2)

    with col1:  # Even-numbered titles
        Age_C = st.text_input('Age')
        Length_C = st.text_input('Length')
        BMI_C = st.text_input('BMI')
        DM_C_input = st.selectbox('Diabetes Mellitus (DM)', ['Yes', 'No'])
        DM_C = 1 if DM_C_input == 'Yes' else 0
        Current_Smoker_C_input = st.selectbox('Current Smoker', ['Yes', 'No'])
        Current_Smoker_C = 1 if Current_Smoker_C_input == 'Yes' else 0
        FH_C_input = st.selectbox('Family History of CAD (FH)', ['Yes', 'No'])
        FH_C = 1 if FH_C_input == 'Yes' else 0
        CRF_C_input = st.selectbox('Chronic Renal Failure (CRF)', ['Yes', 'No'])
        CRF_C = 1 if CRF_C_input == 'Yes' else 0
        Airway_Disease_C_input = st.selectbox('Airway Disease', ['Yes', 'No'])
        Airway_Disease_C = 1 if Airway_Disease_C_input == 'Yes' else 0
        CHF_C_input = st.selectbox('Congestive Heart Failure (CHF)', ['Yes', 'No'])
        CHF_C = 1 if CHF_C_input == 'Yes' else 0
        BP_C = st.text_input('Blood Pressure (BP)')
        Edema_C_input = st.selectbox('Edema', ['Yes', 'No'])
        Edema_C = 1 if Edema_C_input == 'Yes' else 0
        Lung_Rales_C_input = st.selectbox('Lung Rales', ['Yes', 'No'])
        Lung_Rales_C = 1 if Lung_Rales_C_input == 'Yes' else 0
        Diastolic_Murmur_C_input = st.selectbox('Diastolic Murmur', ['Yes', 'No'])
        Diastolic_Murmur_C = 1 if Diastolic_Murmur_C_input == 'Yes' else 0
        Dyspnea_C_input = st.selectbox('Dyspnea', ['Yes', 'No'])
        Dyspnea_C = 1 if Dyspnea_C_input == 'Yes' else 0
        Atypical_C_input = st.selectbox('Atypical Chest Pain', ['Yes', 'No'])
        Atypical_C = 1 if Atypical_C_input == 'Yes' else 0
        Exertional_CP_C_input = st.selectbox('Exertional Chest Pain', ['Yes', 'No'])
        Exertional_CP_C = 1 if Exertional_CP_C_input == 'Yes' else 0
        Q_Wave_C_input = st.selectbox('Q Wave', ['Yes', 'No'])
        Q_Wave_C = 1 if Q_Wave_C_input == 'Yes' else 0
        St_Depression_C_input = st.selectbox('ST Depression', ['Yes', 'No'])
        St_Depression_C = 1 if St_Depression_C_input == 'Yes' else 0
        LVH_C_input = st.selectbox('Left Ventricular Hypertrophy (LVH)', ['Yes', 'No'])
        LVH_C = 1 if LVH_C_input == 'Yes' else 0
        TG_C = st.text_input('Triglycerides (TG)')
        LDL_C = st.text_input('Low-Density Lipoprotein (LDL)')
        BUN_C = st.text_input('Blood Urea Nitrogen (BUN)')
        HB_C = st.text_input('Hemoglobin (HB)')
        Na_C = st.text_input('Sodium (Na)')
        Lymph_C = st.text_input('Lymphocyte Count (Lymph)')
        PLT_C = st.text_input('Platelet Count (PLT)')
        Region_RWMA_C = st.selectbox('Regional Wall Motion Abnormalities (RWMA)', [0,1,2,3,4])
        

    with col2:  # Odd-numbered titles
        Weight_C = st.text_input('Weight')
        Sex_C_input = st.selectbox('Sex', ['Male', 'Female',"Other"])
        Sex_C = 1 if Sex_C_input == 'Male' else 0
        HTN_C_input = st.selectbox('Hypertension (HTN)', ['Yes', 'No'])
        HTN_C = 1 if HTN_C_input == 'Yes' else 0
        EX_Smoker_C_input = st.selectbox('Ex-Smoker', ['Yes', 'No'])
        EX_Smoker_C = 1 if EX_Smoker_C_input == 'Yes' else 0
        Obesity_C_input = st.selectbox('Obesity', ['Yes', 'No'])
        Obesity_C = 1 if Obesity_C_input == 'Yes' else 0
        CVA_C_input = st.selectbox('Cerebrovascular Accident (CVA)', ['Yes', 'No'])
        CVA_C = 1 if CVA_C_input == 'Yes' else 0
        Thyroid_Disease_C_input = st.selectbox('Thyroid Disease', ['Yes', 'No'])
        Thyroid_Disease_C = 1 if Thyroid_Disease_C_input == 'Yes' else 0
        DLP_C_input = st.selectbox('Dyslipidemia (DLP)', ['Yes', 'No'])
        DLP_C = 1 if DLP_C_input == 'Yes' else 0
        PR_C = st.text_input('Pulse Rate (PR)')
        Weak_Peripheral_Pulse_C_input = st.selectbox('Weak Peripheral Pulse', ['Yes', 'No'])
        Weak_Peripheral_Pulse_C = 1 if Weak_Peripheral_Pulse_C_input == 'Yes' else 0
        Systolic_Murmur_C_input = st.selectbox('Systolic Murmur', ['Yes', 'No'])
        Systolic_Murmur_C = 1 if Systolic_Murmur_C_input == 'Yes' else 0
        Typical_Chest_Pain_C_input = st.selectbox('Typical Chest Pain', ['Yes', 'No'])
        Typical_Chest_Pain_C = 1 if Typical_Chest_Pain_C_input == 'Yes' else 0
        Function_Class_C_input = st.selectbox('Functional Class', ['Class I', 'Class II', 'Class III', 'Class IV'])
        Function_Class_mapping_C = {
            "Class I":0,
            "Class II":1,
            "Class III":2,
            "Class IV":3,

        }
        Function_Class_C = Function_Class_mapping_C[Function_Class_C_input]
        Nonanginal_C_input = st.selectbox('Nonanginal Chest Pain', ['Yes', 'No'])
        Nonanginal_C = 1 if Nonanginal_C_input == 'Yes' else 0
        LowTH_Ang_C_input = st.selectbox('Low Threshold Angina', ['Yes', 'No'])
        LowTH_Ang_C = 1 if LowTH_Ang_C_input == 'Yes' else 0
        St_Elevation_C_input = st.selectbox('ST Elevation', ['Yes', 'No'])
        St_Elevation_C = 1 if St_Elevation_C_input == 'Yes' else 0
        Tinversion_C_input = st.selectbox('T-wave Inversion', ['Yes', 'No'])
        Tinversion_C = 1 if Tinversion_C_input == 'Yes' else 0
        Poor_R_Progression_C_input = st.selectbox('Poor R Wave Progression', ['Yes', 'No'])
        Poor_R_Progression_C = 1 if Poor_R_Progression_C_input == 'Yes' else 0
        FBS_C = st.text_input('Fasting Blood Sugar (FBS)')
        CR_C = st.text_input('Creatinine (CR)')
        HDL_C = st.text_input('High-Density Lipoprotein (HDL)')
        ESR_C = st.text_input('Erythrocyte Sedimentation Rate (ESR)')
        K_C = st.text_input('Potassium (K)')
        WBC_C = st.text_input('White Blood Cell Count (WBC)')
        Neut_C = st.text_input('Neutrophil Count (Neut)')
        EF_TTE_C = st.text_input('Ejection Fraction (EF) from TTE')
        VHD_C_input = st.selectbox('Valvular Heart Disease (VHD)', ["None","Mild","Moderate","Severe"])
        VHD_C_input_mapping = {
            "None":0,
            "Mild":1,
            "Moderate":2,
            "Severe":3
        }
        VHD_C = VHD_C_input_mapping[VHD_C_input]

    # Code for prediction
    diagnosis_C = ''




# Code for CAD prediction
    if st.button("CAD Test Result"):
        try:
            # Convert inputs to numeric types (handle empty or invalid inputs)
            try:
                Age_C = float(Age_C)
            except ValueError:
                st.error("Error converting 'Age' to a number")
                raise
            
            try:
                Weight_C = float(Weight_C)
            except ValueError:
                st.error("Error converting 'Weight' to a number")
                raise
            
            try:
                Length_C = float(Length_C)
            except ValueError:
                st.error("Error converting 'Length' to a number")
                raise
            
            try:
                BMI_C = float(BMI_C)
            except ValueError:
                st.error("Error converting 'BMI' to a number")
                raise
            
            try:
                BP_C = float(BP_C)
            except ValueError:
                st.error("Error converting 'Blood Pressure (BP)' to a number")
                raise
            
            try:
                PR_C = float(PR_C)
            except ValueError:
                st.error("Error converting 'Pulse Rate (PR)' to a number")
                raise
            
            try:
                FBS_C = float(FBS_C)
            except ValueError:
                st.error("Error converting 'Fasting Blood Sugar (FBS)' to a number")
                raise
            
            try:
                CR_C = float(CR_C)
            except ValueError:
                st.error("Error converting 'Creatinine (CR)' to a number")
                raise
            
            try:
                TG_C = float(TG_C)
            except ValueError:
                st.error("Error converting 'Triglycerides (TG)' to a number")
                raise
            
            try:
                LDL_C = float(LDL_C)
            except ValueError:
                st.error("Error converting 'Low-Density Lipoprotein (LDL)' to a number")
                raise
            
            try:
                HDL_C = float(HDL_C)
            except ValueError:
                st.error("Error converting 'High-Density Lipoprotein (HDL)' to a number")
                raise
            
            try:
                BUN_C = float(BUN_C)
            except ValueError:
                st.error("Error converting 'Blood Urea Nitrogen (BUN)' to a number")
                raise
            
            try:
                ESR_C = float(ESR_C)
            except ValueError:
                st.error("Error converting 'Erythrocyte Sedimentation Rate (ESR)' to a number")
                raise
            
            try:
                HB_C = float(HB_C)
            except ValueError:
                st.error("Error converting 'Hemoglobin (HB)' to a number")
                raise
            
            try:
                K_C = float(K_C)
            except ValueError:
                st.error("Error converting 'Potassium (K)' to a number")
                raise
            
            try:
                Na_C = float(Na_C)
            except ValueError:
                st.error("Error converting 'Sodium (Na)' to a number")
                raise
            
            try:
                WBC_C = float(WBC_C)
            except ValueError:
                st.error("Error converting 'White Blood Cell Count (WBC)' to a number")
                raise
            
            try:
                Lymph_C = float(Lymph_C)
            except ValueError:
                st.error("Error converting 'Lymphocyte Count (Lymph)' to a number")
                raise
            
            try:
                Neut_C = float(Neut_C)
            except ValueError:
                st.error("Error converting 'Neutrophil Count (Neut)' to a number")
                raise
            
            try:
                PLT_C = float(PLT_C)
            except ValueError:
                st.error("Error converting 'Platelet Count (PLT)' to a number")
                raise
            
            try:
                EF_TTE_C = float(EF_TTE_C)
            except ValueError:
                st.error("Error converting 'Ejection Fraction (EF)' to a number")
                raise

            # Make prediction
            cad_predict = cad_model.predict([[
                Age_C, Weight_C, Length_C, Sex_C, BMI_C, DM_C, HTN_C, Current_Smoker_C, EX_Smoker_C, FH_C, Obesity_C,
                CRF_C, CVA_C, Airway_Disease_C, Thyroid_Disease_C, CHF_C, DLP_C, BP_C, PR_C, Edema_C, Weak_Peripheral_Pulse_C,
                Lung_Rales_C, Systolic_Murmur_C, Diastolic_Murmur_C, Typical_Chest_Pain_C, Dyspnea_C, Function_Class_C,
                Atypical_C, Nonanginal_C, Exertional_CP_C, LowTH_Ang_C, Q_Wave_C, St_Elevation_C, St_Depression_C, Tinversion_C,
                LVH_C, Poor_R_Progression_C, FBS_C, CR_C, TG_C, LDL_C, HDL_C, BUN_C, ESR_C, HB_C, K_C, Na_C, WBC_C,
                Lymph_C, Neut_C, PLT_C, EF_TTE_C, Region_RWMA_C, VHD_C
            ]])

            # Display the prediction result
            if cad_predict[0] == 1:
                diagnosis_C = "The person is at risk of CAD"
            else:
                diagnosis_C = "The person is not at risk of CAD"

            st.success(diagnosis_C)
        
        except ValueError as e:
            st.error(f"Input error: {e}")
