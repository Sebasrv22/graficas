# Importamos la librería Streamlit
import streamlit as st

# Crear el título para la aplicación web
st.title("Mi Primera App")
st.header ("Sebastián Romero Velasco")
st.write("Titanic gráficas")

import pandas as pd
import streamlit as st
import matplotlib.pyplot as ptl

titanic_link = '/Users/sebastianromero/Desktop/graficas/Titanic.csv'
titanic_data = pd.read_csv(titanic_link)

st.dataframe(titanic_data)
st.header("Data Description")



