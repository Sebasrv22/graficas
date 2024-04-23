#importamos la biblioteca streamlit
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

#creamos el título de la app
st.title("Mi primera App")
st.header("Demo Titanic App")
st.write("Graficas del dataset")

titanic_link = '/Users/sebastianromero/Desktop/graficas/Titanic.csv'
titanic_data =pd.read_csv(titanic_link)
st.dataframe(titanic_data)

fig, ax = plt.subplots()
ax.hist(titanic_data["Fare"])
st.header("Histograma del Titanic")
st.pyplot(fig)

