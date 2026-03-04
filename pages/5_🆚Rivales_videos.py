import pandas as pd
import streamlit as st


df_matches = pd.read_excel('Matches.xlsx')
df_matches = df_matches.dropna(subset=['video'])

df_matches = df_matches[df_matches.Propio==False]


jornada = set(df_matches['jornada'].values)

jornada_select = st.sidebar.multiselect(
    "Elige la jornada",
    jornada,
    jornada)

df_matches = df_matches[df_matches['jornada'].isin(jornada_select)]
urls_match = df_matches['video'].values

#df_matches = df_matches[df_matches['match_filter'].isin(partidos_select)]
n_matches = df_matches.shape[0]
n_columns = 3
for i in range(0, n_matches, n_columns):
    cols = st.columns(n_columns)
    for j in range(n_columns):
        if i + j < n_matches:
            cols[j].video(urls_match[i + j], muted=0)