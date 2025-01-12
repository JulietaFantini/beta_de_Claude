import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

def main():
    # Configuración inicial
    st.set_page_config(
        page_title="Generador de Prompts con IA",
        page_icon="🎨",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Estilos CSS
    st.markdown("""
        <style>
        /* Contenedor principal */
        .main {
            background-color: #F8F6FF;
            padding: 1rem;
        }
        
        /* Botones */
        .stButton>button {
            background-color: #6B46C1 !important;
            color: white !important;
            border-radius: 8px;
            padding: 0.5rem 2rem !important;
            border: none;
            font-family: monospace;
        }
        
        /* Campos de texto */
        .stTextInput>div>div>input, .stTextArea>div>textarea {
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
        }
        
        /* Contenedores de ejemplos */
        .example-container {
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }
        
        .good-example {
            background-color: #E6F4EA;
        }
        
        .bad-example {
            background-color: #FCE8E8;
        }
        
        /* Texto de ayuda */
        .help-text {
            color: #4A5568;
            font-size: 0.9rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Control de pasos
    if 'step' not in st.session_state:
        st.session_state.step = 1
        st.session_state.idea = ""
        st.session_state.tipo = ""
        st.session_state.estilo = ""

    # Barra de progreso
    progress = (st.session_state.step - 1) / 3
    st.progress(progress)
    
    # Título con color personalizado
    colored_header(
        label=f"Paso {st.session_state.step} de 4",
        description="Creá tu prompt perfecto",
        color_name="violet-70"
    )

    add_vertical_space(2)

    # Contenido principal
    with st.container():
        if st.session_state.step == 1:
            st.markdown("### 💭 Tu idea inicial")
            
            idea = st.text_area(
                "¿Qué imagen tenés en mente?",
                value=st.session_state.idea,
                placeholder="Ej: Una ciudad futurista flotando entre nubes coloridas...",
                height=150
            )
            
            # Ejemplos
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("""
                    <div class="example-container good-example">
                        <strong>✨ Buen ejemplo</strong><br>
                        Una fotografía en primer plano de un café humeante al atardecer, con luz cálida entrando por ventanales
                    </div>
                    """, unsafe_allow_html=True)
                    
            with col2:
                st.markdown("""
                    <div class="example-container bad-example">
                        <strong>📝 Para mejorar</strong><br>
                        Una foto de un café
                    </div>
                    """, unsafe_allow_html=True)
            
            if st.button("Continuar →"):
                st.session_state.idea = idea
                st.session_state.step += 1
                st.experimental_rerun()

        elif st.session_state.step == 2:
            st.markdown("### 🎨 Estilo y tipo")
            
            tipo = st.selectbox(
                "Tipo de imagen",
                ["", "Fotografía", "Ilustración", "Render 3D", "Arte Digital"],
                index=0,
                key="tipo_select"
            )
            
            estilo = st.selectbox(
                "Estilo artístico",
                ["", "Realista", "Minimalista", "Fantástico", "Surrealista"],
                index=0,
                key="estilo_select"
            )
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("← Atrás"):
                    st.session_state.step -= 1
                    st.experimental_rerun()
            with col2:
                if st.button("Continuar →"):
                    st.session_state.tipo = tipo
                    st.session_state.estilo = estilo
                    st.session_state.step += 1
                    st.experimental_rerun()

    # Sidebar educativo
    with st.sidebar:
        st.title("Guía de Prompts")
        
        with st.expander("✨ Tips Básicos", expanded=True):
            st.write("""
            1. Sé específico en la descripción
            2. Define el estilo visual
            3. Especifica el propósito
            4. Incluye detalles técnicos
            """)
        
        with st.expander("📖 Ejemplos por categoría"):
            st.write("""
            **Fotografía:**
            - Retrato en primer plano con iluminación dramática
            - Paisaje urbano nocturno con luces de neón
            
            **Ilustración:**
            - Personaje cartoon en estilo minimalista
            - Escena fantástica con elementos flotantes
            """)
            
        with st.expander("❓ Ayuda"):
            st.write("""
            Si necesitás ayuda adicional:
            1. Revisá los ejemplos de la derecha
            2. Usá los tips como guía
            3. Experimentá con diferentes combinaciones
            """)

if __name__ == "__main__":
    main()
