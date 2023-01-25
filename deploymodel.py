import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest

# Load the training data
df = pd.read_csv('deployment_and_lead_time_data.csv')

# Split the data into features and labels
X = df[['team_size', 'average_commit_frequency', 'average_review_time']]
y_deployment = df['deployment_frequency']
y_lead = df['lead_time']

# Train an Isolation Forest model for deployment frequency
deployment_model = IsolationForest()
deployment_model.fit(y_deployment.values.reshape(-1, 1))

# Train an Isolation Forest model for lead time
lead_model = IsolationForest()
lead_model.fit(y_lead.values.reshape(-1, 1))

# Use Streamlit to build the interface
st.title('Anomaly Detection')

# Add a form for entering data
input_data = st.form(key='input')
team_size = input_data.number_input('Team size', value=5)
average_commit_frequency = input_data.number_input('Average commit frequency (per week)', value=10)
average_review_time = input_data.number_input('Average review time (hours)', value=24)

def predict(data):
  deployment_prediction = deployment_model.predict(data)[0]
  lead_prediction = lead_model.predict(data)[0]
  return deployment_prediction, lead_prediction

# Add a button to trigger the prediction
submit = input_data.form_submit_button('Predict')
if submit:
  data = [[team_size, average_commit_frequency, average_review_time]]
  deployment_prediction, lead_prediction = predict(data)
  st.write(f'Predicted deployment frequency: {deployment_prediction:.2f} deployments per week')
  st.write(f'Predicted lead time: {lead_prediction:.2f} hours')

  # Check for anomalies in the predictions
  deployment_anomaly = deployment_model.predict(deployment_prediction.reshape(-1, 1))[0]
  lead_anomaly = lead_model.predict(lead_pred
