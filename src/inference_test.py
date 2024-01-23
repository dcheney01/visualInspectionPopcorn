from ultralytics import YOLO
import os
import time
import cv2

model = YOLO('/home/daniel/software/visualInspectionPopcorn/runs/detect/train/weights/best.pt')
data_folder = "/home/daniel/software/visualInspectionPopcorn/data/raw_data/validation"

cv2.namedWindow("YOLO Detection", cv2.WINDOW_NORMAL)
images = sorted(os.listdir(data_folder))

for img in images:
    img_path = os.path.join(data_folder, img)
    image = cv2.imread(img_path)

    start = time.time()
    results = model.predict(image, show=True, verbose=False, conf=0.6)
    end = time.time()

    print(f"Time: {end - start}")

    cv2.waitKey(0)


