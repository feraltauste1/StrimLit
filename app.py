import os
from io import BytesIO

import boto3
import pandas as pd
import streamlit as st

bucket = os.environ["BUCKET"]
s3 = boto3.client("s3")
objeto = s3.get_object(Bucket=bucket, Key="csv/market_data_proc.csv")
datos = pd.read_csv(BytesIO(objeto["Body"].read()), parse_dates=["TIME"])

san = datos[datos["VALOR"] == "SAN"]

st.title("Operaciones de SAN")
col1, col2 = st.columns(2)
col1.metric("Operaciones", len(san))
col2.metric("Precio medio", f"{san['PRECIO'].mean():.4f}")