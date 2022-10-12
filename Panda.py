import numpy as np
import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh



st.set_page_config(page_title="Environment",
                   page_icon=":bar_chart:",
                   layout="wide",
                   )



#"C:/Users/Nikol/Onedrive/Dokumenter/dataxlsx.xlsx"
#"C:\Users\Nikol\OneDrive\Dokumenter\dataxlsx.xlsx"




df = pd.read_excel("dataxlsx.xlsm",
                   sheet_name='Data ind',
                   parse_dates=[0],
                   index_col=[0],
                   header=6,
                   usecols='A:D',
                   nrows=100,
                   )


CH1 = pd.read_excel("dataxlsx.xlsm",
                   sheet_name='Data ind',
                   header=3,
                   usecols='B:B',
                   nrows=1,
                   )


Temp = np.mean(df['CH1'])
Gas = np.mean(df['CH3'])
Humidty = np.mean(df['CH2'])



count = st_autorefresh(interval=1000, limit=100)

kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric(label="Temperatur", value=round(Temp))
kpi2.metric(label="Gas i luften", value=round(Gas))
kpi3.metric(label="Luftfugtighed", value=round(Humidty))

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

with tab1:
   st.header("Chart")
   st.line_chart(df)

with tab2:
   st.header("data")
   st.dataframe(df)









# ---Sidebar---
#st.sidebar.header("EXTRA")
