import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.io
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





count = st_autorefresh(interval=1000, limit=100)

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "")
col2.metric("Gas", " ")
col3.metric("Humidity", " ")

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

with tab1:
   st.header("Chart")
   st.line_chart(df)

with tab2:
   st.header("data")
   st.dataframe(df)









# ---Sidebar---
#st.sidebar.header("EXTRA")
