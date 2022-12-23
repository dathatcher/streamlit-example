import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("deployments.csv")

# Convert the deployment date column to a datetime object
df['deployment_date'] = pd.to_datetime(df['deployment_date'])

# Calculate the difference in days between each deployment
df['days_between_deployments'] = df['deployment_date'].diff().dt.days

# Create a new column that categorizes the frequency of deployments as either yearly, monthly, weekly, or daily
df['deployment_frequency'] = np.where(df['days_between_deployments'] > 365, 'Yearly',
                                      np.where(df['days_between_deployments'] > 30, 'Monthly',
                                               np.where(df['days_between_deployments'] > 7, 'Weekly', 'Daily')))

# Display the data in a table
st.table(df)

# Calculate the deployment frequency trend over time
deployment_frequency_trend = df.groupby(['deployment_date']).agg({'deployment_frequency': 'first'})

# Plot the deployment frequency trend
plt.plot(deployment_frequency_trend)
plt.xlabel('Deployment Date')
plt.ylabel('Deployment Frequency')

# Display the plot
st.pyplot()