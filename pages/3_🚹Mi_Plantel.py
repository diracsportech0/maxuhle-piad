import streamlit as st
import numpy as np
import pandas as pd
from etl import df, df_pass
from functions import player_passmap,graph_barras, heat_map

#----------------------
df_players_excel = pd.read_excel('players.xlsx')

#OBTENER DATA TOTALIZADA POR JUGADOR
# Agrupar por Partido, Jugador y Evento y contar ocurrencias
grouped = df.groupby(['Rival', 'player', 'Event']).size().reset_index(name='count')
# Pivotar los datos para transformar los eventos en columnas
pivot_table = grouped.pivot_table(index=['Rival', 'player'], columns='Event', values='count', fill_value=0)
# Restablecer el índice para que Partido y Jugador sean columnas nuevamente
df_players_totalstats = pivot_table.reset_index()

#MENU LATERAL
players = set(df_players_totalstats['player'].values)
player = st.sidebar.selectbox(
        "Jugador",
        players,
        0)
df_player = df_players_totalstats[df_players_totalstats.player==player]
n_partidos = 1#df_player.shape[0] #partidos jugados por un futbolista

st.title("🚹 MI PLANTEL")
#--- CONTENIDO INFO BASICA
matching_row = df_players_excel.loc[df_players_excel['player'] == player]
name_player = matching_row['name_complete'].values[0]
apellido = matching_row['surname'].values[0]

#born_player = matching_row['born'].values[0].astype('M8[ms]').astype('O').strftime('%Y/%m/%d')
#min_played = matching_row['min_played'].values[0]
dorsal= matching_row['dorsal'].values[0]
#edad_player = matching_row['edad'].values[0]


# TABLA
df_events_player = df[df.player==player]
metric_off = ['CONDUCCION','PASE','REGATE','TIRO']
metric_def = ['INTERCEPTACION','DUELO', 'DESPEJE','RECUPERACION',
              'PRESION']
#
colA3, colB3, colC3, colD3, colE3= st.columns([3,3,2,5,1])
try:
        with colA3:st.image(f'imgs/{name_player}.jpg', use_column_width=True)
except:
      with colA3:st.image('imgs/perfil.jfif', use_column_width=True)
with colB3:
         st.write('Jugador:', name_player)
         st.write('Posición:', matching_row['position'].values[0])
#        st.write('Nacimiento:', born_player)
         #st.write('Edad:', edad_player)
         st.write('Partidos jugados:', n_partidos)
         st.write('Dorsal:', dorsal)
with colC3: pass
with colE3: pass



