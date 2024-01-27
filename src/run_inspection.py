import time
from ultralytics import YOLO
import cv2 as cv
import numpy as np
from PIL import Image

# def main(weights_path):
weights_path = "/fsg/dcheney1/visualInspectionPopcorn/runs/detect/train3/weights/best.pt"
video_writer = cv.VideoWriter("output_video.mp4", cv.VideoWriter_fourcc(*"MJPG"),
                                10, (640,480))

camera = cv.VideoCapture(0)
# camera.set(cv.CAP_PROP_BRIGHTNESS, 8)
# camera.set(cv.CAP_PROP_EXPOSURE, 20)
# camera.set(cv.CAP_PROP_CONTRAST, 10)
# camera.set(cv.CAP_PROP_FPS, 60)

print("Camera Started...")

model = YOLO(weights_path)
print("Model Loaded...")

counter = 0

while True:
    ret0, frame = camera.read()

    start = time.time()
    result = model.predict(source=frame, imgsz=640, show=True, verbose=False, conf=0.75)
    end = time.time()
    print(f"Loop Time: {end-start}")

    # Show the results
    for r in result:
        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im.save(f'simple_video/{counter}.jpg')  # save image

    counter += 1


# if __name__ == "__main__":
#     print
#     main(weights_path)