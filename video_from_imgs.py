import os
import cv2 as cv


image_folder = "/fsg/dcheney1/visualInspectionPopcorn/simple_video"
video_name = "simple.avi"

images = [img for img in os.listdir(image_folder)]

frame = cv.imread(os.path.join(image_folder, images[0]))

height, width, layers = frame.shape

video = cv.VideoWriter(video_name, 0, 25, (width, height))

for image in images:
    video.write(cv.imread(os.path.join(image_folder, image)))

cv.destroyAllWindows()
video.release()