import streamlit as st
from auth import login_ui
from dashboard import panel_directivo
from data_loader import cargar_datos

st.set_page_config(layout="wide")
st.title("🏛️ Sistema Académico Institucional PRO")

usuario = login_ui()
if not usuario:
    st.stop()

df, docentes = cargar_datos()
if df is None:
    st.warning("Cargar datos para comenzar")
    st.stop()

menu = st.sidebar.selectbox("Módulos", [
    "Panel Directivo"
])

if menu == "Panel Directivo":
    panel_directivo(df)