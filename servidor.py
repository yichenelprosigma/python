import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuración: Carpeta donde se guardarán los vídeos
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Límite de tamaño (ejemplo: 50MB)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024 

# Extensiones permitidas
ALLOWED_EXTENSIONS = {'mp4', 'mov', 'avi', 'mkv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return "No hay parte de archivo"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No se seleccionó ningún archivo"
    
    if file and allowed_file(file.filename):
        # secure_filename evita que alguien suba archivos con nombres peligrosos
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return f"Vídeo '{filename}' subido con éxito a Upload.com"
    
    return "Tipo de archivo no permitido"

if __name__ == '__main__':
    # Crea la carpeta si no existe
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True, port=5000)