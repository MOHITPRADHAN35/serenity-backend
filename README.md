#Serenity - AI Wellness Companion

![Serenity Logo](logo.png)

**Serenity** is your real-time AI wellness companion, designed to enhance emotional well-being by analyzing emotions through text and facial expressions. Powered by Groq, Serenity provides fast, accurate, and meaningful insights into your emotions to help you manage stress, track your mental health, and stay emotionally balanced.

##🚀 Project Overview
Project Name: Serenity
Hackathon: Groq Hackathon
Team Members:

Mohit Pradhan - AI Modules (Text and Facial Emotion Detection)

Sambhav - Cloud Integration

Aditya - Backend Development

Mahima - UI/UX Design

##🧠 Project Goal
Serenity’s mission is to provide emotional support in a fast-paced world. It uses cutting-edge AI technology to detect and analyze emotions from two key modalities:

Text Emotion Detection: Real-time emotion analysis from user input.

Facial Emotion Detection: Detecting emotions from facial expressions in real-time.

##🌟 Key Features:
Emotion Detection: Accurately detects emotions from text (happy, sad, angry, etc.).

Facial Expression Analysis: Real-time facial recognition and emotion classification.

Instant Feedback: Provides users with emotional insights and real-time feedback on their mood.

##🛠 Technologies Used:
Groq: Fast emotion inference engine for both text and facial emotion detection.

Python: Core programming language for AI and backend logic.

TensorFlow/Keras: Deep learning framework for training emotion detection models.

OpenCV: Used for real-time facial emotion detection.

Flask: Web framework for creating the backend API.

Heroku: For hosting the backend application (for demo purposes).

##🏁 Quick Start Guide
1. Clone the repository:
bash
Copy
Edit
git clone https://github.com/yourusername/Serenity.git
2. Navigate to the project folder:
bash
Copy
Edit
cd Serenity
3. Set up a virtual environment:
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # For Linux/MacOS
.\venv\Scripts\activate   # For Windows
4. Install required dependencies:
bash
Copy
Edit
pip install -r requirements.txt
5. Set up environment variables:
Copy the .env.sample file and rename it to .env.

Add necessary API keys and database credentials.

6. Run the backend API:
bash
Copy
Edit
python backend/app.py
7. Access the application:
Open your browser and navigate to http://localhost:5000 (or the hosted URL if deployed on Heroku).

##🧠 Emotion Detection Models
Text Emotion Detection
Serenity uses a pre-trained emotion analysis model to classify the user’s emotional state from text. Leveraging Groq's AI capabilities, it provides real-time analysis of the user's mood based on their written words.

Facial Emotion Detection
Serenity detects emotions in real-time through facial expressions. Using OpenCV, the system processes camera inputs and recognizes emotions like happiness, sadness, anger, and surprise.

##💡 Hackathon Submission
Final Deliverables:
A multimodal emotion detection system (text + facial).

User Interface that provides real-time emotional insights.

A backend API integrated with the AI models for smooth interaction.

Complete Documentation for easy setup and use.

##🚀 Future Enhancements
After the hackathon, we plan to:

Add more emotions and personalized insights.

Improve accuracy and real-time performance for facial emotion detection.

Build mobile and web applications for greater accessibility.

##👨‍💻 Contributing
We welcome contributions to make Serenity even better! Here’s how you can help:

Fork the repo to your own account.

Create a new branch for your feature (git checkout -b feature-name).

Commit your changes (git commit -am 'Add new feature').

Push your branch to your fork (git push origin feature-name).

Create a pull request with a description of your changes.

