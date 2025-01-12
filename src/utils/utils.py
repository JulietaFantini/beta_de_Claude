import streamlit as st

def configurar_sidebar():
    """
    Configuración unificada de la barra lateral educativa
    """
    with st.sidebar:
        st.title("Guía de Prompts")
        
        with st.expander("Cómo crear prompts efectivos"):
            st.markdown("""
            ### Reglas Básicas
            1. Sé específico en cada descripción
            2. Define el estilo visual claramente
            3. Especifica el propósito
            4. Incluye detalles técnicos relevantes
            5. Evitá términos genéricos como "bonito" o "interesante"

            #### Ejemplo Práctico
            ✅ "Fotografía profesional de un café acogedor al atardecer, con luz cálida entrando por ventanales"
            ❌ "Una foto de un café"
            """)

        with st.expander("Aprende a generar prompts"):
            st.markdown("""
            ### Proceso Básico
            1. Define tu idea principal
            2. Elegí el tipo de imagen
            3. Especificá el propósito
            4. Ajustá detalles técnicos

            #### Tips Prácticos
            - Comenzá con lo general y afiná los detalles
            - Revisá la coherencia entre estilo y propósito
            """)

        with st.expander("Documentación detallada"):
            st.markdown("""
            ### Referencia Técnica
            - Términos clave y conceptos fundamentales
            - Preguntas frecuentes
            - Detalles del desarrollo
            """)

def validar_session_state():
    """
    Inicializa y valida el estado de la sesión
    """
    if "params" not in st.session_state:
        st.session_state.params = {}
    
    if "pantalla_actual" not in st.session_state:
        st.session_state.pantalla_actual = "pantalla1"

def mostrar_herramientas():
    """
    Muestra la sección de herramientas recomendadas
    """
    st.header("🛠️ Herramientas Recomendadas")
    
    herramientas = {
        "DALL·E (OpenAI)": "Herramienta de OpenAI para dibujar imágenes con IA. Ideal para creaciones artísticas y composiciones realistas.",
        "MidJourney": "Reconocida por su calidad artística y estética muy cuidada en las imágenes generadas.",
        "Stable Diffusion": "Ideal para personalización y modificaciones detalladas de prompts.",
        "Grok (Twitter/X)": "Conectá tus imágenes con las tendencias más actuales en redes sociales.",
        "Claude": "Ideal para analizar y mejorar prompts complejos, integrándose con chatbots IA.",
        "Copilot": "Soporte creativo para generación rápida y versátil de contenido y prompts."
    }
    
    for nombre, descripcion in herramientas.items():
        with st.expander(nombre):
            st.markdown(descripcion)