import streamlit as st

pg_intro = st.Page('intro.py', title='Introducción')
pg_eda_intro = st.Page('seccion_eda/introduccion.py', title='Primeros Pasos')

navigation_env = st.navigation(
    {
        '''''': [pg_intro],
        '''EDA''': [pg_eda_intro]
    }
)

pg_intro.run()
