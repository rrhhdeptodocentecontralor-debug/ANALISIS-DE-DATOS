import streamlit as st
import pandas as pd

def cargar_datos():
    archivo = st.sidebar.file_uploader("📂 Cursos", type=["xlsx"])
    archivo_doc = st.sidebar.file_uploader("👨‍🏫 Docentes", type=["xlsx"])

    if archivo and archivo_doc:
        df = pd.read_excel(archivo)
        df_doc = pd.read_excel(archivo_doc)
        return df, df_doc

    return None, None