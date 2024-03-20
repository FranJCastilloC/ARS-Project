import streamlit as st
from modulos.analisis_exploratorio import run as run_analisis_exploratorio
from modulos.correlacion_datos import run as run_correlacion_datos
from modulos.modelo import run as run_modelo
from modulos.base_datos import run as run_base_datos

def main():
    st.set_page_config(layout="wide")
    st.sidebar.title("Menú")
    opcion = st.sidebar.radio(
        "Selecciona un módulo",
        ("Análisis Exploratorio de Datos", "Correlación de Datos", "Modelo", "Base de datos")
    )

    if opcion == "Análisis Exploratorio de Datos":
        run_analisis_exploratorio()
    elif opcion == "Correlación de Datos":
        run_correlacion_datos()
    elif opcion == "Modelo":
        run_modelo()
    elif opcion == "Base de datos":
        run_base_datos()

if __name__ == "__main__":
    main()
