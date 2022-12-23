import streamlit as st
#import sklearn
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load the data model
model = RandomForestRegressor()
model.load('application_testing_model.pkl')

# Load the data
df = pd.read_csv('application_testing_data.csv')

# Create a user interface to enter data
st.title('Application Testing Quality Predictor')

test_cases_passed = st.number_input('Number of test cases passed')
test_cases_failed = st.number_input('Number of test cases failed')
bugs_reported = st.number_input('Number of bugs reported')

# Predict the quality based on the entered data
prediction = model.predict([[test_cases_passed, test_cases_failed, bugs_reported]])[0]
prediction_text = 'Based on the entered data, the predicted quality is: {:.2f}'.format(prediction)
st.write(prediction_text)