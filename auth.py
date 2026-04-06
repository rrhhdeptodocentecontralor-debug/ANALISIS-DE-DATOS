import streamlit as st

def login_ui():
    st.sidebar.title("🔐 Acceso")
    user = st.sidebar.text_input("Usuario")
    pwd = st.sidebar.text_input("Contraseña", type="password")

    if st.sidebar.button("Ingresar"):
        if user == "admin" and pwd == "admin123":
            return user
        else:
            st.error("Credenciales incorrectas")

    return None