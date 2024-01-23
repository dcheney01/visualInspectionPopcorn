from ultralytics import YOLO

# Load a model
model = YOLO('yolov8m.pt')  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data='/home/daniel/software/visualInspectionPopcorn/data/data.yaml', epochs=200, imgsz=640, device=[0,1], save=True)