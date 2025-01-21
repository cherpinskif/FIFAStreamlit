import streamlit as st
import pandas as pd
import os
import re
from datetime import datetime

st.set_page_config(layout='wide')

df_data = st.session_state['data']

year = ['17','18','19','20','21','22','23']
select_year = st.sidebar.selectbox("Selecione o ano que você deseja?",year)
df_times = pd.read_csv(r'datasets/CLEAN_FIFA'&year&'_official_data.csv',index_col=0)
df_times = df_times[df_times["Contract Valid Until"] >= datetime.today().year]
df_times = df_times[df_times["Value(£)"] > 0]
df_times = df_times.sort_values(by="Overall", ascending=False)

select_clube = st.sidebar.selectbox("Clube",df_times["Club"].unique())

df_times_selecionado = df_times[(df_times['Club'] == select_clube)].set_index('Name')
logo_do_time = st.image(df_times_selecionado.iloc[0]['Club Logo'],width=50)
st.markdown(f"## {select_clube}")

try:
    columns = ["Age","Photo","Flag","Overall","Value(£)","Wage(£)","Joined","Height(cm.)","Weight(lbs.)","Contract Valid Until","Release Clause(£)"]
    df_times_filtrado = st.dataframe(df_times_selecionado[columns],column_config={"Overall":st.column_config.ProgressColumn("Overall",format="%d"),"Photo":st.column_config.ImageColumn(),"Wage(£)":st.column_config.ProgressColumn("Weekly Wage",format="£%f",min_value=0,max_value=df_times_selecionado["Wage(£)"].max()),"Flag":st.column_config.ImageColumn()})
except:
    columns = ["Age","Photo","Flag","Overall","Value(£)","Wage(£)","Joined","Height(cm.)","Weight(lbs.)","Contract Valid Until"]
    df_times_filtrado = st.dataframe(df_times_selecionado[columns],column_config={"Overall":st.column_config.ProgressColumn("Overall",format="%d"),"Photo":st.column_config.ImageColumn(),"Wage(£)":st.column_config.ProgressColumn("Weekly Wage",format="£%f",min_value=0,max_value=df_times_selecionado["Wage(£)"].max())})
