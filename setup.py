#!/usr/bin/env python3
"""
Setup script for Ayurvedic Health Monitoring System
This script will install dependencies, create dataset, train model, and test the system
"""

import os
import sys
import subprocess
import time

def print_header(text):
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)

def print_step(step, text):
    print(f"\n🔸 STEP {step}: {text}")
    print("-" * 40)

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"Running: {description}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ is required")
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def install_dependencies():
    """Install required Python packages"""
    print_step(1, "INSTALLING DEPENDENCIES")
    
    if not run_command("pip install -r requirements.txt", "Installing Python packages"):
        print("\n⚠️ If installation failed, try:")
        print("pip install --upgrade pip")
        print("pip install -r requirements.txt")
        return False
    
    print("\n📦 Installed packages:")
    subprocess.run("pip list | grep -E '(numpy|pandas|sklearn|flask)'", shell=True)
    return True

def create_dataset():
    """Create the Ayurvedic symptoms dataset"""
    print_step(2, "CREATING AYURVEDIC DATASET")
    
    try:
        from dataset_creator import AyurvedicDatasetCreator
        creator = AyurvedicDatasetCreator()
        dataset = creator.create_comprehensive_dataset()
        print(f"✅ Dataset created with {len(dataset)} records")
        return True
    except Exception as e:
        print(f"❌ Dataset creation failed: {e}")
        return False

def train_model():
    """Train the machine learning model"""
    print_step(3, "TRAINING AI MODEL")
    
    try:
        from ayurvedic_predictor import AyurvedicPredictor
        predictor = AyurvedicPredictor()
        predictor.train_model()
        print("✅ Model training completed")
        return True
    except Exception as e:
        print(f"❌ Model training failed: {e}")
        return False

def test_system():
    """Run basic system tests"""
    print_step(4, "TESTING SYSTEM")
    
    try:
        from ayurvedic_predictor import AyurvedicPredictor
        predictor = AyurvedicPredictor()
        predictor.load_model()
        
        if not predictor.model_loaded:
            print("❌ Model not loaded properly")
            return False
        
        # Test prediction
        test_symptoms = ["dry skin", "anxiety", "joint pain"]
        result = predictor.predict(test_symptoms)
        
        print(f"✅ Test prediction: {result['prediction']}")
        print(f"   Confidence: {result['confidence']}")
        print(f"   Percentages: {result['dosha_percentages']}")
        return True
        
    except Exception as e:
        print(f"❌ System test failed: {e}")
        return False

def show_usage_instructions():
    """Show how to use the system"""
    print_step(5, "USAGE INSTRUCTIONS")
    
    print("🚀 Your Ayurvedic Health Monitoring System is ready!")
    print("\n📋 How to use:")
    print("1. Run comprehensive tests:")
    print("   python test_system.py")
    
    print("\n2. Start web interface:")
    print("   python web_app.py")
    print("   Then open: http://localhost:5000")
    
    print("\n3. Use in Python code:")
    print("   from ayurvedic_predictor import AyurvedicPredictor")
    print("   predictor = AyurvedicPredictor()")
    print("   predictor.load_model()")
    print("   result = predictor.predict(['dry skin', 'anxiety'])")
    print("   print(result)")
    
    print("\n4. Interactive demo:")
    print("   python test_system.py demo")
    
    print(f"\n📁 Files created:")
    print(f"   - symptoms_dataset.csv (training data)")
    print(f"   - ayurvedic_classifier.pkl (trained model)")
    print(f"   - symptoms_vectorizer.pkl (text vectorizer)")
    
    print(f"\n🏥 Doshas detected:")
    print(f"   • VATA (Vatham): Air & Space - Movement, nervous system")
    print(f"   • PITTA (Pitham): Fire & Water - Metabolism, digestion")  
    print(f"   • KAPHA (Kapham): Water & Earth - Structure, immunity")
    print(f"   • No match: When symptoms don't clearly match any dosha")

def main():
    """Main setup function"""
    print_header("🕉️ AYURVEDIC HEALTH MONITORING SYSTEM SETUP 🕉️")
    
    print("This system uses AI to predict Ayurvedic doshas based on symptoms.")
    print("Based on traditional knowledge from Charaka Samhita and other texts.")
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Track setup steps
    steps_completed = 0
    total_steps = 4
    
    # Step 1: Install dependencies
    if install_dependencies():
        steps_completed += 1
    else:
        print("\n❌ Setup failed at dependency installation")
        sys.exit(1)
    
    # Step 2: Create dataset
    if create_dataset():
        steps_completed += 1
    else:
        print("\n❌ Setup failed at dataset creation")
        sys.exit(1)
    
    # Step 3: Train model
    if train_model():
        steps_completed += 1
    else:
        print("\n❌ Setup failed at model training")
        sys.exit(1)
    
    # Step 4: Test system
    if test_system():
        steps_completed += 1
    else:
        print("\n❌ Setup failed at system testing")
        sys.exit(1)
    
    # Show final results
    print_header("✅ SETUP COMPLETED SUCCESSFULLY")
    print(f"🎯 {steps_completed}/{total_steps} steps completed")
    
    show_usage_instructions()
    
    # Ask user what to do next
    print("\n" + "="*60)
    print("What would you like to do next?")
    print("1. Run comprehensive tests")
    print("2. Start web interface") 
    print("3. Interactive demo")
    print("4. Exit")
    
    while True:
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "1":
            print("\n🧪 Running comprehensive tests...")
            os.system("python test_system.py")
            break
        elif choice == "2":
            print("\n🌐 Starting web interface...")
            print("Open http://localhost:5000 in your browser")
            os.system("python web_app.py")
            break
        elif choice == "3":
            print("\n🎮 Starting interactive demo...")
            os.system("python test_system.py demo")
            break
        elif choice == "4":
            print("\n👋 Goodbye!")
            break
        else:
            print("Please enter 1, 2, 3, or 4")

if __name__ == "__main__":
    main()