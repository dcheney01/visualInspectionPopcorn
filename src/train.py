from ultralytics import YOLO

# Load a model
model = YOLO('yolov5s.pt')  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data='/home/daniel/catkin_ws/src/josh_vision/data/data.yaml', epochs=100, imgsz=640, device=[0,1], save=True)