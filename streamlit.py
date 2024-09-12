import streamlit as st
import requests
import pandas as pd
import numpy as np

# URL de l'API Flask
API_URL = "http://localhost:5000/predict"

st.set_page_config(page_title="Prédictions de Modèle", page_icon=":star:")

st.title('Prédictions de Modèle')

st.markdown("""
    <style>
    .big-font {
        font-size:24px !important;
        color: #1E90FF;
    }
    .custom-button {
        background-color: #FF6347;
        color: white;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

st.header('Entrer les données pour prédiction')

# Formulaire pour entrer les données avec des clés uniques
input_data = {
    'CreditScore': st.text_input('Enter the Credit Score', key='credit_score'),
    'Units': st.selectbox('Choose the Unit', [0, 1], key='unit_selector'),
    'PropertyType': st.text_input('Enter the PropertyType', key='property_type'),
    'OrigLoanTerm': st.text_input('Enter the OrigLoanTerm', key='orig_loanTerm'),
    'NumBorrowers': st.text_input('Enter the NumBorrowers', key='num_borrowers'),
    'MonthsDelinquent': st.selectbox('Choose the MonthsDelinquent', [0, 1], key='months_delinquent'),
    'MonthsInRepayment': st.text_input('Enter the MonthsInRepayment', key='months_in_repayment'),
    'Occupancy_O': st.selectbox('Choose the Occupancy', [0, 'juste 0'], key='occupancy_o'),
    'MonthlyIncome': st.text_input('Enter the MonthlyIncome', key='monthly_income'),
    'InterestAmount': st.text_input('Enter the InterestAmount', key='interest_amount'),
    'Totalpayment': st.text_input('Enter the Totalpayment', key='total_payment'),
    'MonthlyInstallment': st.text_input('Enter the MonthlyInstallment', key='monthly_installment'),
    'OrigUPB': st.text_input('Enter the OrigUPB', key='orig_upb'),
    'CurrentUPB': st.text_input('Enter the CurrentUPB', key='current_upb'),
    'DTI': st.text_input('Enter the DTI', key='dti'),
    'LoanSeqNum': st.text_input('Enter the LoanSeqNum', key='loan_seq_num'),
    'FirstTimeHomebuyer': st.selectbox('Choose the FirstTimeHomebuyer', [0, 1], key='first_time_homebuyer'),
}

# Bouton pour soumettre les données avec une clé unique
if st.button('Faire une prédiction', key='predict_button'):
    df = pd.DataFrame([input_data])

    response = requests.post(API_URL, json=df.to_dict(orient='records'))

    if response.status_code == 200:
        result = response.json()
        st.subheader('Résultats de la Prédiction')
        if result['class_predictions'][0] == 1:
            st.write('classification : EverDeliquent')
            rounded_prediction = round(result['reg_predictions'][0], 2)
            st.write('Prediction of prepayment risk:', rounded_prediction)
        else:
            st.write(
                'Prédictions de classification :Not EverDeliquent, Prepayement risk prediction not needed')

    else:
        st.error('Erreur lors de la requête à l\'API')
