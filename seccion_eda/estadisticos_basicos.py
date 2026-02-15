import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown('''Lorem ipsum''')

df = pd.read_csv('bike_dataset_hour.csv')

st.markdown('''## Datos Crudos del Dataset''')

st.dataframe(df.head(500)) # Cargamos los primeros 500 registros del dataset

st.markdown('''## Datos sobre el Dataset''')

st.dataframe(df.describe().T)

st.markdown('''## Estadísticos''')

st.dataframe(df[['dteday', 'temp', 'windspeed', 'hum', 'cnt']].describe().T[['count', 'mean', 'std']])

st.markdown('''## Distribución de las Variables''')

cols = st.columns(3)
with cols[0]:
    fig, ax = plt.subplots(figsize=(8,5))
    sns.histplot(df['temp'], kde=True)
    plt.title('Distribución de la Temperatura')
    st.pyplot(fig)
with cols[1]:
    fig, ax = plt.subplots(figsize=(8,5))
    sns.histplot(df['hum'], kde=True)
    plt.title('Distribución de la Humedad')
    st.pyplot(fig)
with cols[2]:
    fig, ax = plt.subplots(figsize=(8,5))
    sns.histplot(df['windspeed'], kde=True)
    plt.title('Distribución de la Velocidad del Viento')
    st.pyplot(fig)

st.markdown('''---''')
st.markdown('''## Distribución de la Variable Objetivo''')

cols_target, = st.columns(1)
with cols_target:
    fig, ax = plt.subplots(figsize=(8,5))
    sns.histplot(df['cnt'], kde=True)
    plt.title('Distribución de la Venta de Bicicletas')
    st.pyplot(fig)

st.markdown('''## Matriz de Correlación''')

cols_interes = ['temp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']
matriz_correlacion = df[cols_interes].corr()

col, = st.columns(1)
with col:
    fig, ax = plt.subplots()
    sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Matriz de Correlación con cnt')
    st.pyplot(fig)