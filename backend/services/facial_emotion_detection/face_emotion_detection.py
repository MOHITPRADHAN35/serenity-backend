import os
import cv2
import numpy as np
import tensorflow as tf
import csv
import time

# === Setup Paths ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "emotion_detections.csv")

# === Emotion Labels ===
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# === Load models once at startup! 🚀
emotion_model_path = os.path.join(BASE_DIR, "models", "emotion_model.h5")
face_model_path = os.path.join(BASE_DIR, "models", "face_model.h5")

emotion_model = tf.keras.models.load_model(emotion_model_path, compile=False)
face_model = tf.keras.models.load_model(face_model_path, compile=False)

# === Utility Functions ===
def preprocess_image(image):
    image = cv2.resize(image, (64, 64))
    image = np.expand_dims(image, axis=-1)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0
    return image

def detect_emotions_in_frame(frame_bytes):
    """Detect emotion from a single image frame (bytes)."""
    nparr = np.frombuffer(frame_bytes, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) == 0:
        return {"emotion": "No face detected", "confidence": 0.0}

    x, y, w, h = faces[0]
    face = frame[y:y+h, x:x+w]
    face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

    processed_face = preprocess_image(face_gray)

    emotion_probs = emotion_model.predict(processed_face)
    emotion = emotion_labels[np.argmax(emotion_probs)]
    confidence = float(np.max(emotion_probs))

    return {"emotion": emotion, "confidence": confidence}

def detect_emotions_in_video():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    csv_file = open(csv_path, mode="w", newline="")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Timestamp", "Emotion", "Confidence"])

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            processed_face = preprocess_image(face_gray)

            emotion_probs = emotion_model.predict(processed_face)
            emotion = emotion_labels[np.argmax(emotion_probs)]
            confidence = float(np.max(emotion_probs))
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

            csv_writer.writerow([timestamp, emotion, confidence])

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"{emotion}: {confidence*100:.2f}%", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow("Real-Time Emotion Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    csv_file.close()
    cv2.destroyAllWindows()

# === Entry point ===
if __name__ == "__main__":
    detect_emotions_in_video()
