import streamlit as st
import pandas as pd
import os
import re
from datetime import datetime

st.set_page_config(layout='wide')

if 'data' not in st.session_state:
    year = ['17','18','19','20','21','22','23']
    select_year = st.sidebar.selectbox("Selecione o ano que você deseja?",year)
    df_times = pd.read_csv(r'datasets/CLEAN_FIFA'+year+'_official_data.csv',index_col=0)
    df_times = df_times[df_times["Contract Valid Until"] >= datetime.today().year]
    df_times = df_times[df_times["Value(£)"] > 0]
    df_times = df_times.sort_values(by="Overall", ascending=False)
    st.session_state['data'] = df_times





