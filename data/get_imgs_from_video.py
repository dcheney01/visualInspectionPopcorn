import cv2

# Specify the path to the video file
video_path = '/home/daniel/catkin_ws/src/josh_vision/data/phone_video.mp4'

# Create a VideoCapture object
cap = cv2.VideoCapture(video_path)

# Check if the video file is opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Read frames from the video until there are no more frames
frame_count = 0
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Break the loop if there are no more frames
    if not ret:
        break

    # Process the frame (you can replace this with your own processing)
    # For example, you can save each frame as an image
    output_image_path = f'/home/daniel/catkin_ws/src/josh_vision/data/phone_data/frame_{frame_count}.png'
    cv2.imwrite(output_image_path, frame)

    # Display the frame (optional)
    cv2.imshow('Frame', frame)

    # Increment frame count
    frame_count += 1

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close the OpenCV window
cap.release()
cv2.destroyAllWindows()

print(f"Frames saved to {frame_count} files.")