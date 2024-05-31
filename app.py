import streamlit as st
import requests

'''
# TaxiFare Prediction Model
'''

'''
## Select the parameters of the ride

1. We ask for:
'''
date_and_time = st.text_input("date and time: ")
pickup_longitude = st.text_input("pickup longitude: ")
pickup_latitude = st.text_input("pickup latitude: ")
dropoff_longitude = st.text_input("dropoff longitude: ")
dropoff_latitude = st.text_input("dropoff latitude: ")
passenger_count = st.text_input("passenger count: ")

url = 'https://taxifare.lewagon.ai/predict'

params = {
    'pickup_datetime':date_and_time,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
    }

if st.button('Predict'):
    response = requests.get(
        url,
        params=params,
    ).json()

    prediction = response['fare']

    f'''
    # Predicted Fare is of {round(prediction)}$
    '''
