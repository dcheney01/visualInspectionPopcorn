import pyzed.sl as sl
import cv2
import time
from ultralytics import YOLO
import serial

def main():
    while True:
        start = time.time()
        result = model.predict(source=left_image.get_data()[:,:,:3], imgsz=640, show=True, verbose=False, conf=0.7)


if __name__ == "__main__":
    main()