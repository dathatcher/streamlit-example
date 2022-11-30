import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="DevOps",
                   page_icon=":bar_chart:", layout="wide"
)
st.title("Research Exchange")
st.header("Current Software Delivery Performance")
st.markdown("##")

df1 = pd.read_excel(
       io='testPython.xlsx',
       engine='openpyxl',
       sheet_name='Test',
       #skiprows=3,
       usecols='A:C',
       nrows=4,
)
def get_data_from_excel():
    df = pd.read_excel(
        io="testPython.xlsx",
        engine="openpyxl",
        sheet_name="Test",
       #skiprows=3,
        usecols="D",
        nrows=6,
    )
    
    return df

# ----- SIDEBAR -------
#st.sidebar.header("Please Filter Here")
#freq = st.sidebar.multiselect(
#       "select Freq",
#       options=df["Freq"].unique(),
#       default=df["Freq"].unique()
#)

#df_selection = df.query("Freq==@freq")

st.dataframe(df1)

#st.title("Deployments (Last 4 Weeks)")
st.header("# Deployments (Last 4 Weeks)")
st.markdown("""---""")

df = get_data_from_excel()
st.line_chart(df)

