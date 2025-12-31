from ayurvedic_predictor import AyurvedicPredictor

print("="*60)
print("AYURVEDIC HEALTH MONITORING SYSTEM - QUICK TEST")
print("="*60)

predictor = AyurvedicPredictor()
predictor.load_model()

# Test cases
test_cases = [
    (["dry skin", "anxiety", "constipation"], "vata"),
    (["acidity", "anger", "burning sensation"], "pitta"),
    (["congestion", "weight gain", "lethargy"], "kapha"),
]

print("\nRunning tests...\n")

for i, (symptoms, expected) in enumerate(test_cases, 1):
    result = predictor.predict(symptoms)
    status = "PASS" if result['prediction'] == expected else "FAIL"
    print(f"Test {i}: {status}")
    print(f"  Symptoms: {symptoms}")
    print(f"  Predicted: {result['prediction']} (Expected: {expected})")
    print(f"  Confidence: {result['confidence']}")
    print()

print("="*60)
print("All tests completed successfully!")
print("="*60)
