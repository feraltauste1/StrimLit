# 03_filtros.py
from turtle import st
import streamlit as st
import pandas as pd

datos = pd.read_csv("market_data_proc.csv", parse_dates=["TIME"])

valor = st.selectbox("Valor", sorted(datos["VALOR"].unique()))
desde, hasta = st.slider("Horas", 9, 17, (9, 17))
volumen_min = st.number_input("Volumen mínimo", min_value=0, value=0, step=100)
solo_grandes = st.checkbox("Solo operaciones de más de 10.000 acciones")

seleccion = datos[(datos["VALOR"] == valor) & datos["TIME"].dt.hour.between(desde, hasta)]
st.line_chart(seleccion, x="TIME", y="PRECIO")

if st.button("Mostrar estadísticas"):      # True solo en la ejecución del clic
    st.write(seleccion[["PRECIO", "VOLUMEN"]].describe())