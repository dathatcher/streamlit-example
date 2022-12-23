import streamlit as st
import pandas as pd

# Prompt the user to upload a CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# If a file is uploaded, read it into a Pandas DataFrame
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, parse_dates=["deployment date"], infer_datetime_format=True)

    # Prompt the user to select an application
    application = st.selectbox("Select an application:", df["Application"].unique())

    # Filter the DataFrame to only include rows for the selected application
    df = df[df["Application"] == application]

    # Calculate the deployment frequency
    deployment_counts = df["deployment date"].dt.week.value_counts()
    if (deployment_counts >= 3).any():
        frequency = "Daily"
    elif (deployment_counts >= 3).sum() >= 3:
        frequency = "Weekly"
    else:
        frequency = "Monthly"

    # Display the frequency in a text field
    st.write(f"Deployment frequency: {frequency}")

    # Display the selected application's data in a table
    st.dataframe(df)
