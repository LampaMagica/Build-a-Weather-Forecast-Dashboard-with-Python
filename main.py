import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import back_end as be

st.title('Weather forcast for the next days')

place_input = st.text_input(label='Place')

forcast_day = st.slider(label='Forcast days',min_value=1,max_value=5)

data_to_view = st.selectbox(label='Select data to view',options=('Temperature','Weather'))

st.title(f'{data_to_view} for the next {forcast_day} days in {place_input}')


try:
    temp,days = be.get_data(place_input,forcast_day)

    pdt = px.line(x=days, y=temp, labels={'x': 'Days', 'y': 'Temp'})

    st.plotly_chart(pdt)
except KeyError as e:
    if 'list' in str(e):
        print("KeyError: 'list'")
        print('No data yet passed')
    else:
        raise
