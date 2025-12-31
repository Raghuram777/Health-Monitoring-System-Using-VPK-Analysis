from flask import Flask, render_template, request, jsonify
from ayurvedic_predictor import AyurvedicPredictor
import json

app = Flask(__name__)

# Initialize predictor
predictor = AyurvedicPredictor()
predictor.load_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        symptoms = data.get('symptoms', [])
        
        if not symptoms:
            return jsonify({'error': 'No symptoms provided'})
        
        # Clean and validate symptoms
        symptoms = [symptom.strip() for symptom in symptoms if symptom.strip()]
        
        if not symptoms:
            return jsonify({'error': 'No valid symptoms provided'})
        
        # Get prediction
        result = predictor.predict(symptoms)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/batch_predict', methods=['POST'])
def batch_predict():
    try:
        data = request.get_json()
        symptoms_list = data.get('symptoms_list', [])
        
        if not symptoms_list:
            return jsonify({'error': 'No symptoms list provided'})
        
        results = predictor.predict_batch(symptoms_list)
        
        return jsonify({'predictions': results})
        
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'model_loaded': predictor.model_loaded
    })

if __name__ == '__main__':
    if not predictor.model_loaded:
        print("Warning: Model not loaded. Please train the model first by running train_model.py")
    
    app.run(debug=True, host='0.0.0.0', port=5000)