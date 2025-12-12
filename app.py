import streamlit as st
import datetime
import pandas as pd
import os
import csv

def load_trips_data_simple(file_path):

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return pd.DataFrame()
    try:
        df = pd.read_csv(file_path)
        df["Trip", "Stopped Time", "Moving Time", "Total Fare"] = pd.to_numeric(df["Trip", "Stopped Time", "Moving Time", "Total Fare"], errors="coerce")
        return df
    except Exception as e:
        st.warning(f"Error al leer el CSV: {e}. Se cargará un historial vacío.")
        return pd.DataFrame()


st.set_page_config(
    page_title="Taxímetro",
    page_icon=":oncoming_taxi:",
    layout="wide"
)

st.title(":oncoming_taxi: Taximetro")
st.write("Bienvenido a tu viaje intergaláctico")

# Secciones principales
# -------------------
tab_taxi, tab_grafica = st.tabs([
    "Taxi",
    "Gráfica"
])

with tab_grafica:
    st.subheader("Datos del grupo")
    st.dataframe(df, width="stretch")