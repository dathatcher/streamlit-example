import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="DevOps",
                   page_icon=":bar_chart:", layout="wide"
)
st.title("Research Exchange")

st.header("Software Delivery Performance")
st.markdown("##")

df1 = pd.read_excel(
       io='testPython.xlsx',
       engine='openpyxl',
       sheet_name='Test',
       #skiprows=3,
       usecols='A:C',
       nrows=4,
)
def get_data_from_excel_df():
    df = pd.read_excel(
        io="testPython.xlsx",
        engine="openpyxl",
        sheet_name="Test",
       #skiprows=3,
        usecols="D:E",
        nrows=6,
    )
    
    return df

def get_data_from_excel_lt():
    df3 = pd.read_excel(
        io="testPython.xlsx",
        engine="openpyxl",
        sheet_name="Test",
       #skiprows=3,
        usecols="F:G",
        nrows=6,
    )
    
    return df3

def get_data_from_excel_mttr():
    df4 = pd.read_excel(
        io="testPython.xlsx",
        engine="openpyxl",
        sheet_name="Test",
       #skiprows=3,
        usecols="H:I",
        nrows=6,
    )
    
    return df4

def get_data_from_excel_cfr():
    df5 = pd.read_excel(
        io="testPython.xlsx",
        engine="openpyxl",
        sheet_name="Test",
       #skiprows=3,
        usecols="J:K",
        nrows=6,
    )
    
    return df5
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
st.header("# Deployments")
st.markdown("""---""")

st.metric("Total Oct. Deployments vs Sep.", "15 Deployments", "-1")

df = get_data_from_excel_df()
st.line_chart(df)

st.header("Lead Time for Change (avg days)")
st.markdown("""---""")

st.metric("Total Oct. avg Lead Time vs Sep", "44 Days", "-9", delta_color="inverse")

df2 = get_data_from_excel_lt()
st.line_chart(df2)

st.header("MTTR (hours)")
st.markdown("""---""")

st.metric("Mean Time to Recover Oct. vs Sep", "0%", "-0%", delta_color="off")

df3 = get_data_from_excel_mttr()
st.line_chart(df3)

st.header("Change Failure Rate")
st.markdown("""---""")

st.metric("", "Change Failure Rate", "-Last 30 Days", delta_color="off")

df4 = get_data_from_excel_cfr()
st.line_chart(df4)