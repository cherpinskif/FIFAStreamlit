import streamlit as st
import pandas as pd
import os
import re
from datetime import datetime

st.set_page_config(layout='wide')

if 'data' not in st.session_state:
    year = ['17','18','19','20','21','22','23']
    select_year = st.sidebar.selectbox("Selecione o ano que você deseja?",year)
    df_times = pd.read_csv(r'datasets/CLEAN_FIFA'+select_year+'_official_data.csv',index_col=0)
    df_times = df_times[df_times["Contract Valid Until"] >= datetime.today().year]
    df_times = df_times[df_times["Value(£)"] > 0]
    df_times = df_times.sort_values(by="Overall", ascending=False)
    st.session_state['data'] = df_times

st.markdown("# FIFA23 OFFICIAL DATASET! ⚽️")
st.sidebar.markdown("Desenvolvido por [Felipe Cherpinski - Aluno: Asimov Academy](https://asimov.academy)")


btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes. 
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.
"""
)



