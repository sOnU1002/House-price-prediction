from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)


with open('best_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
      
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

     
        bedrooms = float(data.get('bedrooms', 0))
        bathrooms = float(data.get('bathrooms', 0))
        floors = float(data.get('floors', 0))
        yr_built = float(data.get('yr_built', 0))
        sqft_living = float(data.get('sqft_living', 0))

    
        features = np.array([bedrooms, bathrooms, floors, yr_built, sqft_living]).reshape(1, -1)

        prediction = model.predict(features)[0]  
        return jsonify({'prediction': f"{prediction:,.2f}"})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)