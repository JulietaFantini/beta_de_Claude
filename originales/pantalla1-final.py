import streamlit as st
from utils import validar_session_state

def configurar_pantalla1():
    validar_session_state()
    
    st.title("Creador de imágenes con IA")
    st.markdown("Herramienta para diseñar imágenes únicas y generar descripciones efectivas para IA.")

    with st.container():
        st.header("1. Idea Inicial")
        idea = st.text_area(
            "¿Qué imagen tenés en mente?",
            placeholder="Ej: Ciudad futurista flotando entre nubes al atardecer",
            height=100
        )
    
    col1, col2 = st.columns(2)
    with col1:
        tipo_imagen = st.selectbox(
            "2. Tipo de imagen",
            ["Fotografía", "Ilustración", "Render 3D", "Arte Digital", "Otro"]
        )
        if tipo_imagen == "Otro":
            tipo_personalizado = st.text_input("Especificá el tipo:")

    with col2:
        estilo = st.selectbox(
            "3. Estilo artístico",
            ["Realista", "Minimalista", "Artístico", "Futurista", "Vintage", "Otro"]
        )
        if estilo == "Otro":
            estilo_personalizado = st.text_input("Especificá el estilo:")

    st.header("4. Características Técnicas")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        iluminacion = st.selectbox("Iluminación", 
            ["Natural (Luz día)", "Artificial", "Dramática", "Ambiental", "Nocturna"])
    
    with col2:
        plano = st.selectbox("Plano",
            ["General (Todo el contexto)", "Primer plano", "Plano medio", "Plano detalle"])
    
    with col3:
        composicion = st.selectbox("Composición",
            ["Centrada", "Regla de tercios", "Simétrica", "Dinámica"])

    col4, col5 = st.columns(2)
    with col4:
        resolucion = st.selectbox("Resolución",
            ["Redes Sociales (1080x1080)", "Web (1920x1080)", "Móvil (750x1334)", "Alta Calidad (4K)"])
    
    with col5:
        acabado = st.selectbox("Acabado",
            ["Natural", "Suavizado", "Detallado", "Artístico"])

    st.session_state.params = {
        "idea_inicial": idea,
        "tipo_imagen": tipo_personalizado if tipo_imagen == "Otro" else tipo_imagen,
        "estilo_artistico": estilo_personalizado if estilo == "Otro" else estilo,
        "iluminacion": iluminacion,
        "plano": plano,
        "composicion": composicion,
        "resolucion": resolucion,
        "acabado": acabado
    }

    if st.button("Generar Prompt →", use_container_width=True):
        st.session_state.pantalla_actual = "pantalla2"
        st.experimental_rerun()