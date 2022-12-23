import streamlit as st
import pandas as pd
import numpy as np

# Load the CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Prompt the user for the 'Application'
    application = st.selectbox("Select an application:", df['Application'].unique())

    # Filter the dataframe to only include the selected application
    filtered_df = df[df['Application'] == application]

    # Convert the 'deployment date' values to datetime objects
    filtered_df['deployment date'] = pd.to_datetime(filtered_df['deployment date'])

    # Calculate the deployment frequency for the selected application
    deployment_dates = filtered_df['deployment date'].sort_values().reset_index(drop=True)
    diffs = deployment_dates.diff()
    median_diff = np.median(diffs)

    # Convert the median difference to days, weeks, or months
    if median_diff <= pd.Timedelta(days=1):
        frequency = "Daily"
    elif median_diff <= pd.Timedelta(weeks=1):
        frequency = "Weekly"
    else:
        frequency = "Monthly"

    # Display the frequency in a text field
    st.write(f"The deployment frequency for {application} is {frequency}.")

    # Display the selected application's data in a table
    st.dataframe(filtered_df)
