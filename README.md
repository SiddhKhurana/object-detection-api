# 🔍 Object Detection API with YOLOv5 + Flask

This project is a simple and powerful REST API for real-time object detection built using:

- 🧠 [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5)
- ⚙️ Flask (Python micro web framework)
- 📦 Python (with virtualenv)

You can upload an image to the `/detect` endpoint, and get back detected objects in JSON format — including class name, confidence score, and bounding box coordinates.

---

## 🚀 Features

- Accepts image uploads via `/detect` endpoint
- Performs object detection using YOLOv5s model
- Returns structured JSON output
- Fast and minimal API setup
- Easy to extend: draw boxes, deploy, or integrate with a frontend

---

## 📦 Requirements

- Python 3.8 or higher
- pip / virtualenv

Recommended packages (installed via `pip install`):
-flask
-ultralytics
-torch
-torchvision
-opencv-python-headless

---

## 📂 API Endpoints

### `POST /detect`

Upload an image and receive detection results using YOLOv5.

---

### 📤 Request

- **Method:** `POST`
- **URL:** `http://localhost:5000/detect`
- **Content-Type:** `multipart/form-data`
- **Body:**
  - `image`: (File) – The image to analyze

You can test this using **Postman** or `curl`:

#### 🔧 curl example:
```bash
curl -X POST -F "image=@your-image.jpg" http://127.0.0.1:5000/detect
