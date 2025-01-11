# app.py
from flask import Flask, request, jsonify
import pickle
# import numpy as np

app = Flask(__name__)

# Load the trained model from model.pkl
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return "Machine Learning Model API"

@app.route('/predict', methods=['POST'])
def predict():
    # Check if JSON data is received
    if not request.is_json:
        return jsonify({'error': 'Invalid input, JSON expected'}), 400

    data = request.get_json()

    # Extract features from the JSON payload
    try:
        input_data = data['payloads']
        print(input_data)
        # Convert to numpy array and reshape
        # input_data = np.array(payloads).reshape(1, -1)
    except (KeyError, TypeError, ValueError):
        return jsonify({'error': 'Invalid input format. JSON with "features": [f1, f2, f3, f4] expected'}), 400

    # Make prediction
    prediction = model.predict(input_data)

    isDetected = False
    for detect in range(len(input_data)):
        if "normal" not in prediction[detect]:
            isDetected = True
    
    # Return the result as JSON
    return jsonify({'isMalicious': isDetected})

if __name__ == '__main__':
    app.run(debug=True) 
