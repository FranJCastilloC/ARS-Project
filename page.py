import streamlit as st
from modulos.EDE import run as run_EDE

def main():
    st.set_page_config(layout="wide")
    st.sidebar.title("Menú")
    opcion = st.sidebar.radio(
        "Selecciona un módulo",
        ("Análisis Exploratorio de Datos", "Correlación de Datos", "Modelo", "Base de datos")
    )

    if opcion == "Análisis Exploratorio de Datos":
        run_EDE()
    elif opcion == "Correlación de Datos":
        run_correlacion_datos()
    elif opcion == "Modelo":
        run_modelo()
    elif opcion == "Base de datos":
        run_base_datos()

if __name__ == "__main__":
    main()
