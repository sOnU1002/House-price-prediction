AI House Price Predictor

Overview

The AI House Price Predictor is a web-based application that predicts house prices based on user inputs. It features an interactive chatbot-style interface for collecting user data and a Flask backend for making predictions using a machine learning model.

Features

📊 Machine Learning Model: Uses Linear Regression and Random Forest to predict house prices.

🤖 Chatbot UI: Collects user inputs through a conversational interface.

🚀 Flask API Backend: Processes data and returns predictions.

🎨 Particles.js Animation: Enhances UI with animated effects.

Installation & Setup

Step 1: Clone the Repository

git clone https://github.com/your-username/AI-House-Price-Predictor.git
cd AI-House-Price-Predictor

Step 2: Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

Step 3: Install Dependencies

pip install -r requirements.txt

Step 4: Train the Model

python train_model.py

This script will:

Load the house price dataset.

Train both Linear Regression and Random Forest models.

Save the best-performing model as best_model.pkl.

Step 5: Run the Flask Application

python app.py

The application will run on http://127.0.0.1:5500/.

How It Works

1️⃣ User Interaction



The chatbot greets the user and asks 5 questions about house features:

Number of bedrooms 🛏️

Number of bathrooms 🚿

Number of floors 🏠

Year built 📅

Square footage of living area 📐

2️⃣ Backend Processing



The Flask backend receives input via a /predict API endpoint.

The trained model predicts the house price based on the input features.

Returns the predicted price in JSON format.

3️⃣ Displaying Prediction


The chatbot displays the predicted house price in the chat interface.


Technologies Used

Python (Flask, NumPy, Scikit-learn, Pickle)

JavaScript (Fetch API, Particles.js)

HTML/CSS (Chatbot UI)

Machine Learning (Linear Regression, Random Forest)

Future Enhancements 🚀

Add more advanced ML models for better accuracy.

Improve UI with voice-enabled chatbot.
