import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read in the CSV file
@st.cache
def read_data(file):
    df = pd.read_csv(file)
    df['deployment_date'] = pd.to_datetime(df['deployment_date'])
    return df

# Calculate the deployment frequency according to DORA's method
def calculate_frequency(df):
    delta = df['deployment_date'].max() - df['deployment_date'].min()
    days = delta.days + 1
    if days >= 365:
        frequency = 'Yearly'
    elif days >= 30:
        frequency = 'Monthly'
    elif days >= 7:
        frequency = 'Weekly'
    else:
        frequency = 'Daily'
    return frequency

# Plot a trend line of the data
def plot_trend(df):
    plt.plot(df['deployment_date'], df['deployments'])
    plt.xlabel('Date')
    plt.ylabel('Number of Deployments')
    plt.title('Trend of Deployments Over Time')

# Main function
def main():
    # Select the CSV file to load
    file = st.file_uploader('Upload a CSV file of deployment data:')
    if file is not None:
        df = read_data(file)

        # Calculate the deployment frequency
        frequency = calculate_frequency(df)
        st.write(f'The deployment frequency is: {frequency}')

        # Plot the trend line
        st.plotly_chart(plot_trend(df))

if __name__ == '__main__':
    main()