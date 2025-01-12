import streamlit as st
from src.pantalla1 import configurar_pantalla1
from src.pantalla2 import configurar_pantalla2
from src.utils.utils import configurar_sidebar, validar_session_state

def load_custom_css():
    """Carga los estilos personalizados desde un archivo CSS"""
    with open('assets/styles/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    """
    Punto de entrada principal de la aplicación.
    Maneja la navegación entre Pantalla 1 y Pantalla 2.
    """
    # Configuración inicial de la página
    st.set_page_config(
        page_title="Generador de Prompts con IA",
        page_icon=":art:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Inicializa el estado de la pantalla
    if "pantalla_actual" not in st.session_state:
        st.session_state.pantalla_actual = "pantalla1"

    # Cargar los estilos personalizados desde styles.css
    load_custom_css()

    # Inyectar CSS adicional para anular el estilo predeterminado de Streamlit
    st.markdown(
        """
        <style>
        :root {
            --primary-color: #6B46C1;
            --background-color: #F8F6FF;
            --secondary-background-color: #EEEAF5;
            --text-color: #1A202C;
            --font: "monospace";
        }

        /* Botones personalizados */
        .stButton>button {
            background-color: var(--primary-color) !important;
            color: #FFFFFF !important;
            border-radius: 8px;
            font-size: 16px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #5A3AA9 !important;
        }

        /* Expanders con fondo personalizado */
        [data-testid="stExpander"] {
            background-color: var(--secondary-background-color) !important; 
            border-radius: 8px;
            padding: 10px;
        }

        /* Inputs y labels personalizados */
        [data-testid="stTextInput"] label, [data-testid="stTextArea"] label, 
        [data-testid="stSelectbox"] label, [data-testid="stRadio"] label, [data-testid="stCheckbox"] label {
            font-family: var(--font) !important;
            color: var(--text-color) !important;
        }
        [data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea, 
        [data-testid="stSelectbox"] [role="combobox"], 
        [data-testid="stRadio"] div[data-testid="stMarkdownContainer"],
        [data-testid="stCheckbox"] div[data-testid="stMarkdownContainer"] {
            font-family: var(--font) !important;
        }

        /* Fondo de la página */
        body {
            background-color: var(--background-color) !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Validar session_state
    validar_session_state()

    # Barra lateral educativa
    configurar_sidebar()

    # Funciones de navegación entre pantallas
    def mostrar_pantalla1():
        st.session_state.pantalla_actual = "pantalla1"

    def mostrar_pantalla2():
        st.session_state.pantalla_actual = "pantalla2"

    # Mostrar pantalla correspondiente
    if st.session_state.pantalla_actual == "pantalla1":
        configurar_pantalla1(mostrar_pantalla2)
    else:
        configurar_pantalla2(mostrar_pantalla1)

if __name__ == "__main__":
    main()
