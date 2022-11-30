import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Software Delivery Performance",
                   page_icon=":bar_chart:", layout="wide"
)
st.title("Software Delivery Performance")
st.markdown("##")

df = pd.read_excel(
       io='testPython.xlsx',
       engine='openpyxl',
       sheet_name='Test',
       #skiprows=3,
       usecols='A:D',
       nrows=10,

)


# ----- SIDEBAR -------
#st.sidebar.header("Please Filter Here")
#freq = st.sidebar.multiselect(
#       "select Freq",
#       options=df["Freq"].unique(),
#       default=df["Freq"].unique()
#)

#df_selection = df.query("Freq==@freq")

st.dataframe(df)