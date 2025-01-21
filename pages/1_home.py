import streamlit as st
import pandas as pd
import os
import re
from datetime import datetime

st.set_page_config(layout='wide')

if 'data' not in st.session_state:
    arquivos = os.getcwd()+r"\datasets"
    lista = os.listdir(arquivos)
    lista = [listas for listas in lista]
    year = []
    for x in lista:
        x = re.findall("\d+",x)
        year.extend(x)
    select_year = st.sidebar.selectbox("Selecione o ano que você deseja?",year)
    df_times = pd.read_csv(arquivos+'\\CLEAN_FIFA'+str(select_year)+'_official_data.csv',index_col=0)
    df_times = df_times[df_times["Contract Valid Until"] >= datetime.today().year]
    df_times = df_times[df_times["Value(£)"] > 0]
    df_times = df_times.sort_values(by="Overall", ascending=False)
    st.session_state['data'] = df_times





