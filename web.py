import streamlit as st #para una interfaz de una página web
import google.generativeai as genai # Si usas la API de Gemini
from PIL import Image

# 1. Configuración de la IA (Pon tu clave aquí)
genai.configure(api_key="TU_API_KEY_AQUÍ")
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. Diseño de la página (Frontend)
st.set_page_config(page_title="Upload.com", page_icon="🚀")
st.title("🚀 Upload.com")
st.subheader("La IA que analiza tus archivos")

# 3. Barra lateral para los que no saben programar
with st.sidebar:
    st.write("### Panel de Control")
    modo = st.selectbox("¿Qué quieres hacer?", ["Analizar Imagen", "Resumir Texto"])

# 4. Lógica de subida de archivos
archivo_subido = st.file_uploader("Arrastra tu archivo aquí", type=['png', 'jpg', 'jpeg', 'txt'])

if archivo_subido is not None:
    if modo == "Analizar Imagen":
        # Mostrar la imagen
        imagen = Image.open(archivo_subido)
        st.image(imagen, caption='Imagen subida', use_column_width=True)
        
        if st.button("Preguntar a la IA"):
            # Enviar a la IA
            respuesta = model.generate_content(["Explica qué ves en esta imagen de forma detallada", imagen])
            st.write("### Resultado:")
            st.info(respuesta.text)

    elif modo == "Resumir Texto":
        texto = archivo_subido.read().decode("utf-8")
        st.text_area("Contenido del archivo:", texto, height=200)
        
        if st.button("Resumir ahora"):
            respuesta = model.generate_content(f"Resume el siguiente texto de forma breve: {texto}")
            st.write("### Resumen:")
            st.success(respuesta.text)

else:
    st.info("Por favor, sube un archivo para comenzar.")