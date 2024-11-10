from ultralytics import YOLO

model = YOLO('best_float32.tflite', task="detect")

outputs = model.predict('test/leaf', save=True, imgsz=1024, conf=0.2)


len(results[0].boxes)


import pandas as pd

df = pd.DataFrame({
    'image_name': pd.Series(dtype='str'),
    'num_boxes': pd.Series(dtype='int')
})

for output in outputs:
	image_name: str = output.path.split("/")[-1]
	num_boxes: int = len(output.boxes)
	df.loc[len(df)] = [image_name, num_boxes]

df.to_csv('output.csv', index=False)
