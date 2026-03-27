import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Use webcam OR replace with video file
cap = cv2.VideoCapture("traffic.mp4")
# cap = cv2.VideoCapture("traffic.mp4")

# Vehicle classes (COCO dataset)
vehicle_classes = [2, 3, 5, 7]  
# car=2, motorcycle=3, bus=5, truck=7

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO
    results = model(frame)

    count = 0

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])

            if cls in vehicle_classes:
                count += 1

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Draw bounding box
                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)

                # Label
                cv2.putText(frame, "Vehicle", (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    # Show vehicle count
    cv2.putText(frame, f"Vehicles: {count}", (20,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("Traffic Analyzer", frame)

    # Exit on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()