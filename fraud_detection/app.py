import json
import joblib
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request


app = Flask(__name__)
model = joblib.load('model/lgbm_fraud_detection.sav')

PORT = 5002


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = json.loads(request.json)
        data = np.array(list(data.values())).astype(float)
        prediction = model.predict(data.reshape(1, -1))[0]
        return jsonify({'prediction': int(prediction)}), 200
    
    except json.JSONDecodeError:
        return jsonify(
            {'error': 'Invalid JSON format in request body'}
        ), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'Alive!'}), 200


if __name__ == '__main__':
    app.run(
        port=PORT, 
        debug=False, 
        threaded=True
    )
