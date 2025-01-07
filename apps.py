


import pickle
import streamlit as st
from PIL import Image

import pandas as pd

from joblib import load

def predict():

    st.title(':orange[BANK MARKETING SUCCESS PREDICTION]')
    st.write("[Colab Notebook Link](https://colab.research.google.com/drive/1vELLot4e1iCcOTxGc0M3B8JVP_PZcj1W)")

    model=pickle.load(open('model.sav','rb'))

    scaler=pickle.load(open('scaler.sav','rb'))


    age=st.text_input('Enter the age of client',key='age_input')

    job=st.selectbox('Enter the job of the client',['Blue-collar','Management','Technician','Admin','Services','Retired','Self-employed','Entrepreneur','Unemployed','Housemaid','Student'])
    st.write("You selected:", job)

    if job == 'Blue-collar':
        j = 1
    elif job == 'Management':
        j = 4
    elif job == 'Technician':
        j = 9
    elif job == 'Admin':
        j = 0
    elif job == 'Services':
        j = 7
    elif job == 'Retired':
        j = 5
    elif job == 'Self-employed':
        j = 6
    elif job == 'Entrepreneur':
        j = 2
    elif job == 'Unemployed':
        j = 10
    elif job == 'Housemaid':
        j = 3
    else:
        j = 8

    marital=st.radio('Enter the marital status of the client',['Single','Married','Divorced'])
    st.write("You selected:", marital)
    if marital == "Married":
        ma = 1
    elif marital == "Single":
        ma = 2
    else:
        ma = 0

    education=st.radio('Enter the educational status of the client', ['Primary', 'Secondary', 'Tertiary'])
    st.write("You selected:", education)
    if education == "Tertiary":
        ed = 2
    elif education == "Secondary":
        ed = 1
    else:
        ed = 0

    loan_default_status=st.radio('Loan default history of client',['No','Yes'])
    st.write("You selected:", loan_default_status)
    if loan_default_status=='No':
        lo=0
    else:
        lo=1

    account_balance=st.text_input('Enter the account balance of client')

    housing = st.radio('Housing status of the client', ['No', 'Yes'])
    st.write("You selected:", housing)
    if housing=='No':
        h=0
    else:
        h=1

    loan=st.radio('Weather the client had taken any loan', ['No', 'Yes'])
    st.write("You selected:", loan)
    if loan=='No':
        ls=0
    else:
        ls=1

    contact=st.radio('Select the contact mode of the client', ['Cellular', 'Telephone'])
    st.write("You selected:", contact)
    if contact=='Cellular':
        co=0
    else:
        co=1


    contacted_day_of_month = st.slider('Enter the day of the month when the client was coontacted', min_value=1, max_value=31)

    month=st.selectbox('Enter the month in which client was contacted',['January','Febuary','March','April','May','June','July','August','September','October','November','December'])
    st.write("You selected:", month)
    if month=='January':
        m=4
    elif month=='February':
        m=3
    elif month=='March':
        m=7
    elif month=='April':
        m=0
    elif month=='May':
        m=8
    elif month=='June':
        m=6
    elif month=='July':
        m=5
    elif month=='August':
        m=1
    elif month=='September':
        m=11
    elif month=='October':
        m=10
    elif month=='November':
        m=9
    else:
        m=2

    call_duration=st.text_input('Enter the duration of call with the client in second')

    campaign_call = st.text_input('Enter the number of campaign calls made with the client')

    no_days_passed = st.text_input('Enter the number of days passed after the call')

    previous_campaign_call = st.text_input('Enter number of previous campaign calls')

    pred=st.button(':red[PREDICT]')
    features=[age,j,ma,ed,lo,account_balance,h,ls,co,contacted_day_of_month,m,call_duration,campaign_call,no_days_passed,previous_campaign_call]
    #features = pd.to_numeric(features, errors='coerce')


    if pred:
        try:
            result = model.predict(scaler.transform([features]))

            if result==0:
              st.write('Client will not subscribe to Term deposit')
            else:
              st.write('Client will subscribe to Term deposit')
        except:
            st.write('Check the inputs:exclamation:')
predict()
