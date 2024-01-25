import time
from ultralytics import YOLO
import cv2 as cv
import numpy as np

'''
Set WEBCAM to 1 to use your webcam or 0 to use the Flea2 cameras on the lab machine
Set CATCHER to 1 to use the catcher connected to the lab machine or 0 to use your own computer
'''
WEBCAM = 1

if WEBCAM:
    camera = cv.VideoCapture(0)
else:
    from src.Flea2Camera import FleaCam
    camera = FleaCam()
    camera.set

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