import streamlit as st
import pickle
from Ocr_reader import *

parkinson_model = pickle.load(
    open('C:\Med_Guardian\Parkinsons.sav', 'rb'))
def park():
    st.title("Parkinson Prediction") 

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
        # Collect all necessary inputs for prediction
        with col1:
            MDVP_Fo_P = st.text_input('MDVP Fo Hz')
            MDVP_Fhi_P = st.text_input('MDVP Fhi Hz')
            MDVP_Flo_P = st.text_input('MDVP Flo Hz)')
            MDVP_Jitter_percent_P = st.text_input('MDVP Jitter %')
            MDVP_Jitter_Abs_P = st.text_input('MDVP Jitter Abs')
            MDVP_RAP_P = st.text_input('MDVP RAP')
            MDVP_PPQ_P = st.text_input('MDVP PPQ')
            Jitter_DDP_P = st.text_input('Jitter DDP')
            MDVP_Shimmer_P = st.text_input('MDVP Shimmer')
            MDVP_Shimmer_dB_P = st.text_input('MDVP Shimmer dB)')
            Shimmer_APQ3_P = st.text_input('Shimmer APQ3')

        with col2:
            Shimmer_APQ5_P = st.text_input('Shimmer APQ5')
            MDVP_APQ_P = st.text_input('MDVP APQ')
            Shimmer_DDA_P = st.text_input('Shimmer DDA')
            NHR_P = st.text_input('NHR')
            HNR_P = st.text_input('HNR')
            # status_P = st.text_input('status')
            RPDE_P = st.text_input('RPDE')
            DFA_P = st.text_input('DFA')
            spread1_P = st.text_input('spread1')
            spread2_P = st.text_input('spread2')
            D2_P = st.text_input('D2')
            PPE_P = st.text_input('PPE')

        # Code for prediction
        diagnosis_P = ''

        if st.button("Parkinson Test Result"):
            try:
                # Convert inputs to correct data types (e.g., float, int)
                parkinson_predict = parkinson_model.predict([[
                    float(MDVP_Fo_P), float(MDVP_Fhi_P), float(MDVP_Flo_P), float(MDVP_Jitter_percent_P),
                    float(MDVP_Jitter_Abs_P), float(MDVP_RAP_P), float(MDVP_PPQ_P), float(Jitter_DDP_P),
                    float(MDVP_Shimmer_P), float(MDVP_Shimmer_dB_P), float(Shimmer_APQ3_P), float(Shimmer_APQ5_P),
                    float(MDVP_APQ_P), float(Shimmer_DDA_P), float(NHR_P), float(HNR_P),
                    float(RPDE_P), float(DFA_P), float(spread1_P), float(spread2_P), float(D2_P), float(PPE_P)
                ]])
                
                if parkinson_predict[0] == 1:
                    diagnosis_P = "Our system estimates Parkison risk but can't guarantee results"
                else:
                    diagnosis_P = "Our system predicts you do not have Parkinson, but this is not a guarantee"

                st.success(diagnosis_P)

            except ValueError as e:
                st.error(f"Input error: {e}")