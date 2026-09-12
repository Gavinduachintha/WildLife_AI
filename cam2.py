import cv2
from picamera2 import Picamera2
from ultralytics import YOLO
import time

# Camera setup - lower res for speed + low RAM
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

# Load NCNN model (fastest on Pi 5)
model = YOLO("yolo26n_ncnn_model")   # or yolo11n_ncnn_model / yolov8n_ncnn_model

print("YOLO Camera started. Press 'q' to quit.")

frame_count = 0
start_time = time.time()

while True:
    frame = picam2.capture_array()

    # Inference with smaller size for 2GB Pi
    results = model(frame, imgsz=480, conf=0.25, verbose=False)

    annotated = results[0].plot()

    # Show FPS
    frame_count += 1
    if frame_count % 10 == 0:
        fps = frame_count / (time.time() - start_time)
        cv2.putText(annotated, f"FPS: {fps:.1f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("YOLO Pi Camera", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
picam2.stop()
