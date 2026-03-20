import streamlit as st
import google.generativeai as genai
from PIL import Image
import cv2
import tempfile
import os
import time
from datetime import datetime
import pandas as pd

# =================================================================
# [CLASS] CONFIGURACIÓN Y ESTILOS DE LA INTERFAZ
# =================================================================
class UIStyle:
    @staticmethod
    def apply_custom_css():
        st.markdown("""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;500&display=swap');
            :root { --primary-glow: #ff4b4b; --bg-dark: #0d1117; }
            html, body, [class*="css"] { font-family: 'Fira Code', monospace; }
            .main { background-color: var(--bg-dark); color: #c9d1d9; }
            .stButton>button {
                background: linear-gradient(90deg, #ff4b4b 0%, #a50000 100%);
                border: none; color: white; border-radius: 4px;
                font-weight: bold; width: 100%; transition: 0.3s;
            }
            .stButton>button:hover { box-shadow: 0 0 20px var(--primary-glow); transform: scale(1.01); }
            .history-card {
                padding: 15px; border-left: 4px solid var(--primary-glow);
                background: #161b22; margin: 10px 0; border-radius: 0 8px 8px 0;
            }
            </style>
        """, unsafe_allow_html=True)

# =================================================================
# [CLASS] MOTOR DE INTELIGENCIA ARTIFICIAL
# =================================================================
class AIEngine:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model_flash = genai.GenerativeModel('gemini-1.5-flash')
        self.model_pro = genai.GenerativeModel('gemini-1.5-pro')

    def analyze_image(self, prompt, img, fast_mode=True):
        model = self.model_flash if fast_mode else self.model_pro
        response = model.generate_content([prompt, img])
        return response.text

    def upload_and_analyze_video(self, path, prompt):
        video_file = genai.upload_file(path=path)
        # Espera activa de procesamiento
        while video_file.state.name == "PROCESSING":
            time.sleep(2)
            video_file = genai.get_file(video_file.name)
        
        response = self.model_flash.generate_content([prompt, video_file])
        return response.text

# =================================================================
# [MAIN] LÓGICA DE LA APLICACIÓN
# =================================================================
def main():
    UIStyle.apply_custom_css()
    
    if 'history_db' not in st.session_state:
        st.session_state.history_db = []

    # --- SIDEBAR ---
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=60)
        st.title("UPLOAD PRO v4.1")
        
        api_key = st.text_input("Gemini API Key:", type="password")
        menu = st.radio("SISTEMAS:", ["⚡ Dashboard", "🎮 Gaming Analytics", "📂 Historial"])
        
        st.divider()
        if st.button("🗑️ LIMPIAR SESIÓN"):
            st.session_state.history_db = []
            st.rerun()

    if not api_key:
        st.warning("⚠️ Introduce tu API Key en el lateral para comenzar.")
        return

    # Inicializar motor si hay API Key
    ai_engine = AIEngine(api_key)

    # --- MÓDULO: DASHBOARD (IMAGEN) ---
    if menu == "⚡ Dashboard":
        st.header("🖼️ Visión Neuronal")
        uploaded_img = st.file_uploader("Sube una imagen:", type=['png', 'jpg', 'jpeg'])
        
        if uploaded_img:
            img = Image.open(uploaded_img)
            col1, col2 = st.columns(2)
            with col1:
                st.image(img, use_container_width=True)
            with col2:
                prompt = st.text_area("Instrucciones para la IA:", "Describe esta imagen.")
                if st.button("ANALIZAR"):
                    with st.spinner("Procesando..."):
                        res = ai_engine.analyze_image(prompt, img)
                        st.session_state.history_db.append({"type": "📸 Imagen", "data": res, "time": datetime.now()})
                        st.info(res)

    # --- MÓDULO: GAMING ANALYTICS (VIDEO) ---
    elif menu == "🎮 Gaming Analytics":
        st.header("🎬 Analizador de Clips")
        

["Image of video editing software interface"]

# --- MÓDULO: GAMING ANALYTICS (VIDEO) ---
    elif menu == "🎮 Gaming Analytics":
        st.header("🎬 Analizador de Clips")
        
        # Esta línea debe estar alineada exactamente con el st.header de arriba
        video_up = st.file_uploader("Sube tu clip:", type=['mp4', 'mov', 'avi'])
        
        if video_up:
            # El código dentro del IF lleva un nivel más de sangría
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tfile:
                tfile.write(video_up.read())
                temp_path = tfile.name

            st.video(temp_path)
            action = st.selectbox("Acción:", ["Resumen de jugada", "Detectar errores", "Crear título viral"])
            
            if st.button("PROCESAR VIDEO"):
                with st.status("Subiendo y analizando vídeo...") as status:
                    try:
                        res = ai_engine.upload_and_analyze_video(temp_path, action)
                        st.session_state.history_db.append({"type": "🎥 Vídeo", "data": res, "time": datetime.now()})
                        st.write(res)
                        status.update(label="Análisis completo", state="complete")
                    except Exception as e:
                        st.error(f"Error: {e}")
                    finally:
                        # Limpieza del archivo temporal
                        if os.path.exists(temp_path):
                            os.remove(temp_path)

    # --- MÓDULO: HISTORIAL ---
    elif menu == "📂 Historial":
        st.header("📜 Archivo de Sesión")
        if not st.session_state.history_db:
            st.info("Aún no hay registros.")
        else:
            for entry in reversed(st.session_state.history_db):
                st.markdown(f"""
                <div class="history-card">
                    <small>{entry['time'].strftime('%H:%M:%S')} | <b>{entry['type']}</b></small><br>
                    {entry['data']}
                </div>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()