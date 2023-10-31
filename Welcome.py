import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.plotting import figure
#from ipywidgets import interact
import os


st.write('Hello world')

file_name_list = []
for i in os.listdir(): 
  if i.endswith('csv'):
    file_name_list.append(i)

st.write(file_name_list)
  

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)


el_list = df.columns.tolist()[27:80]
st.selectbox('select element',[el_list])

st.multiselect('select location', file_name_list,file_name_list[0]) #add the first location as a default option 




#x = df['Si']
#y = df['Al']
x = st.selectbox('x-axis', el_list) #df.columns.tolist()[27:80])
y = st.selectbox('y-axis', el_list) #df.columns.tolist()[27:80])
p1 = figure(
  x_axis_label=x + ' (wt%)',
  y_axis_label=y + ' (wt%)')
p1.scatter(df[x]/10000, df[y]/10000, legend_label='Trend', size=7)
st.bokeh_chart(p1, use_container_width = True)
