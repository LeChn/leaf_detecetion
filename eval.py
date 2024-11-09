from ultralytics import YOLO

model = YOLO('best_float32.tflite')

model.predict('test/leaf', save=True, imgsz=1024, conf=0.2)