from pathlib import Path

import pandas as pd
import streamlit as st

datos = pd.read_csv(Path(__file__).with_name("market_data_proc.csv"), parse_dates=["TIME"])

col1, col2, col3, col4 = st.columns(4)
col1.metric("Operaciones", f"{len(datos):,}")
col2.metric("Valores", datos["VALOR"].nunique())
col3.metric("Volumen total", f"{datos['VOLUMEN'].sum():,}")
col4.metric("Media precio all operations", f"{datos['PRECIO'].mean():.2f}")

st.dataframe(datos.head(100), hide_index=True)
st.bar_chart(datos.groupby("VALOR")["VOLUMEN"].sum())

st.subheader("Precio de SAN")
st.line_chart(datos[datos["VALOR"] == "SAN"], x="TIME", y="PRECIO")

st.subheader("Precio de TEF")
st.line_chart(datos[datos["VALOR"] == "TEF"], x="TIME", y="PRECIO")

st.subheader("Operaciones por hora")
operaciones_por_hora = datos["TIME"].dt.hour.value_counts().sort_index()
st.bar_chart(operaciones_por_hora, x_label="Hora", y_label="Operaciones")

st.subheader("10 operaciones de mayor volumen")
st.dataframe(datos.nlargest(10, "VOLUMEN"), hide_index=True)
