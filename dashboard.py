import streamlit as st

def panel_directivo(df):
    st.subheader("🏛️ Panel Directivo")

    total = len(df)
    alumnos = df["Cursos/Alumnos activos"].sum() if "Cursos/Alumnos activos" in df.columns else 0

    col1, col2 = st.columns(2)
    col1.metric("Cursos", total)
    col2.metric("Alumnos", int(alumnos))