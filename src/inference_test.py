from ultralytics import YOLO

model = YOLO('/home/daniel/catkin_ws/src/josh_vision/runs/detect/train/weights/best.pt')
results = model.predict(source="/home/daniel/catkin_ws/src/josh_vision/raw_data/phone_video.mp4", show=True)