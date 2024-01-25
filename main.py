import streamlit as st
import plotly.express as px
import back_end as be

st.title('Weather forcast for the next days')

place_input = st.text_input(label='Place')

forcast_day = st.slider(label='Forcast days',min_value=1,max_value=5)

data_to_view = st.selectbox(label='Select data to view',options=('Temperature','Weather'))

st.title(f'{data_to_view} for the next {forcast_day} days in {place_input}')

data_all = be.get_data(place_input,forcast_day,data_to_view)

if data_to_view == 'Temperature':
    try:
        temp,days = data_all

        pdt = px.line(x=days, y=temp, labels={'x': 'Days', 'y': 'Temp'})

        st.plotly_chart(pdt)
    except KeyError as e:
        if 'list' in str(e):
            print("KeyError: 'list'")
            print('No data yet passed')
        else:
            raise

if data_to_view == 'Weather':
    num_columns = 6

    columns = st.columns(num_columns)
    
    for i, e in enumerate(data_all):
        # Start a new row for every 6 images
        if i % num_columns == 0:
            columns = st.columns(num_columns)

        with columns[i % num_columns]:
            st.image(image=e['icon'], caption=e['time'])