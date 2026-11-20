# 01_hola.py
import pandas as pd
import streamlit as st

st.title("Hola, Streamlit")
st.write("Esto es una aplicación web escrita solo en Python.")
st.markdown("Admite **Markdown**: listas, *cursiva*, `código` y enlaces.")

precios = pd.DataFrame({"VALOR": ["SAN", "TEF"], "PRECIO": [5.41, 8.12]})
st.write(precios)
