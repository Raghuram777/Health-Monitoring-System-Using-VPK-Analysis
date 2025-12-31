import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
import json
from typing import List, Dict, Tuple

class AyurvedicPredictor:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
        self.classifier = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model_loaded = False
        
        # Threshold for prediction confidence
        self.confidence_threshold = 0.3
        
    def load_data(self, csv_path: str = 'symptoms_dataset.csv') -> pd.DataFrame:
        """Load the symptoms dataset"""
        try:
            df = pd.read_csv(csv_path)
            print(f"Dataset loaded successfully with {len(df)} records")
            return df
        except FileNotFoundError:
            print("Dataset not found. Please run dataset_creator.py first.")
            return None
            
    def preprocess_symptoms(self, symptoms: List[str]) -> str:
        """Convert list of symptoms to a single string"""
        return ' '.join(symptoms).lower()
        
    def train_model(self, csv_path: str = 'symptoms_dataset.csv'):
        """Train the machine learning model"""
        df = self.load_data(csv_path)
        if df is None:
            return
            
        # Prepare features and labels
        X = df['symptoms'].values
        y = df['dosha'].values
        
        # Vectorize the symptoms text
        X_vectorized = self.vectorizer.fit_transform(X)
        
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(
            X_vectorized, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Train the classifier
        self.classifier.fit(X_train, y_train)
        
        # Evaluate the model
        y_pred = self.classifier.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        print(f"Model trained successfully!")
        print(f"Accuracy: {accuracy:.2f}")
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))
        
        # Save the model and vectorizer
        self.save_model()
        
    def save_model(self):
        """Save the trained model and vectorizer"""
        joblib.dump(self.classifier, 'ayurvedic_classifier.pkl')
        joblib.dump(self.vectorizer, 'symptoms_vectorizer.pkl')
        print("Model and vectorizer saved successfully!")
        
    def load_model(self):
        """Load the trained model and vectorizer"""
        try:
            self.classifier = joblib.load('ayurvedic_classifier.pkl')
            self.vectorizer = joblib.load('symptoms_vectorizer.pkl')
            self.model_loaded = True
            print("Model loaded successfully!")
        except FileNotFoundError:
            print("Model files not found. Please train the model first.")
            self.model_loaded = False
            
    def predict(self, symptoms: List[str]) -> Dict[str, any]:
        """
        Predict dosha based on symptoms
        
        Args:
            symptoms: List of symptom strings
            
        Returns:
            Dictionary with prediction results
        """
        if not self.model_loaded:
            return {"error": "Model not loaded. Please load model first."}
            
        # Preprocess symptoms
        symptoms_text = self.preprocess_symptoms(symptoms)
        
        # Vectorize symptoms
        symptoms_vectorized = self.vectorizer.transform([symptoms_text])
        
        # Get prediction probabilities
        probabilities = self.classifier.predict_proba(symptoms_vectorized)[0]
        
        # Get class names
        classes = self.classifier.classes_
        
        # Create result dictionary
        dosha_probabilities = {}
        for i, dosha in enumerate(classes):
            dosha_probabilities[dosha] = round(probabilities[i] * 100, 2)
            
        # Find the best prediction
        max_prob_idx = np.argmax(probabilities)
        best_dosha = classes[max_prob_idx]
        best_probability = probabilities[max_prob_idx]
        
        # Check if prediction is confident enough
        if best_probability < self.confidence_threshold:
            prediction = "not vatham pitham or kapham"
            confidence = "Low confidence - symptoms don't clearly match known patterns"
        else:
            prediction = best_dosha
            confidence = f"{best_probability * 100:.2f}%"
            
        return {
            "prediction": prediction,
            "confidence": confidence,
            "dosha_percentages": dosha_probabilities,
            "symptoms_analyzed": symptoms,
            "recommendation": self._get_recommendation(prediction, symptoms)
        }
        
    def _get_recommendation(self, dosha: str, symptoms: List[str] = None) -> Dict[str, any]:
        """Get personalized recommendations based on dosha and symptoms"""
        
        # Symptom-specific recommendations database
        symptom_recommendations = {
            'dry skin': {
                'vata': 'Apply warm sesame oil massage daily, use oil-based moisturizers',
                'remedy': 'Stay hydrated, consume healthy fats like ghee and nuts'
            },
            'constipation': {
                'vata': 'Drink warm water in morning, consume fiber-rich foods, take triphala at night',
                'remedy': 'Include cooked vegetables, warm soups, and avoid cold/dry foods'
            },
            'anxiety': {
                'vata': 'Practice meditation and pranayama, maintain regular sleep schedule',
                'remedy': 'Use calming herbs like ashwagandha, reduce caffeine intake'
            },
            'joint pain': {
                'vata': 'Perform gentle yoga, apply warm oil massage on affected joints',
                'remedy': 'Consume turmeric milk, avoid cold and raw foods'
            },
            'acidity': {
                'pitta': 'Avoid spicy, oily, and fried foods, eat cooling foods like cucumber',
                'remedy': 'Drink coconut water, consume aloe vera juice before meals'
            },
            'anger': {
                'pitta': 'Practice cooling pranayama (sitali), avoid heated arguments',
                'remedy': 'Use cooling herbs like coriander, reduce exposure to heat and sun'
            },
            'burning sensation': {
                'pitta': 'Consume cooling foods like buttermilk, avoid hot spices',
                'remedy': 'Apply cooling sandalwood paste, drink plenty of water'
            },
            'inflammation': {
                'pitta': 'Use anti-inflammatory herbs like turmeric and neem',
                'remedy': 'Avoid acidic foods, consume sweet fruits and vegetables'
            },
            'congestion': {
                'kapha': 'Perform steam inhalation with eucalyptus, avoid dairy products',
                'remedy': 'Drink warm ginger tea, use black pepper in meals'
            },
            'weight gain': {
                'kapha': 'Increase physical activity, eat light and warm foods',
                'remedy': 'Avoid heavy, oily foods, practice intermittent fasting'
            },
            'lethargy': {
                'kapha': 'Wake up before sunrise, engage in vigorous exercise',
                'remedy': 'Consume stimulating spices like ginger, reduce daytime sleep'
            },
            'cold limbs': {
                'kapha': 'Keep body warm, perform active movements',
                'remedy': 'Drink warm beverages, use warming spices in cooking'
            },
            'headache': {
                'all': 'Apply cooling paste on forehead, practice pranayama',
                'remedy': 'Stay hydrated, get adequate rest, avoid stress triggers'
            },
            'fatigue': {
                'all': 'Ensure proper sleep, consume nutritious meals',
                'remedy': 'Practice yoga, take adaptogenic herbs like ashwagandha'
            },
            'insomnia': {
                'vata': 'Establish regular sleep routine, drink warm milk with nutmeg',
                'remedy': 'Practice relaxation techniques, avoid screens before bed'
            },
            'excessive heat': {
                'pitta': 'Stay in cool environment, avoid sun exposure during peak hours',
                'remedy': 'Consume cooling beverages, apply sandalwood paste'
            },
            'excessive sleep': {
                'kapha': 'Reduce sleep duration gradually, establish wake-up routine',
                'remedy': 'Avoid heavy meals at night, practice morning exercises'
            },
            'irregular digestion': {
                'vata': 'Eat at regular times, consume warm cooked meals',
                'remedy': 'Use digestive spices like cumin, avoid eating in stress'
            }
        }
        
        # Base recommendations by dosha
        base_recommendations = {
            "vata": {
                "diet": [
                    "Favor warm, cooked, and nourishing foods",
                    "Include sweet, sour, and salty tastes",
                    "Consume healthy fats like ghee, nuts, and seeds",
                    "Avoid cold, raw, and dry foods",
                    "Eat at regular times"
                ],
                "lifestyle": [
                    "Maintain regular daily routines",
                    "Practice oil massage (abhyanga) with warm sesame oil",
                    "Ensure adequate rest and avoid overexertion",
                    "Keep warm and avoid cold, windy environments",
                    "Practice calming yoga and meditation"
                ],
                "herbs": ["Ashwagandha", "Triphala", "Brahmi", "Shatavari"],
                "yoga": ["Gentle stretching", "Grounding poses", "Forward bends", "Restorative yoga"]
            },
            "pitta": {
                "diet": [
                    "Favor cool, fresh, and sweet foods",
                    "Include bitter and astringent tastes",
                    "Consume cooling vegetables like cucumber, leafy greens",
                    "Avoid spicy, oily, fried, and acidic foods",
                    "Drink plenty of water and coconut water"
                ],
                "lifestyle": [
                    "Avoid excessive heat and sun exposure",
                    "Practice stress management techniques",
                    "Engage in moderate, not competitive exercise",
                    "Take cool showers and wear cooling colors",
                    "Maintain work-life balance"
                ],
                "herbs": ["Neem", "Coriander", "Aloe vera", "Amla"],
                "yoga": ["Cooling pranayama", "Moon salutations", "Gentle backbends", "Meditation"]
            },
            "kapha": {
                "diet": [
                    "Favor light, warm, and dry foods",
                    "Include pungent, bitter, and astringent tastes",
                    "Consume stimulating spices like ginger, black pepper",
                    "Avoid heavy, oily, and dairy-rich foods",
                    "Reduce portion sizes and avoid overeating"
                ],
                "lifestyle": [
                    "Engage in regular vigorous exercise",
                    "Wake up early, preferably before sunrise",
                    "Perform dry massage (garshana)",
                    "Stay active and avoid excessive sleep",
                    "Seek variety and new experiences"
                ],
                "herbs": ["Trikatu", "Guggulu", "Turmeric", "Tulsi"],
                "yoga": ["Vigorous vinyasa", "Sun salutations", "Backbends", "Inversions"]
            }
        }
        
        if dosha == "not vatham pitham or kapham":
            return {
                "general": "Your symptoms don't clearly match traditional Ayurvedic dosha patterns. This could indicate a complex imbalance or non-Ayurvedic condition.",
                "advice": "We strongly recommend consulting with a qualified Ayurvedic practitioner for personalized assessment and treatment plan.",
                "note": "Professional guidance is essential for accurate diagnosis and treatment."
            }
        
        # Get base recommendations
        base = base_recommendations.get(dosha, {})
        
        # Collect symptom-specific recommendations
        specific_recommendations = []
        remedies = []
        
        if symptoms:
            for symptom in symptoms:
                symptom_lower = symptom.lower()
                if symptom_lower in symptom_recommendations:
                    rec = symptom_recommendations[symptom_lower]
                    if dosha in rec:
                        specific_recommendations.append(f"For {symptom}: {rec[dosha]}")
                    elif 'all' in rec:
                        specific_recommendations.append(f"For {symptom}: {rec['all']}")
                    if 'remedy' in rec:
                        remedies.append(f"• {symptom.capitalize()}: {rec['remedy']}")
        
        return {
            "dosha": dosha.upper(),
            "diet": base.get("diet", []),
            "lifestyle": base.get("lifestyle", []),
            "herbs": base.get("herbs", []),
            "yoga": base.get("yoga", []),
            "specific_recommendations": specific_recommendations if specific_recommendations else ["Maintain balanced lifestyle according to general dosha guidelines"],
            "remedies": remedies if remedies else ["Follow general dosha-balancing practices"],
            "note": f"These recommendations are for balancing {dosha.upper()} dosha. Always consult an Ayurvedic practitioner for personalized treatment."
        }
        
    def predict_batch(self, symptoms_list: List[List[str]]) -> List[Dict[str, any]]:
        """Predict dosha for multiple symptom sets"""
        results = []
        for symptoms in symptoms_list:
            result = self.predict(symptoms)
            results.append(result)
        return results

# Example usage
if __name__ == "__main__":
    predictor = AyurvedicPredictor()
    
    # Try to load existing model
    predictor.load_model()
    
    if not predictor.model_loaded:
        print("Training new model...")
        predictor.train_model()
        predictor.load_model()
    
    # Test predictions
    test_symptoms = [
        ["dry skin", "constipation", "anxiety", "joint pain"],
        ["acidity", "burning sensation", "anger", "skin inflammation"],
        ["congestion", "weight gain", "lethargy", "cold hands"],
        ["headache", "fever", "unknown symptom"]
    ]
    
    print("\n" + "="*50)
    print("AYURVEDIC DISEASE PREDICTION")
    print("="*50)
    
    for i, symptoms in enumerate(test_symptoms, 1):
        print(f"\nTest Case {i}: {symptoms}")
        result = predictor.predict(symptoms)
        print(f"Prediction: {result['prediction']}")
        print(f"Confidence: {result['confidence']}")
        print(f"Dosha Percentages: {result['dosha_percentages']}")
        print(f"Recommendation: {result['recommendation']}")
        print("-" * 30)