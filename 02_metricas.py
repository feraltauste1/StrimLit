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
st.line_chart(datos[datos["VALOR"] == "SAN"], x="TIME", y="PRECIO")
