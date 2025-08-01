from ultralytics import YOLO
import os
import time
import cv2

model = YOLO('/fsg/dcheney1/visualInspectionPopcorn/runs/detect/train3/weights/best.pt')
data_folder = "/media/dcheney1/CCJ/popcorn_classification/raw_data/webcam"

print("loaded model")
cv2.namedWindow("YOLO Detection", cv2.WINDOW_NORMAL)

for folder in os.listdir(data_folder):
    folder_path = os.path.join(data_folder, folder)
    for img in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img)
        image = cv2.imread(img_path)

        start = time.time()
        results = model.predict(image, show=True, verbose=False, conf=0.8)
        end = time.time()

        print(f"Time: {end - start}")

        cv2.waitKey(0)