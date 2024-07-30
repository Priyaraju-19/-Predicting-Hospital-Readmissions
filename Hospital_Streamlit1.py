import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import pickle
from PIL import Image

import warnings
warnings.filterwarnings("ignore")

#________________________________________________________________________

def predict_readmission(Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
                        Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
                        Num_Emergency_Visits, Num_Diagnoses, A1C_Result):

    with open("Readmitted_Model.pkl","rb") as m:
        model = pickle.load(m)
    
    data = np.array([[Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
                      Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
                      Num_Emergency_Visits, Num_Diagnoses, A1C_Result]])
    prediction = model.predict(data)
    out = prediction[0]
    return out 

#_________________________________________________________________________

st.set_page_config(page_title="Predicting Hospital Readmissions",
                   layout="wide",
                   menu_items={'About': "### This page is created by Desilva!"})

st.markdown("<h1 style='text-align: center; color: #fa6607;'>Predicting Hospital Readmissions</h1>", unsafe_allow_html=True)
st.write("")

select = option_menu(None, ["Home", "Readmission"], 
                    icons=["hospital-fill", "ticket-detailed"], orientation="horizontal",
                    styles={"container": {"padding": "0!important", "background-color": "#fafafa"},
                            "icon": {"color": "#fdfcfb", "font-size": "20px"},
                            "nav-link": {"font-size": "20px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
                            "nav-link-selected": {"background-color": "#fa6607"}})

if select == "Home":
    st.title("Welcome to the Hospital Readmissions Prediction Project!")
    st.write('''
    This project aims to predict whether a patient will be readmitted to the hospital based on various factors such as demographics, admission details, and medical history.
    ''')

elif select == "Readmission":
    st.write("")
    st.header("Fill all the details below to know the prediction")
    st.write("")

    col1, col2, col3 = st.columns([5, 1, 5])
    with col1:
        selected_gender = st.selectbox('Select a Gender:', ["Female", "Male", "Other"])
        Gender = {"Female": 0, "Male": 1, "Other": 2}[selected_gender]

        Selected_Admission_Type = st.selectbox('Select an Admission Type:', ['Emergency', 'Urgent', 'Elective'])
        Admission_Type = {"Emergency": 1, "Urgent": 2, "Elective": 0}[Selected_Admission_Type]

        Selected_Diagnosis = st.selectbox('Select a Diagnosis:', ['Heart Disease', 'Diabetes', 'Injury', 'Infection'])
        Diagnosis = {"Heart Disease": 1, "Diabetes": 0, "Injury": 3, "Infection": 2}[Selected_Diagnosis]

        Num_Lab_Procedures = st.selectbox('Select the Number of Lab Procedures:', range(1, 100))
        Num_Medications = st.selectbox('Select the Number of Medications:', range(1, 36))

    with col3:
        Num_Outpatient_Visits = st.selectbox('Select the Number of Outpatient Visits:', range(0, 5))
        Num_Inpatient_Visits = st.selectbox('Select the Number of Inpatient Visits:', range(0, 5))
        Num_Emergency_Visits = st.selectbox('Select the Number of Emergency Visits:', range(0, 5))
        Num_Diagnoses = st.selectbox('Select the Number of Diagnoses:', range(1, 10))

        A1C = st.selectbox('Select A1C Result:', ['Normal', 'Abnormal'])
        A1C_Result = {"Normal": 1, "Abnormal": 0}[A1C]

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns([3, 4, 3])
    with col2:
        button = st.button(":red[PREDICT THE READMISSION]", use_container_width=True)

        if button:
            admission = predict_readmission(Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
                                            Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
                                            Num_Emergency_Visits, Num_Diagnoses, A1C_Result)
            if admission == 1:
                st.write("## :red[Readmission is Required]")
            else:
                st.write("## :green[Readmission is Not Required]")  
