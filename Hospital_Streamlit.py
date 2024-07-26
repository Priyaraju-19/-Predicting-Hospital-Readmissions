# import
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

st.set_page_config(page_title= "Predicting Hospital Readmissions",
                   layout= "wide",
                   menu_items={'About': "### This page is created by Desilva!"})

st.markdown("<h1 style='text-align: center; color: #fa6607;'>Predicting Hospital Readmissions</h1>", unsafe_allow_html=True)
st.write("")

select = option_menu(None,["Home", "Readmission"], 
                    icons =["hospital-fill","ticket-detailed"], orientation="horizontal",
                    styles={"container": {"padding": "0!important", "background-color": "#fafafa"},
                            "icon": {"color": "#fdfcfb", "font-size": "20px"},
                            "nav-link": {"font-size": "20px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
                            "nav-link-selected": {"background-color": "#fa6607"}})

if select == "Home":
    st.title("Welcome to the Hospital Readmissions Prediction Project!")

    st.write('''

elif select == "Readmission":

    st.write("")
    st.header("Fill all the details below to know the prediction")
    st.write("")

    col1,col2,col3 = st.columns([5,1,5])
    with col1:
        selected_gender = st.selectbox('Select a Gender:', ["Female", "Male", "Other"])
        if selected_gender == "Female":
            Gender = 0
        elif selected_gender == "Male":
            Gender = 1
        else:
            Gender = 2


        Selected_Admission_Type  = st.selectbox('Select a Admission Type:', ['Emergency','Urgent', 'Elective'])
        if Selected_Admission_Type  == "Emergency":
            Admission_Type = 1
        elif Selected_Admission_Type == "Urgent":
            Admission_Type = 2
        else:
            Admission_Type = 0

        Selected_Diagnosis  = st.selectbox('Select a Diagnosis:', ['Heart Disease', 'Diabetes', 'Injury', 'Infection'])
        if Selected_Admission_Type  == "Heart Disease":
            Diagnosis = 1
        elif Selected_Admission_Type == "Diabetes":
            Diagnosis = 0
        elif Selected_Admission_Type == "Injury":
            Diagnosis = 3
        else:
            Diagnosis = 2

        Num_Lab_Procedures  = st.selectbox('Select a Number of Lab Procedures:', range(1,100))

        Num_Medications  = st.selectbox('Select a Number of Medications:', range(1,36))
                         
    with col3:
        Num_Outpatient_Visits  = st.selectbox('Select a Number of Outpatient Visits:', range(0,5))

        Num_Inpatient_Visits  = st.selectbox('Select a Number of Inpatient Visits:', range(0,5))

        Num_Emergency_Visits  = st.selectbox('Select a Number of Emergency Visits:', range(0,5))

        Num_Diagnoses  = st.selectbox('Select a Number of Diagnoses:', range(1,10))

        A1C = st.selectbox('Select a Number of A1C Result:', ['Normal','Abnormal'])
        if A1C  == "Normal":
            A1C_Result = 1
        else:
            A1C_Result = 0

    st.write("")
    st.write("")

    col1,col2,col3 = st.columns([3,4,3])
    with col2:
        button = st.button(":red[PREDICT THE READMISSION]",use_container_width= True)

        if button:
            admission = predict_readmission(Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
       Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
       Num_Emergency_Visits, Num_Diagnoses, A1C_Result)
            if admission == 1:
                st.write("## :red[Readmission is Required]")
            else:
                st.write("## :green[Readmission is Not Required]")                


#__________________________________________END_____________________________________________________________
            
