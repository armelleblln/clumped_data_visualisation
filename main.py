import os

import pandas as pd
import plotly.express as px
import streamlit as st



st.set_page_config(
    page_title='Home',
    page_icon=':home:'
)

#from tools import authenticator
#if not authenticator.check_password():
 #   st.stop()  # Do not continue if check_password is not True.


st.title("Quick and easy clumped isotope (𝚫45-49) data visualization")
#st.header("Hi! Let's visualize data together:", divider='rainbow')
st.header("Let's visualize data together:", divider='rainbow')
st.write("Page created in October 2023 by Armelle Ballian | Senckenberg Climate and Biodiversity Research Centre; "
         "Goethe University, Frankfurt am Main (Germany)")

#from tools import authenticator
#if not authenticator.check_password():
#   st.stop()  # Do not continue if check_password is not True.

st.write("The following template table contains raw data extracted from the Easotope software:")

file_name_list = []
for i in os.listdir():
    if i.endswith('csv'):
        file_name_list.append(i)

st.write(file_name_list)
st.write("Table with raw data:")
df = pd.read_excel('Sample_data.xlsx')
st.dataframe(df)

st.write("Table with targeted parameters:")
df=df[["Run","Sample","d45","d45 SD","d46", "d46 SD", "d47", "d47 SD", "d48", "d48 SD", "d49",
       "d49 SD", "D47 (raw)", "D47 SD (raw)", "D48 (raw)", "D48 SD (raw)", "D49 (raw)",
       "d49 SD (raw)", "d13C", "d13C SD", "d18O", "d18O SD", "Magazine", "Weight",
       "Leak", "p no Acid", "pCO2", "VM1", "Init. Int"]]
st.dataframe(df)
#df = df.loc[~(df['Excl.']=="X")]
#df = df.loc[(df['Excl.'].isna())]
#st.dataframe(df)



samples = df["Sample"].unique()

selected = st.multiselect("Select sample(s)", samples, key="selected_samples")

if len(selected) != 0:
    df = df.loc[df['Sample'].isin(selected)]

#parameter_list = df.columns.tolist()[6:33]
#st.selectbox('Parameters ',[parameter_list])

x = st.selectbox('x-axis', df.keys()) #df.columns.tolist()[27:80])
y = st.selectbox('y-axis', df.keys()) #df.columns.tolist()[27:80])

fig = px.scatter(df,
                 x=x,
                 y=y,
                 color= "Sample",
                 hover_data=["Run","d47",'Weight', 'pCO2'])
st.plotly_chart(fig,
                theme=None,
                use_container_width=True)

st.dataframe(df)

st.write("Table with targeted parameters:")
df=df[["Run","Sample","d45","d45 SD","d46", "d46 SD", "d47", "d47 SD", "d48", "d48 SD", "d49",
       "d49 SD", "D47 (raw)", "D47 SD (raw)", "D48 (raw)", "D48 SD (raw)", "D49 (raw)",
       "d49 SD (raw)", "d13C", "d13C SD", "d18O", "d18O SD", "Magazine", "Weight",
       "Leak", "p no Acid", "pCO2", "VM1", "Init. Int"]]
st.dataframe(df)
#df = df.loc[~(df['Excl.']=="X")]
#df = df.loc[(df['Excl.'].isna())]
#st.dataframe(df)


st.write("contact: armelle.ballian@senckenberg.de")