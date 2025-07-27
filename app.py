from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from yolov5_infer import detect_objects

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return "✅ Object Detection API is running!"

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    filename = secure_filename(image.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    image.save(filepath)

    results = detect_objects(filepath)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
