import streamlit as st
from utils import configurar_sidebar, validar_session_state, mostrar_herramientas

def generar_prompt(params):
    """
    Crea un texto final combinando la idea inicial, tipo de imagen, propósito, 
    estilo y características técnicas.
    """
    frases = []

    # (1) Idea Inicial
    idea = params["idea_inicial"].strip()
    if idea:
        frases.append(f"Imaginá {idea}.")

    # (2) Tipo de Imagen + Estilo Artístico
    if "Otro" in params["tipo_imagen"]:
        tipo = params.get("tipo_imagen_personalizado", "").strip()
    else:
        tipo = params["tipo_imagen"]

    if "Otro" in params["estilo_artistico"]:
        estilo = params.get("estilo_artistico_personalizado", "").strip()
    else:
        estilo = params["estilo_artistico"]

    if tipo and estilo:
        frases.append(f"Se trata de un {tipo.lower()} con un estilo {estilo.lower()}.")
    elif tipo:
        frases.append(f"Se trata de un {tipo.lower()}.")

    # (3) Propósito
    proposito_cat = params.get("proposito_categoria")
    subcat = params.get("proposito_subcategoria", "")
    if "Otro" in proposito_cat:
        proposito_personalizado = params.get("proposito_personalizado", "").strip()
        if proposito_personalizado:
            frases.append(f"Fue creada para {proposito_personalizado.lower()}.")
    else:
        if subcat:
            frases.append(f"Fue creada para {proposito_cat.lower()}, específicamente {subcat.lower()}.")
        else:
            frases.append(f"Fue creada para {proposito_cat.lower()}.")

    # (4) Características Técnicas
    iluminacion = params.get("iluminacion", "").lower()
    plano = params.get("plano", "").lower()
    composicion = params.get("composicion", "").lower()
    resolucion = params.get("resolucion", "").lower()
    acabado = params.get("acabado", "").lower()

    detalles = []
    if iluminacion:   detalles.append(f"iluminación {iluminacion}")
    if plano:         detalles.append(f"plano {plano}")
    if composicion:   detalles.append(f"composición {composicion}")
    if resolucion:    detalles.append(f"resolución {resolucion}")
    if acabado:       detalles.append(f"acabado {acabado}")

    if detalles:
        frases.append("Incluye detalles como " + ", ".join(detalles) + ".")

    # Unir todo en un solo texto
    prompt_final = " ".join(frases)
    return prompt_final.strip()
    
    return prompt.strip()

def configurar_pantalla2(mostrar_pantalla1=None):
    """
    Configura la segunda pantalla de la aplicación donde se muestra y edita el prompt generado.
    """
    validar_session_state()

    st.title("Tu prompt está listo")
    
    # Área de Edición
    st.header("Revisá y editá tu prompt")
    prompt_inicial = generar_prompt()
    if "prompt_generado" not in st.session_state:
        st.session_state.prompt_generado = prompt_inicial
    
    texto_editable = st.text_area(
        "Editar Prompt",
        value=st.session_state.prompt_generado,
        height=200,
        key="editor_prompt"
    )
    
    # Botón para restaurar original
    if st.button("↺ Restaurar original"):
        st.session_state.prompt_generado = prompt_inicial
        st.experimental_rerun()
    
    # Área de Copiado
    st.markdown("---")
    st.header("Copiá tu prompt")
    st.info("### ⬆️ CLICK EN EL ÍCONO DE COPIAR ⬆️\n"
            "Mirá la esquina superior derecha del recuadro")
    st.code(texto_editable, language="")
    st.success("✅ Prompt copiado exitosamente")
    
    # Traducción
    st.header("Traducción")
    st.markdown("""
    ¿Necesitás el prompt en inglés? Muchas herramientas funcionan mejor con prompts en inglés. 
    Si es tu caso, usá la traducción:
    
    1. Hacé clic en "Abrir Google Translate"
    2. El texto se cargará automáticamente
    3. Copiá la traducción
    """)
    
    google_translate_url = f"https://translate.google.com/?sl=es&tl=en&text={texto_editable}"
    st.markdown(f"[Abrir Google Translate]({google_translate_url})")
    st.info("💡 Tip: Revisá siempre la traducción automática para asegurarte de que mantiene el sentido deseado.")
    
    # Herramientas Recomendadas
    st.header("🛠️ Herramientas Recomendadas")
    
    with st.expander("DALL·E (OpenAI)", expanded=True):
        st.markdown("""
            Herramienta de OpenAI para dibujar imágenes con inteligencia artificial.
            - Permite creaciones artísticas y composiciones realistas
            - Basada en modelos de última generación
            - Ideal para prompts detallados y resultados consistentes
        """)
    
    with st.expander("MidJourney"):
        st.markdown("""
            Reconocida por su calidad artística y estética muy cuidada en las imágenes generadas.
            - Excelente para estilos artísticos específicos
            - Resultados de alta calidad visual
            - Gran comunidad de usuarios y recursos
        """)
    
    with st.expander("Stable Diffusion"):
        st.markdown("""
            Ideal para personalización y modificaciones detalladas de tu prompt.
            - Control preciso sobre los resultados
            - Múltiples modelos disponibles
            - Posibilidad de ajuste fino
        """)
    
    with st.expander("Grok (Twitter/X)"):
        st.markdown("""
            Conectá tus imágenes con las tendencias más actuales en redes sociales.
            - Integración directa con Twitter/X
            - Análisis de tendencias en tiempo real
            - Optimización para engagement
        """)
    
    with st.expander("Claude"):
        st.markdown("""
            Ideal para analizar y mejorar prompts complejos, integrándose con chatbots IA.
            - Análisis detallado de prompts
            - Sugerencias de mejora
            - Compatibilidad con otras herramientas IA
        """)
    
    with st.expander("Copilot"):
        st.markdown("""
            Soporte creativo para generación rápida y versátil de contenido y prompts.
            - Asistencia en tiempo real
            - Sugerencias contextuales
            - Integración con flujos de trabajo
        """)

    st.info("💡 Cada herramienta tiene sus fortalezas particulares. Te recomendamos probar varias para encontrar la que mejor se adapte a tu proyecto específico.")
    
    # Botón para volver
    if st.button("← Volver a editar"):
        if mostrar_pantalla1:
            mostrar_pantalla1()
            
    # Footnote
    st.markdown("---")
    st.markdown("*Trabajo final de un curso de IA. Para cualquier feedback o consulta, escribí a julietafantini@gmail.com.*")