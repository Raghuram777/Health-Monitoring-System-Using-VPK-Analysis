#!/usr/bin/env python3
"""
Comprehensive test script for the Ayurvedic Health Monitoring System
This script demonstrates all features and validates the AI model
"""

import sys
import os
import json
from ayurvedic_predictor import AyurvedicPredictor
from dataset_creator import AyurvedicDatasetCreator

class AyurvedicSystemTester:
    def __init__(self):
        self.predictor = AyurvedicPredictor()
        self.test_results = []
    
    def run_comprehensive_test(self):
        """Run comprehensive test suite"""
        print("🕉️" + "="*70)
        print("AYURVEDIC HEALTH MONITORING SYSTEM - COMPREHENSIVE TEST")
        print("="*70 + "🕉️")
        
        # Test 1: Model Loading
        self.test_model_loading()
        
        # Test 2: Classic Dosha Cases
        self.test_classic_cases()
        
        # Test 3: Mixed Symptom Cases
        self.test_mixed_cases()
        
        # Test 4: Edge Cases
        self.test_edge_cases()
        
        # Test 5: Batch Prediction
        self.test_batch_prediction()
        
        # Test 6: Performance Analysis
        self.test_performance()
        
        # Final Report
        self.generate_report()
    
    def test_model_loading(self):
        """Test model loading functionality"""
        print("\n🔧 TEST 1: MODEL LOADING")
        print("-" * 40)
        
        try:
            self.predictor.load_model()
            if self.predictor.model_loaded:
                print("✅ Model loaded successfully")
                self.test_results.append({"test": "Model Loading", "status": "PASS"})
            else:
                print("❌ Model loading failed")
                self.test_results.append({"test": "Model Loading", "status": "FAIL"})
        except Exception as e:
            print(f"❌ Model loading error: {e}")
            self.test_results.append({"test": "Model Loading", "status": "FAIL", "error": str(e)})
    
    def test_classic_cases(self):
        """Test classic Ayurvedic cases"""
        print("\n🎯 TEST 2: CLASSIC DOSHA CASES")
        print("-" * 40)
        
        classic_cases = [
            {
                "name": "Pure Vata Case",
                "symptoms": ["dry skin", "constipation", "anxiety", "joint pain", "irregular digestion", "insomnia", "nervousness"],
                "expected": "vata"
            },
            {
                "name": "Pure Pitta Case",
                "symptoms": ["acidity", "burning sensation", "anger", "excessive heat", "skin inflammation", "yellow urine", "irritability"],
                "expected": "pitta"
            },
            {
                "name": "Pure Kapha Case", 
                "symptoms": ["congestion", "weight gain", "lethargy", "cold limbs", "excessive sleep", "sluggishness", "excess mucus"],
                "expected": "kapha"
            }
        ]
        
        for case in classic_cases:
            print(f"\n📋 {case['name']}")
            print(f"Symptoms: {case['symptoms']}")
            
            result = self.predictor.predict(case['symptoms'])
            
            print(f"Prediction: {result['prediction']}")
            print(f"Confidence: {result['confidence']}")
            print(f"Expected: {case['expected']}")
            
            # Check if prediction matches expected
            if result['prediction'] == case['expected']:
                print("✅ CORRECT")
                self.test_results.append({
                    "test": case['name'], 
                    "status": "PASS",
                    "prediction": result['prediction'],
                    "confidence": result['confidence']
                })
            else:
                print("❌ INCORRECT")
                self.test_results.append({
                    "test": case['name'], 
                    "status": "FAIL",
                    "prediction": result['prediction'],
                    "expected": case['expected'],
                    "confidence": result['confidence']
                })
            
            print(f"Percentages: {result['dosha_percentages']}")
    
    def test_mixed_cases(self):
        """Test mixed symptom cases"""
        print("\n🔀 TEST 3: MIXED SYMPTOM CASES")
        print("-" * 40)
        
        mixed_cases = [
            {
                "name": "Vata-Pitta Mix",
                "symptoms": ["anxiety", "dry skin", "acidity", "irritability"],
                "possible": ["vata", "pitta"]
            },
            {
                "name": "Pitta-Kapha Mix",
                "symptoms": ["weight gain", "acidity", "congestion", "anger"],
                "possible": ["pitta", "kapha"]
            },
            {
                "name": "Minimal Symptoms",
                "symptoms": ["headache", "fatigue"],
                "possible": ["vata", "pitta", "kapha", "not vatham pitham or kapham"]
            }
        ]
        
        for case in mixed_cases:
            print(f"\n📋 {case['name']}")
            print(f"Symptoms: {case['symptoms']}")
            
            result = self.predictor.predict(case['symptoms'])
            
            print(f"Prediction: {result['prediction']}")
            print(f"Confidence: {result['confidence']}")
            print(f"Possible outcomes: {case['possible']}")
            
            if result['prediction'] in case['possible']:
                print("✅ ACCEPTABLE")
                self.test_results.append({
                    "test": case['name'], 
                    "status": "PASS",
                    "prediction": result['prediction']
                })
            else:
                print("⚠️ UNEXPECTED")
                self.test_results.append({
                    "test": case['name'], 
                    "status": "UNEXPECTED",
                    "prediction": result['prediction'],
                    "possible": case['possible']
                })
    
    def test_edge_cases(self):
        """Test edge cases and error handling"""
        print("\n🔍 TEST 4: EDGE CASES")
        print("-" * 40)
        
        edge_cases = [
            {
                "name": "Empty Symptoms",
                "symptoms": [],
                "should_error": True
            },
            {
                "name": "Non-Medical Symptoms",
                "symptoms": ["broken bone", "car accident", "gunshot wound"],
                "expected": "not vatham pitham or kapham"
            },
            {
                "name": "Single Symptom",
                "symptoms": ["headache"],
                "possible": ["vata", "pitta", "kapha", "not vatham pitham or kapham"]
            },
            {
                "name": "Duplicate Symptoms",
                "symptoms": ["anxiety", "anxiety", "dry skin", "dry skin"],
                "possible": ["vata", "pitta", "kapha"]
            },
            {
                "name": "Unknown Symptoms",
                "symptoms": ["xyz symptom", "unknown condition", "fake symptom"],
                "expected": "not vatham pitham or kapham"
            }
        ]
        
        for case in edge_cases:
            print(f"\n📋 {case['name']}")
            print(f"Symptoms: {case['symptoms']}")
            
            try:
                result = self.predictor.predict(case['symptoms'])
                
                if case.get('should_error', False):
                    if 'error' in result:
                        print("✅ CORRECTLY HANDLED ERROR")
                        self.test_results.append({"test": case['name'], "status": "PASS"})
                    else:
                        print("❌ SHOULD HAVE ERRORED")
                        self.test_results.append({"test": case['name'], "status": "FAIL"})
                else:
                    print(f"Prediction: {result['prediction']}")
                    print(f"Confidence: {result['confidence']}")
                    
                    if 'expected' in case:
                        if result['prediction'] == case['expected']:
                            print("✅ CORRECT")
                            self.test_results.append({"test": case['name'], "status": "PASS"})
                        else:
                            print("❌ INCORRECT")
                            self.test_results.append({"test": case['name'], "status": "FAIL"})
                    elif 'possible' in case:
                        if result['prediction'] in case['possible']:
                            print("✅ ACCEPTABLE")
                            self.test_results.append({"test": case['name'], "status": "PASS"})
                        else:
                            print("⚠️ UNEXPECTED")
                            self.test_results.append({"test": case['name'], "status": "UNEXPECTED"})
                            
            except Exception as e:
                print(f"Error: {e}")
                self.test_results.append({"test": case['name'], "status": "ERROR", "error": str(e)})
    
    def test_batch_prediction(self):
        """Test batch prediction functionality"""
        print("\n📦 TEST 5: BATCH PREDICTION")
        print("-" * 40)
        
        batch_symptoms = [
            ["dry skin", "anxiety"],
            ["acidity", "anger"],
            ["congestion", "lethargy"],
            ["headache", "unknown symptom"]
        ]
        
        try:
            results = self.predictor.predict_batch(batch_symptoms)
            
            print(f"Processed {len(results)} cases in batch")
            for i, result in enumerate(results):
                print(f"Case {i+1}: {batch_symptoms[i]} → {result['prediction']}")
            
            print("✅ BATCH PREDICTION SUCCESS")
            self.test_results.append({"test": "Batch Prediction", "status": "PASS"})
            
        except Exception as e:
            print(f"❌ Batch prediction failed: {e}")
            self.test_results.append({"test": "Batch Prediction", "status": "FAIL", "error": str(e)})
    
    def test_performance(self):
        """Test system performance"""
        print("\n⚡ TEST 6: PERFORMANCE ANALYSIS")
        print("-" * 40)
        
        import time
        
        test_symptoms = ["dry skin", "constipation", "anxiety", "joint pain"]
        
        # Test response time
        start_time = time.time()
        for _ in range(10):
            self.predictor.predict(test_symptoms)
        end_time = time.time()
        
        avg_time = (end_time - start_time) / 10
        print(f"Average prediction time: {avg_time:.4f} seconds")
        
        if avg_time < 1.0:
            print("✅ PERFORMANCE GOOD")
            self.test_results.append({"test": "Performance", "status": "PASS", "avg_time": avg_time})
        else:
            print("⚠️ PERFORMANCE SLOW")
            self.test_results.append({"test": "Performance", "status": "SLOW", "avg_time": avg_time})
    
    def generate_report(self):
        """Generate final test report"""
        print("\n📊 FINAL TEST REPORT")
        print("=" * 70)
        
        total_tests = len(self.test_results)
        passed_tests = len([r for r in self.test_results if r['status'] == 'PASS'])
        failed_tests = len([r for r in self.test_results if r['status'] == 'FAIL'])
        error_tests = len([r for r in self.test_results if r['status'] == 'ERROR'])
        unexpected_tests = len([r for r in self.test_results if r['status'] == 'UNEXPECTED'])
        
        print(f"Total Tests: {total_tests}")
        print(f"✅ Passed: {passed_tests}")
        print(f"❌ Failed: {failed_tests}")
        print(f"🔥 Errors: {error_tests}")
        print(f"⚠️ Unexpected: {unexpected_tests}")
        
        success_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
        print(f"Success Rate: {success_rate:.1f}%")
        
        if success_rate >= 80:
            print("\n🎉 SYSTEM STATUS: EXCELLENT")
        elif success_rate >= 60:
            print("\n👍 SYSTEM STATUS: GOOD")
        elif success_rate >= 40:
            print("\n⚠️ SYSTEM STATUS: NEEDS IMPROVEMENT")
        else:
            print("\n❌ SYSTEM STATUS: POOR")
        
        # Save detailed results
        with open('test_results.json', 'w') as f:
            json.dump(self.test_results, f, indent=2)
        print("\n📁 Detailed results saved to: test_results.json")

