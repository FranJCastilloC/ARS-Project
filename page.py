import streamlit as st


def main():
    # Configura la página para utilizar todo el ancho disponible
    st.set_page_config(layout="wide")

    # Creación del menú lateral para la navegación
    st.sidebar.title("Menú")
    opcion = st.sidebar.radio(
        "Selecciona un módulo",
        ("Análisis Exploratorio de Datos", "Correlación de Datos", "Modelo", "Base de datos")
    )
  # Asegúrate de que esta función esté definida en alguna parte de tu script

# Asegúrate de definir las funciones mencionadas aquí, como modulo_analisis_exploratorio, modulo_corr, modulo_modelo, y modulo_overview.

if __name__ == "__main__":
    main()