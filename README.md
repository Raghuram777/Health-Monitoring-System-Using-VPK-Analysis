# Ayurvedic Health Monitoring System (VPK)

A machine learning-based system for predicting Ayurvedic doshas (Vata, Pitta, Kapha) based on symptoms with **dynamic personalized recommendations** and **professional medical-grade UI**.

## ✨ Features

- **🔍 Symptom-based Dosha Analysis**: Input multiple symptoms and get predictions for Vata, Pitta, or Kapha imbalances
- **📊 Percentage Confidence**: Get probability scores for each dosha
- **💡 Dynamic Personalized Recommendations**: Receive tailored advice based on your specific symptoms and dosha
- **🏥 Comprehensive Guidance**: Diet, lifestyle, herbs, yoga practices, and home remedies
- **🎨 Professional Medical-Grade UI**: Modern, clean interface designed for healthcare applications
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices
- **🌿 Ayurvedic Knowledge Base**: Based on traditional principles from Charaka Samhita
- **No Match Detection**: Returns "not vatham pitham or kapham" when symptoms don't match known patterns

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

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Raghuram777/Health-Monitoring-System-Using-VPK-Analysis.git
cd Health-Monitoring-System-Using-VPK-Analysis

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # On Windows
# source .venv/bin/activate  # On Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Train the model (if not already trained)
python train_model.py

# Run the web application
python web_app.py
```

### Access the Application

Open your browser and navigate to:
- **Local**: http://127.0.0.1:5000
- **Network**: http://YOUR_IP:5000

## 📖 Usage

### Web Interface
1. Enter your symptoms using the text input or quick-add buttons
2. Click "Analyze Symptoms & Get Recommendations"
3. View your dosha analysis with personalized recommendations organized in tabs:
   - **Symptom-Specific** advice tailored to your exact symptoms
   - **Diet** guidelines for your dosha
   - **Lifestyle** recommendations
   - **Ayurvedic herbs** to use
   - **Yoga & Exercise** practices

### Python API

```python
from ayurvedic_predictor import AyurvedicPredictor

predictor = AyurvedicPredictor()
predictor.load_model()

symptoms = ["dry skin", "constipation", "anxiety", "joint pain"]
result = predictor.predict(symptoms)

print(f"Prediction: {result['prediction']}")
print(f"Confidence: {result['confidence']}")
print(f"Recommendations: {result['recommendation']}")
```

## 📁 Project Structure

```
├── ayurvedic_predictor.py      # Core prediction engine with ML model
├── dataset_creator.py          # Ayurvedic dataset generator
├── train_model.py             # Model training script
├── web_app.py                 # Flask web application
├── symptoms_dataset.csv       # Training dataset
├── requirements.txt           # Python dependencies
├── templates/
│   └── index.html            # Professional UI with tabbed recommendations
└── README.md                 # Documentation
```

## 🎯 Key Improvements

### Dynamic Recommendation System
- **18+ Symptom Patterns**: Comprehensive database of symptom-specific recommendations
- **Dosha-Specific Advice**: Tailored guidance for Vata, Pitta, and Kapha
- **Home Remedies**: Practical, easy-to-implement solutions
- **Categorized Recommendations**: Diet, lifestyle, herbs, and yoga organized in tabs

### Professional UI Design
- **Medical-Grade Aesthetics**: Clean, trustworthy design with natural color palette
- **Smooth Animations**: Enhanced user experience with CSS transitions
- **Tabbed Interface**: Organized display of comprehensive recommendations
- **Responsive Layout**: Optimized for desktop, tablet, and mobile devices
- **Interactive Elements**: Hover effects, animated progress bars, smooth scrolling

## 🔬 Technology Stack

- **Backend**: Python 3.x, Flask
- **ML Framework**: scikit-learn (Random Forest Classifier)
- **Text Processing**: TF-IDF Vectorization
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Design**: Modern gradients, flexbox/grid layouts, custom animations

## 📊 Model Information

- **Algorithm**: Random Forest Classifier (100 estimators)
- **Features**: TF-IDF vectorization of symptom text
- **Dataset**: Ayurvedic symptom-dosha mappings based on traditional texts
- **Confidence Threshold**: 30% for valid predictions
- **Training Accuracy**: ~85-90% (varies with dataset)

## ⚠️ Important Disclaimer

This system provides general Ayurvedic guidance based on traditional principles and machine learning analysis. **It should not replace professional medical advice.** Always consult:
- Qualified Ayurvedic practitioners for personalized treatment plans
- Licensed healthcare providers for medical conditions and serious symptoms
- Medical professionals before making significant health decisions

## 🤝 Contributing

Contributions are welcome! To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available for educational and research purposes.

## 👨‍💻 Author

**Raghuram**
- GitHub: [@Raghuram777](https://github.com/Raghuram777)

---

**🕉️ Traditional Wisdom Meets Modern Technology**