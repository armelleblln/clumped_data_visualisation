import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title='Import',
    page_icon='📥'
)

# Title
st.title("Upload your own .xlsx data")

# Upload Excel file
st.session_state["uploaded_file"] = st.file_uploader("Upload an Excel file", type=["xlsx"])

if st.session_state["uploaded_file"] is not None:
    # Read the uploaded Excel file into a DataFrame
    df = pd.read_excel(st.session_state["uploaded_file"])

    # Display the data
    st.write("Uploaded Data:")
    st.write(df)


    st.write("Table with targeted parameters:")
    df=df[["Run","Sample","d45","d45 SD","d46", "d46 SD", "d47", "d47 SD", "d48", "d48 SD", "d49",
       "d49 SD", "D47 (raw)", "D47 SD (raw)", "D48 (raw)", "D48 SD (raw)", "D49 (raw)",
           "d49 SD (raw)", "d13C", "d13C SD", "d18O", "d18O SD", "Magazine", "Weight",
     "Leak", "p no Acid", "pCO2", "VM1", "Init. Int"]]
    st.dataframe(df)

    samples = df["Sample"].unique()

    selected = st.multiselect("Select sample(s)", samples)

    if len(selected) != 0:
        df = df.loc[df['Sample'].isin(selected)]

    # parameter_list = df.columns.tolist()[6:33]
    # st.selectbox('select parameter',[parameter_list])

    x = st.selectbox('x-axis', df.keys())  # df.columns.tolist()[27:80])
    y = st.selectbox('y-axis', df.keys())  # df.columns.tolist()[27:80])

    fig = px.scatter(df,
                     x=x,
                     y=y,
                     color="Sample",
                     hover_data=["Run", "d47", 'Weight', 'pCO2'])
    st.plotly_chart(fig,
                    # theme=None,
                    use_container_width=True)






