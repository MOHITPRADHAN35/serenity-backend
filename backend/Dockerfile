# Use official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy everything from the backend folder into the container
COPY . .
COPY services/facial_emotion_detection/emotion_model.h5 /app/services/facial_emotion_detection/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Give start.sh execute permission
RUN chmod +x start.sh

# Start your FastAPI server
CMD ["./start.sh"]
