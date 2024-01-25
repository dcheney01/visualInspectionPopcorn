import time
from ultralytics import YOLO
import cv2 as cv

camera = cv.VideoCapture(0)

def main(weights_path):
    model = YOLO(weights_path)

    while True:
        if WEBCAM:
            ret0, frame = camera.read()
        else:
            frame = camera.getFrame()

        start = time.time()
        result = model.predict(source=frame, imgsz=640, show=True, verbose=False, conf=0.3, device="cpu")
        end = time.time()
        print(f"Loop Time: {end-start}")


if __name__ == "__main__":
    weights_path = "/fsg/dcheney1/visualInspectionPopcorn/runs/detect/train/weights/best.pt"
    main(weights_path)