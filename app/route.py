import io
from flask import Blueprint, request, render_template, url_for
from PIL import Image
from datetime import datetime
import uuid
from .utils import query
from .config import Config

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/', methods=['GET'])
def index():
    return render_template('index.html', filename=None)

@app_routes.route('/generate-image', methods=['POST'])
def generate_image():
    headers = {"Authorization": f"Bearer {Config.API_KEY}"}
    prompt = request.form.get("prompt")
    
    if not prompt:
        return render_template('index.html', filename=None, error="Prompt is required")

    image_bytes = query(Config.API_URL, headers, {"inputs": prompt})

    if image_bytes is not None:
        try:
            image = Image.open(io.BytesIO(image_bytes))
            current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
            random_id = str(uuid.uuid4())[:8]
            filename = f"static/output/image_{current_time}_{random_id}.png"
            image.save(filename)
            return render_template('index.html', filename=f'image_{current_time}_{random_id}.png')
        except Image.UnidentifiedImageError:
            return render_template('index.html', filename=None, error="Could not open image.")
    else:
        return render_template('index.html', filename=None, error="No image data returned.")