import streamlit as st
import google.generativeai as genai
from PIL import Image
import cv2
import tempfile
import os

# 1. Configuración de la IA (Gemini 1.5 Flash es ideal para tu proyecto)
genai.configure(api_key="TU_API_KEY_AQUÍ")
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. Diseño de la página (Frontend mejorado)
st.set_page_config(page_title="Upload.com", page_icon="🚀", layout="wide")
st.title("🚀 Upload.com")
st.markdown("---")

# 3. Panel lateral
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=100)
    st.write("### Panel de Control")
    modo = st.selectbox("¿Qué quieres hacer?", ["Analizar Imagen", "Analizar Vídeo", "Resumir Texto"])
    st.info("Aprovecha tu tiempo con este programa.")

# 4. Lógica de subida de archivos (Ahora acepta vídeo mp4 y avi)
archivo_subido = st.file_uploader("Arrastra tu archivo aquí", type=['png', 'jpg', 'jpeg', 'txt', 'mp4', 'avi'])

if archivo_subido is not None:
    if modo == "Analizar Imagen":
        imagen = Image.open(archivo_subido)
        st.image(imagen, caption='Imagen lista para procesar', width=500)
        
        pregunta = st.text_input("¿Qué quieres saber de la imagen?", "Explica qué ves en esta imagen de forma detallada")
        if st.button("Preguntar a la IA"):
            with st.spinner('La IA está pensando...'):
                respuesta = model.generate_content([pregunta, imagen])
                st.subheader("Resultado:")
                st.info(respuesta.text)

    elif modo == "Analizar Vídeo":
        # Guardamos el vídeo temporalmente para que OpenCV lo lea
        tfile = tempfile.NamedTemporaryFile(delete=False) 
        tfile.write(archivo_subido.read())
        
        st.video(archivo_subido) # Muestra el vídeo en la web
        
        if st.button("Extraer frame y analizar con IA"):
            with st.spinner('Extrayendo fotograma con OpenCV...'):
                cap = cv2.VideoCapture(tfile.name)
                success, frame = cap.read()
                if success:
                    # Convertir el frame de OpenCV (BGR) a PIL (RGB) para Gemini
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    img_para_ia = Image.fromarray(frame_rgb)
                    
                    st.image(img_para_ia, caption="Frame capturado", width=400)
                    
                    # Enviar a la IA
                    respuesta = model.generate_content(["Analiza este frame del vídeo y dime qué sucede", img_para_ia])
                    st.subheader("Análisis del vídeo:")
                    st.success(respuesta.text)
                cap.release()
        os.remove(tfile.name) # Borrar archivo temporal

    elif modo == "Resumir Texto":
        texto = archivo_subido.read().decode("utf-8")
        st.text_area("Contenido:", texto, height=150)
        
        if st.button("Resumir ahora"):
            respuesta = model.generate_content(f"Resume este texto de forma profesional: {texto}")
            st.success(respuesta.text)

else:
    st.info("👋 ¡Hola! Sube una imagen, un texto o un vídeo para que Upload.com empiece a trabajar.")