def interactive_demo():
    """Interactive demo for manual testing"""
    print("\n🚀 INTERACTIVE DEMO")
    print("=" * 50)
    
    predictor = AyurvedicPredictor()
    predictor.load_model()
    
    if not predictor.model_loaded:
        print("❌ Model not loaded. Please run train_model.py first.")
        return
    
    print("Enter symptoms separated by commas (or 'quit' to exit)")
    print("Example: dry skin, anxiety, joint pain")
    print("\nCommon symptoms to try:")
    print("Vata: dry skin, constipation, anxiety, joint pain")
    print("Pitta: acidity, anger, burning sensation, yellow urine")
    print("Kapha: congestion, weight gain, lethargy, cold limbs")
    
    while True:
        user_input = input("\n🔍 Enter symptoms: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
        
        if not user_input:
            print("Please enter some symptoms.")
            continue
        
        # Parse symptoms
        symptoms = [s.strip().lower() for s in user_input.split(',') if s.strip()]
        
        if not symptoms:
            print("Please enter valid symptoms.")
            continue
        
        print(f"\nAnalyzing symptoms: {symptoms}")
        
        try:
            result = predictor.predict(symptoms)
            
            print(f"\n🎯 PREDICTION: {result['prediction'].upper()}")
            print(f"🔢 CONFIDENCE: {result['confidence']}")
            print(f"📊 PERCENTAGES:")
            for dosha, percentage in result['dosha_percentages'].items():
                print(f"   {dosha.upper()}: {percentage}%")
            print(f"💡 RECOMMENDATION: {result['recommendation']}")
            
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        interactive_demo()
    else:
        tester = AyurvedicSystemTester()
        tester.run_comprehensive_test()
        
        # Ask user if they want to run interactive demo
        print(f"\nWould you like to run the interactive demo? (y/n): ", end="")
        if input().lower().startswith('y'):
            interactive_demo()