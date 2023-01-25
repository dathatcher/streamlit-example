import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.title('Deployment Statistics')

# Allow user to upload a CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Read the CSV file into a dataframe
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Convert 'date_of_first_code_commit' and 'deployment_date' to datetime objects
    df['date_of_first_code_commit'] = pd.to_datetime(df['date_of_first_code_commit'])
    df['deployment_date'] = pd.to_datetime(df['deployment_date'])

    # Prompt user to select an application
    app_name = st.selectbox('Select an application:', df['Application'].unique())

    # Filter the dataframe to only include the selected application
    app_df = df[df['Application'] == app_name]

    # Calculate deployment frequency
    deployment_counts = app_df['deployment_date'].value_counts()
    if deployment_counts.max() == 1:
        deployment_frequency = 'Monthly'
    elif deployment_counts.max() <= 7:
        deployment_frequency = 'Weekly'
    else:
        deployment_frequency = 'Daily'

    # Calculate lead time
    lead_times = []
    for index, row in app_df.iterrows():
        lead_time = row['deployment_date'] - row['date_of_first_code_commit']
        lead_times.append(lead_time.days)
    lead_time = pd.Series(lead_times).median()

    # Display deployment frequency and lead time
    st.write(f'Deployment frequency: {deployment_frequency}')
    st.write(f'Lead time: {lead_time} days')

    # Display selected application's data in a table
    st.dataframe(app_df)
