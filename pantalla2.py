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

def configurar_pantalla2(callback):
    """
    Configura la segunda pantalla de la aplicación donde se muestra y edita el prompt generado.
    callback: función para cambiar a la pantalla anterior.
    """
    validar_session_state()

    st.title("Tu prompt está listo")
    
    # División en dos columnas principales
    col_main, col_sidebar = st.columns([2, 1])
    
    # Columna Principal (Prompt y Edición)
    with col_main:
        # Área de Edición
        st.header("Revisá y editá tu prompt")
        prompt_inicial = generar_prompt(st.session_state.params)
        if "prompt_generado" not in st.session_state:
            st.session_state.prompt_generado = prompt_inicial
        
        texto_editable = st.text_area(
            "Editar Prompt",
            value=st.session_state.prompt_generado,
            height=200,
            key="editor_prompt"
        )
        
        # Botón de restaurar en línea con el área de edición
        if st.button("↺ Restaurar original", use_container_width=True):
            st.session_state.prompt_generado = prompt_inicial
            st.experimental_rerun()
        
        # Área de Copiado más prominente
        st.markdown("---")
        st.header("Copiá tu prompt")
        
        # Contenedor para el código y mensaje de copiado
        with st.container():
            st.code(texto_editable, language="")
            copy_col1, copy_col2 = st.columns([1, 3])
            with copy_col1:
                st.info("⬆️ COPIAR")
            with copy_col2:
                st.success("✅ Prompt listo para usar")
    
    # Columna Lateral (Herramientas y Traducción)
    with col_sidebar:
        # Sección de Traducción más compacta
        with st.container():
            st.subheader("Traducción")
            st.markdown("""
            ¿Necesitás el prompt en inglés?
            1. Hacé clic en "Abrir Google Translate"
            2. El texto se cargará automáticamente
            3. Copiá la traducción
            """)
            
            google_translate_url = f"https://translate.google.com/?sl=es&tl=en&text={texto_editable}"
            st.markdown(f"[Abrir Google Translate]({google_translate_url})")
            st.info("💡 Tip: Revisá siempre la traducción")
        
        # Llamada a la función de herramientas de utils.py
        mostrar_herramientas()
    
    # Botón para volver al final
    st.markdown("---")
    if st.button("← Volver a editar", use_container_width=True):
        if callback:
            callback()
    
    # Footnote
    st.markdown("---")
    st.markdown("*Trabajo final de un curso de IA. Para cualquier feedback o consulta, escribí a julietafantini@gmail.com.*")
