import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('census.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('India Ka Data Viz')
selected_state = st.sidebar.selectbox('Select a state',list_of_states)

selected_primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))

selected_secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted((df.columns[5:])))

plot = st.sidebar.button('Plot Graph')

if plot:
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df,lat = 'Latitude', lon = 'Longitude', zoom = 4, size_max=30,
                                size = selected_primary, color= selected_secondary, mapbox_style='carto-positron',
                                width = 1200, height = 700 #, color_continuous_scale=[[0, 'red'], [0.5, 'rgb(0, 0, 255)'],[1, 'green']]
                                , hover_name='District')
        st.plotly_chart(fig, use_container_width=True)
    else:
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', zoom=6, size_max=25,
                                size=selected_primary, color=selected_secondary, mapbox_style='carto-positron',
                                width=1200, height=700
                                #,color_continuous_scale=[[0, 'red'], [0.5, 'rgb(0, 0, 255)'], [1, 'green']]
                                ,hover_name='District')
        st.plotly_chart(fig, use_container_width=True)