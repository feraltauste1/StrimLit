import pandas as pd
import streamlit as st

if "contador" not in st.session_state:
    st.session_state.contador = 0
if st.button("Sumar"):
    st.session_state.contador += 1
st.write(st.session_state.contador)

fichero = st.file_uploader("Sube un CSV", type="csv")
if fichero is None:
    st.info("Prueba con market_data_proc.csv.")
    st.stop()

try:
    datos = pd.read_csv(fichero)
except (ValueError, pd.errors.ParserError):
    st.error("No se pudo leer el CSV.")
    st.stop()

columnas_requeridas = {"VALOR", "PRECIO", "VOLUMEN"}
if not columnas_requeridas.issubset(datos.columns):
    st.error("El CSV debe incluir las columnas VALOR, PRECIO y VOLUMEN.")
    st.stop()

resumen = datos.groupby("VALOR").agg(
    operaciones=("PRECIO", "size"),
    volumen=("VOLUMEN", "sum"),
)
st.dataframe(resumen)
st.download_button("Descargar resumen", resumen.to_csv(), file_name="resumen.csv", mime="text/csv")
