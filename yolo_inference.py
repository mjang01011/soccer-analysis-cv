from ultralytics import YOLO

# github.com/ultralytics/ultralytics
model = YOLO('models/finetuned_yolo_v5/best.pt')

results = model.predict('input_videos/08fd33_4.mp4', save=True)

print(results[0])
print("===========")

for box in results[0].boxes:
    print(box)