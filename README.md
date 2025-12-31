# Ayurvedic Health Monitoring System (VPK)

A machine learning-based system for predicting Ayurvedic doshas (Vata, Pitta, Kapha) based on symptoms.

## Features

- **Symptom-based Disease Prediction**: Input multiple symptoms and get predictions for Vata, Pitta, or Kapha imbalances
- **Percentage Confidence**: Get probability scores for each dosha
- **No Match Detection**: Returns "not vatham pitham or kapham" when symptoms don't match known patterns
- **Dataset**: Based on Ayurvedic principles from Charaka Samhita and other traditional texts

## Doshas (VPK)

### Vata (Vatham)
- **Elements**: Air and Space
- **Characteristics**: Movement, circulation, breathing, nerve impulses
- **Common symptoms**: Dry skin, constipation, anxiety, joint pain, irregular digestion

### Pitta (Pitham)  
- **Elements**: Fire and Water
- **Characteristics**: Metabolism, digestion, body temperature, intelligence
- **Common symptoms**: Acidity, burning sensation, anger, skin inflammation, excessive heat

### Kapha (Kapham)
- **Elements**: Water and Earth  
- **Characteristics**: Structure, immunity, lubrication, stability
- **Common symptoms**: Congestion, weight gain, lethargy, cold limbs, excessive sleep

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from ayurvedic_predictor import AyurvedicPredictor

predictor = AyurvedicPredictor()
predictor.load_model()

symptoms = ["dry skin", "constipation", "anxiety", "joint pain"]
prediction = predictor.predict(symptoms)
print(prediction)
```

## Files

- `ayurvedic_predictor.py`: Main prediction model
- `dataset_creator.py`: Creates dataset from Ayurvedic knowledge
- `train_model.py`: Trains the machine learning model
- `symptoms_dataset.csv`: Training dataset
- `web_app.py`: Flask web application
- `requirements.txt`: Dependencies