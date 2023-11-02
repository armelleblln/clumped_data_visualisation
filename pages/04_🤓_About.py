import streamlit as st

st.set_page_config(page_title='About')

st.header("About this tool and the creator")
st.divider()
st.write("My name is Armelle Ballian (she/her), I am currently a PhD student at the "
         "Senckenberg Climate and Biodiversity Research Centre (Frankfurt am Main, Germany). "
         "My research focuses on stable isotope-based paleoelevation and paleoclimate reconstruction (ẟ18O, ẟD, 𝚫47-𝚫48). "
         "I apply clumped isotope thermometry on pedogenic carbonate nodules and "
         "I perform the lab work at the Joint Goethe University-Senckenberg BiK-F Stable Isotope Facility (Frankfurt am Main, Germany) "
         "on a Kiel IV Carbonate device paired to a MAT253plus IRMS.")
st.write("While I used to spend long enough creating excel files and figures, I got to make my first steps in "
         "coding, and I developed this tool to allow a quick and easy visualization of clumped isotope raw data.")
st.write("Thanks to this tool, you can e.g. have a look at your replicates, "
         "determine preliminary outliers, "
         "calculate the appropriated weight of carbonate for the CO2 reaction... ")
st.write("I hope I made your life a bit easier, enjoy playing around with your data !")
st.divider()


st.write("contact: armelle.ballian@senckenberg.de")