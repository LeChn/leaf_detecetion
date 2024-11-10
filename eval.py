from ultralytics import YOLO

model = YOLO('best_float32.tflite')

outputs = model.predict('test/leaf', save=True, imgsz=1024, conf=0.2)


len(results[0].boxes)

for output in ouputs:
	print("there are", len(output.boxes), "leaves detected.")