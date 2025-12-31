from ayurvedic_predictor import AyurvedicPredictor
from dataset_creator import AyurvedicDatasetCreator
import pandas as pd

def main():
    """Main training script"""
    
    print("="*60)
    print("AYURVEDIC HEALTH MONITORING SYSTEM - MODEL TRAINING")
    print("="*60)
    
    # Step 1: Create dataset
    print("\n1. Creating dataset...")
    creator = AyurvedicDatasetCreator()
    dataset = creator.create_comprehensive_dataset('symptoms_dataset.csv')
    
    # Step 2: Train model
    print("\n2. Training machine learning model...")
    predictor = AyurvedicPredictor()
    predictor.train_model('symptoms_dataset.csv')
    
    # Step 3: Load model and test
    print("\n3. Testing trained model...")
    predictor.load_model()
    
    # Test cases based on traditional Ayurvedic knowledge
    test_cases = [
        {
            "name": "Classic Vata Case",
            "symptoms": ["dry skin", "constipation", "anxiety", "joint pain", "irregular digestion", "insomnia"]
        },
        {
            "name": "Classic Pitta Case", 
            "symptoms": ["acidity", "burning sensation", "anger", "excessive heat", "skin inflammation", "yellow urine"]
        },
        {
            "name": "Classic Kapha Case",
            "symptoms": ["congestion", "weight gain", "lethargy", "cold limbs", "excessive sleep", "sluggishness"]
        },
        {
            "name": "Mixed Vata-Pitta",
            "symptoms": ["anxiety", "dry skin", "acidity", "irritability", "joint pain"]
        },
        {
            "name": "Non-Ayurvedic Symptoms",
            "symptoms": ["broken bone", "car accident", "appendicitis", "covid symptoms"]
        },
        {
            "name": "Modern Stress Case",
            "symptoms": ["headache", "fatigue", "stress", "muscle tension"]
        }
    ]
    
    print("\n" + "="*60)
    print("TEST RESULTS")
    print("="*60)
    
    for test_case in test_cases:
        print(f"\n🔍 {test_case['name']}")
        print(f"Input symptoms: {test_case['symptoms']}")
        
        result = predictor.predict(test_case['symptoms'])
        
        print(f"🎯 Prediction: {result['prediction']}")
        print(f"📊 Confidence: {result['confidence']}")
        print(f"📈 Percentages:")
        for dosha, percentage in result['dosha_percentages'].items():
            print(f"   - {dosha.upper()}: {percentage}%")
        print(f"💡 Recommendation: {result['recommendation']}")
        print("-" * 60)
    
    print(f"\n✅ Training completed successfully!")
    print(f"📁 Model saved as: ayurvedic_classifier.pkl")
    print(f"📁 Vectorizer saved as: symptoms_vectorizer.pkl") 
    print(f"📁 Dataset saved as: symptoms_dataset.csv")

if __name__ == "__main__":
    main()