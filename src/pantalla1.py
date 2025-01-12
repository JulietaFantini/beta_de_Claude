import streamlit as st
from src.utils.utils import generar_dropdown, filtrar_valores, validar_errores

def configurar_pantalla1(cambiar_pantalla):
    """
    Configura la Pantalla 1 del generador de prompts.
    """
    if "params" not in st.session_state:
        st.session_state.params = {}

    params = st.session_state.params

    st.title("Creador de imágenes con IA")
    st.markdown(
        "Herramienta para diseñar imágenes únicas y generar descripciones efectivas para IA. Comienza completando los campos obligatorios."
    )

    # Parámetros obligatorios
    st.header("Parámetros Clave")
    st.caption("Campos obligatorios para generar el prompt")

    params = generar_dropdown(
        "Tipo de imagen",
        "Selecciona el tipo de imagen que quieres generar.",
        ["Seleccioná una opción...", "Fotografía", "Ilustración", "Render 3D", "Otro"],
        params
    )

    if params.get("tipo_de_imagen", "").lower() == "otro":
        params["tipo_de_imagen_personalizado"] = st.text_input(
            "Describe el tipo de imagen (ej.: 'Collage surrealista')"
        )

    params["idea_inicial"] = st.text_input(
        "Describe tu idea inicial",
        placeholder="Ejemplo: Una ciudad flotante al amanecer."
    )

    params = generar_dropdown(
        "Estilo artístico",
        "Selecciona un estilo visual para la imagen.",
        ["Seleccioná una opción...", "Arte Digital", "Minimalismo", "Surrealismo", "Otro"],
        params
    )

    if params.get("estilo_artístico", "").lower() == "otro":
        params["estilo_artístico_personalizado"] = st.text_input(
            "Describe tu estilo artístico personalizado"
        )

    # Validar errores
    errores = validar_errores(params)

    # Botón para avanzar
    if st.button("Validar y continuar"):
        if errores:
            st.error("\n".join(errores))
        else:
            st.session_state.params = params
            cambiar_pantalla()

if __name__ == "__main__":
    configurar_pantalla1(lambda: print("Pantalla 2"))
