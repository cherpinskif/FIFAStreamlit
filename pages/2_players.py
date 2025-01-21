import streamlit as st
import pandas as pd
import os
import re

st.set_page_config(layout='wide')

df_data = st.session_state['data']

arquivos = os.getcwd()+r"\datasets"
lista = os.listdir(arquivos)
lista = [listas for listas in lista]
year = []
for x in lista:
    x = re.findall("\d+",x)
    year.extend(x)

select_year = st.sidebar.selectbox("Selecione o ano que você deseja?",year)

df_times = pd.read_csv(arquivos+'\\CLEAN_FIFA'+str(select_year)+'_official_data.csv',index_col=0)

select_times = st.sidebar.selectbox("Selecione o time", df_times['Club'].unique())

select_jogadores = st.sidebar.selectbox("Selecione o jogador",df_times[df_times['Club'] == select_times]['Name'])
foto_jogador = st.image(set(df_times[df_times['Name'] == select_jogadores]['Photo']))
markdown_nome_jogador = st.markdown(f"## {select_jogadores}")

clube_jogador = st.write(f"**Clube:** {list(df_times[df_times['Name'] == select_jogadores]['Club'])[0]}")
posicao_jogador = st.write(f"**Posição:** {list(df_times[df_times['Name'] == select_jogadores]['Position'])[0]}")

col11, col12, col13 = st.columns([0.05,0.05,0.15])
col11.write(f"**Idade:** {list(df_times[df_times['Name'] == select_jogadores]['Age'])[0]}")
col12.write(f"**Altura:** {list(df_times[df_times['Name'] == select_jogadores]['Height(cm.)']/100)[0]:.2f} m")
col13.write(f"**Peso:** {list(df_times[df_times['Name'] == select_jogadores]['Weight(lbs.)'])[0]*0.453:.2f} Kg")
st.divider()

overall_jogador = list(df_times[df_times['Name'] == select_jogadores]['Overall'])[0]
subheader_overall_jogador = st.subheader(f"Overall {overall_jogador}")
progress_bar_overall_jogador = st.progress(overall_jogador)

try:
    col21, col22, col23 = st.columns([0.05,0.05,0.15])
    valor_de_mercado_jogador = list(df_times[df_times['Name'] == select_jogadores]['Value(£)'])[0]
    col21.metric("Valor de Mercado",f"$ {valor_de_mercado_jogador:,.2f}")
    remuneracao_semanal_jogador = list(df_times[df_times['Name'] == select_jogadores]['Wage(£)'])[0]
    col22.metric("Remuneração Semanal",f"$ {remuneracao_semanal_jogador:,.2f}")
    clausula_rescisao = list(df_times[df_times['Name'] == select_jogadores]['Release Clause(£)'])[0]
    col23.metric("Cláusula de Rescisão",f"$ {clausula_rescisao:,.2f}")
except:
     col23.metric("Cláusula de Rescisão","Não há dados para esse ano")