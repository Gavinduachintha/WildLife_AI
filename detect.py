from ultralytics import YOLO
from picamera2 import Picamera2
import cv2

model = YOLO("yolov8n.pt")

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"size": (640, 480)}))
picam2.start()

while True:
    frame = picam2.capture_array()

    results = model(frame, imgsz=320)
    annotated = results[0].plot()

    cv2.imshow("YOLO", annotated)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
