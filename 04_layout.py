# 04_layout.py
from pathlib import Path

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Panel MIAX", layout="wide")   # siempre lo primero

@st.cache_data                     # se ejecuta una vez y guarda el resultado
def cargar_datos():
    return pd.read_csv(Path(__file__).with_name("market_data_proc.csv"), parse_dates=["TIME"])

datos = cargar_datos()
with st.sidebar:                   # barra lateral
    valores = st.multiselect("Valores", ["SAN", "TEF"], default=["SAN"])

grafico, tabla = st.tabs(["Gráfico", "Tabla"])     # pestañas
seleccion = datos[datos["VALOR"].isin(valores) & datos["TIME"].dt.hour.between(9, 17)]
with grafico:
    st.line_chart(seleccion, x="TIME", y="PRECIO", color="VALOR")
with tabla:
    st.dataframe(seleccion)

with st.expander("Sobre los datos"):                 # desplegable
    st.write("Operaciones del 19 de marzo de 2018.")
