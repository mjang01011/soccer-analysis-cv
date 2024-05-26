from ultralytics import YOLO

# github.com/ultralytics/ultralytics
model = YOLO('yolov8x')

results = model.predict('data/08fd33_4.mp4', save=True)

print(results[0])
print("===========")

for box in results[0].boxes:
    print(box)