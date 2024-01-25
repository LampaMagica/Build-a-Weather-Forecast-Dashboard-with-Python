import streamlit as st
import plotly.express as px
import pandas as pd

st.header('In Search for Happiness')
x_axis = st.selectbox('Select the data for the X-axis',('gdp','happiness','generosity'))
y_axis = st.selectbox('Select the data for the Y-axis',('gdp','happiness','generosity'))

st.title(f'{x_axis} and {y_axis}')

df = pd.read_csv('student_side_mini_project\happy.csv')


x = df[x_axis]
y = df[y_axis]

figure = px.scatter(x=x,y=y,labels={'x':x_axis,"y":y_axis})

st.plotly_chart(figure)
