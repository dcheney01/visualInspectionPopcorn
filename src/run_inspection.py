import pyzed.sl as sl
import cv2
import time
from ultralytics import YOLO
import serial

def setup_ZED():
    zed = sl.Camera()
    # Set configuration parameters (modify as needed)
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD720  # Adjust resolution
    init_params.depth_mode = sl.DEPTH_MODE.PERFORMANCE  # Adjust depth mode
    # Open the camera
    if not zed.is_opened():
        print("Opening ZED Camera...")
        status = zed.open(init_params)
        if status != sl.ERROR_CODE.SUCCESS:
            print(f"Error opening ZED Camera: {str(status)}")
            exit()
    return zed

def setup_yolo():
    print("Loading YOLO model...")
    model = YOLO('/home/daniel/catkin_ws/src/josh_vision/runs/detect/train2/weights/best.pt')
    return model

def setup_serial_connection():
    print("Setting up serial connection...")
    serial_port = "/dev/ttyUSB0"
    baud_rate = 9600
    ser = serial.Serial(serial_port, baud_rate)
    ser.flush()
    return ser

def determine_tracking_object(detected_classes):
    priority_tracking = ["foam", "box", "trash_can", "stool"]
    class_ids = ["stool", "trash_can", "foam", "box"]

    curr_highest_priority_idx = None
    curr_highest_priority_class = None

    for i in range(len(detected_classes)):
        detected_id = int(detected_classes[i].item())
        curr_class = class_ids[detected_id]

        if curr_class in priority_tracking and (
            curr_highest_priority_idx is None or priority_tracking.index(curr_class) < priority_tracking.index(curr_highest_priority_class)):
                curr_highest_priority_idx = i
                curr_highest_priority_class = curr_class
    return curr_highest_priority_idx, curr_highest_priority_class

def get_desired_servo_locations(xn_c, yn_c):
    kp = 20.0
    setpoint = 0.5

    yaw = kp * (setpoint - xn_c)
    pitch = kp * (setpoint - yn_c)
    return int(yaw), int(pitch)

def send_servo_commands(ser, yaw, pitch):
    ser.write(f"{yaw} {pitch}\n".encode())

def main():
    zed = setup_ZED()
    model = setup_yolo()
    ser = setup_serial_connection()
    
    print("Starting Inference...")
    runtime_params = sl.RuntimeParameters()
    left_image = sl.Mat()
    try:
        while True:
            start = time.time()
            if zed.grab(runtime_params) == sl.ERROR_CODE.SUCCESS:
                zed.retrieve_image(left_image, sl.VIEW.LEFT)
                result = model.predict(source=left_image.get_data()[:,:,:3], imgsz=640, show=True, verbose=False, conf=0.7)

                if result[0].boxes.xywhn.shape[0] != 0:
                    tracking_idx, tracking_class = determine_tracking_object(result[0].boxes.cls)
                    xn_c, yn_c = result[0].boxes.xywhn[tracking_idx][:2]
                    yaw, pitch = get_desired_servo_locations(xn_c, yn_c)
                    print(f"Servos Commanded to: ({yaw}, {pitch})")
                    send_servo_commands(ser, yaw, pitch)


            line = ser.readline().decode('utf-8').strip()  # Assuming UTF-8 encoding, remove leading/trailing whitespace
            if line:
                # print(f"Tracking {tracking_class} at ({xn_c}, {yn_c})")
                print(f"Loop time: {time.time() - start}")
                print("Received:", line)
                print("")

            time.sleep(0.1)
    finally:
        zed.close()
        print("ZED Camera closed.")

if __name__ == "__main__":
    main()