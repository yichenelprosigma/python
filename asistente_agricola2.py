import streamlit as st
import google.generativeai as genai
from PIL import Image
import pandas as pd
st.title("Asistente agrícola")

def ia_diagnosticar_planta(gemini, imagen , idioma):
    genai.configure(api_key=gemini)
    modelo = genai.GenerativeModel("gemini-1.5-flash")

    tips=f"Dile al usuario si tiene plaga o está marchitada la flor en este idioma {idioma}"

    respuesta_de_ia=modelo.generate_content(tips,imagen)
    return respuesta_de_ia.text

def subir_imagenes(api_key):
    st.text("pon aquí fotos")
    subida_de_imagenes=st.file_uploader("Sube la foto aquí", type=["Jpg","Png","Webp"])
    idioma = st.selectbox("Selecciona el idioma", ["Español", "Ruso", "Chino", "Inglés"])

    if subida_de_imagenes is not None:
        foto = Image.open(subida_de_imagenes)
        st.image(foto, caption="Imagen cargada", use_container_width=True)

    if st.button("Diagnosticar"):
        if not api_key:
            st.error("Por favor, introduce tu API Key en la barra lateral.")
        else:
            with st.spinner("Analizando cultivo..."):
                resultado = ia_diagnosticar_planta(api_key, foto, idioma)
                st.write(resultado)

if __name__ == "__main__":
    with st.sidebar:
        mi_api_key = st.text_input("Ponga su api key",type="password")
    
    subir_imagenes(mi_api_key)