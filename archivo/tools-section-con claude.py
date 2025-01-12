# Agregar esto en configurar_pantalla2() después del área de copiado

def mostrar_herramientas_recomendadas():
    st.header("🛠️ Herramientas Recomendadas")
    
    # DALL·E
    with st.expander("DALL·E (OpenAI)", expanded=True):
        st.markdown("""
            - Herramienta de OpenAI para dibujar imágenes con inteligencia artificial
            - Permite creaciones artísticas y composiciones realistas
            - Ideal para prompts detallados y resultados consistentes
            """)
    
    # MidJourney
    with st.expander("MidJourney"):
        st.markdown("""
            - Reconocida por su calidad artística excepcional
            - Estética muy cuidada en las imágenes generadas
            - Excelente para estilos artísticos específicos
            """)
    
    # Stable Diffusion
    with st.expander("Stable Diffusion"):
        st.markdown("""
            - Ideal para personalización y modificaciones detalladas
            - Permite ajuste fino de parámetros
            - Gran comunidad y recursos disponibles
            """)
    
    # Grok
    with st.expander("Grok (Twitter/X)"):
        st.markdown("""
            - Conectá tus imágenes con las tendencias más actuales
            - Integración directa con redes sociales
            - Análisis de tendencias en tiempo real
            """)
    
    # Claude
    with st.expander("Claude"):
        st.markdown("""
            - Ideal para analizar y mejorar prompts complejos
            - Se integra con chatbots IA
            - Excelente para refinamiento de descripciones
            """)
    
    # Copilot
    with st.expander("Copilot"):
        st.markdown("""
            - Soporte creativo para generación rápida
            - Versátil para contenido y prompts
            - Buena integración con flujos de trabajo existentes
            """)
    
    st.info("💡 Cada herramienta tiene sus fortalezas particulares. Te recomendamos probar varias para encontrar la que mejor se adapte a tu proyecto específico.")