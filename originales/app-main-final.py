import streamlit as st
from pantalla1 import configurar_pantalla1
from pantalla2 import configurar_pantalla2
from utils import configurar_sidebar, validar_session_state

def main():
    st.set_page_config(
        page_title="Generador de Prompts con IA",
        page_icon="🎨",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    validar_session_state()
    configurar_sidebar()

    if st.session_state.pantalla_actual == "pantalla1":
        configurar_pantalla1()
    else:
        configurar_pantalla2(lambda: setattr(st.session_state, 'pantalla_actual', 'pantalla1'))

if __name__ == "__main__":
    main()