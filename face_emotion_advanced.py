import cv2
from fer import FER

# Emotion detector
detector = FER(mtcnn=True)

# Webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret: 
        break

    # Detect emotions
    results = detector.detect_emotions(frame)

    for face in results:

        (x, y, w, h) = face["box"]
        emotions = face["emotions"]

        # Get dominant emotion
        emotion = max(emotions, key=emotions.get)
        confidence = emotions[emotion]

        # Draw rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

        text = f"{emotion} ({confidence:.2f})"

        cv2.putText(frame, text, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (0,255,0), 2)

    cv2.imshow("Face Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()