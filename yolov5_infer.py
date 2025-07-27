from ultralytics import YOLO

model = YOLO("yolov5s.pt")  # Automatically downloads the pretrained model
def detect_objects(image_path):
    results = model(image_path)
    return results[0].tojson()
