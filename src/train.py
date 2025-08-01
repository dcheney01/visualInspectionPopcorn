from ultralytics import YOLO

# Load a model
model = YOLO('/home/daniel/software/visualInspectionPopcorn/runs/detect/train/weights/best.pt')  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data='/home/daniel/software/visualInspectionPopcorn/data/data.yaml', epochs=100, imgsz=640, device=[0,1], save=True)