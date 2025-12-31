#!/usr/bin/env python3
"""
Command Line Interface for Ayurvedic Health Monitoring System
Quick and easy way to test symptom predictions
"""

import sys
import argparse
from ayurvedic_predictor import AyurvedicPredictor

def print_dosha_info():
    """Print information about the three doshas"""
    print("\n🕉️ AYURVEDIC DOSHAS (VPK) INFORMATION")
    print("=" * 50)
    
    print("\n🌬️ VATA (Vatham) - Air & Space Elements")
    print("   Governs: Movement, circulation, breathing, nervous system")
    print("   Balanced: Creativity, flexibility, quick thinking")
    print("   Imbalanced: Anxiety, dry skin, constipation, joint pain")
    print("   Common symptoms: dry skin, constipation, anxiety, joint pain,")
    print("                   irregular digestion, insomnia, nervousness")
    
    print("\n🔥 PITTA (Pitham) - Fire & Water Elements")  
    print("   Governs: Metabolism, digestion, body temperature, intelligence")
    print("   Balanced: Good digestion, sharp intellect, courage")
    print("   Imbalanced: Anger, acidity, inflammation, excessive heat")
    print("   Common symptoms: acidity, burning sensation, anger, yellow urine,")
    print("                   skin inflammation, excessive sweating")
    
    print("\n🌊 KAPHA (Kapham) - Water & Earth Elements")
    print("   Governs: Structure, immunity, lubrication, stability")
    print("   Balanced: Strong immunity, calm mind, stable emotions") 
    print("   Imbalanced: Weight gain, lethargy, congestion, depression")
    print("   Common symptoms: congestion, weight gain, lethargy, cold limbs,")
    print("                   excessive sleep, sluggishness")

def format_prediction_result(result):
    """Format prediction result for display"""
    output = []
    
    # Main prediction
    prediction = result['prediction'].upper()
    if prediction == "NOT VATHAM PITHAM OR KAPHAM":
        output.append(f"🔍 PREDICTION: {prediction}")
        output.append("   (Symptoms don't clearly match known Ayurvedic patterns)")
    else:
        dosha_icons = {'VATA': '🌬️', 'PITTA': '🔥', 'KAPHA': '🌊'}
        icon = dosha_icons.get(prediction, '❓')
        output.append(f"🎯 PREDICTION: {icon} {prediction}")
    
    # Confidence
    output.append(f"📊 CONFIDENCE: {result['confidence']}")
    
    # Percentages
    output.append("📈 DOSHA PERCENTAGES:")
    for dosha, percentage in result['dosha_percentages'].items():
        dosha_upper = dosha.upper()
        icon = {'VATA': '🌬️', 'PITTA': '🔥', 'KAPHA': '🌊'}.get(dosha_upper, '❓')
        bars = '█' * int(percentage / 5)  # Visual bar
        output.append(f"   {icon} {dosha_upper:5}: {percentage:5.1f}% {bars}")
    
    # Recommendation
    output.append(f"💡 RECOMMENDATION: {result['recommendation']}")
    
    return '\n'.join(output)

def predict_from_args(predictor, symptoms):
    """Make prediction from command line arguments"""
    print("🔍 ANALYZING SYMPTOMS...")
    print(f"Input: {symptoms}")
    print("-" * 50)
    
    result = predictor.predict(symptoms)
    print(format_prediction_result(result))

def interactive_mode(predictor):
    """Run in interactive mode"""
    print("\n🚀 INTERACTIVE MODE")
    print("=" * 50)
    print("Enter symptoms separated by commas (or 'help' for examples)")
    print("Type 'info' for dosha information, 'quit' to exit")
    
    while True:
        try:
            user_input = input("\n🔍 Enter symptoms: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if user_input.lower() in ['help', 'h']:
                print("\n📝 EXAMPLE SYMPTOM COMBINATIONS:")
                print("Vata: dry skin, anxiety, constipation, joint pain")
                print("Pitta: acidity, anger, burning sensation, yellow urine") 
                print("Kapha: congestion, weight gain, lethargy, cold limbs")
                print("Mixed: headache, fatigue, stress")
                print("Non-Ayurvedic: broken bone, car accident, covid symptoms")
                continue
                
            if user_input.lower() in ['info', 'doshas']:
                print_dosha_info()
                continue
            
            if not user_input:
                print("Please enter some symptoms.")
                continue
            
            # Parse symptoms
            symptoms = [s.strip().lower() for s in user_input.split(',') if s.strip()]
            
            if not symptoms:
                print("Please enter valid symptoms.")
                continue
            
            print(f"\nAnalyzing: {symptoms}")
            print("-" * 50)
            
            result = predictor.predict(symptoms)
            print(format_prediction_result(result))
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(
        description="Ayurvedic Health Monitoring System - Predict doshas from symptoms",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py --symptoms "dry skin" "anxiety" "joint pain"
  python cli.py -s "acidity" "anger" "burning sensation"
  python cli.py --interactive
  python cli.py --info

Doshas:
  VATA (Vatham):  Air & Space - Movement, nervous system
  PITTA (Pitham): Fire & Water - Metabolism, digestion  
  KAPHA (Kapham): Water & Earth - Structure, immunity
        """
    )
    
    parser.add_argument(
        '-s', '--symptoms',
        nargs='+',
        help='List of symptoms to analyze'
    )
    
    parser.add_argument(
        '-i', '--interactive',
        action='store_true',
        help='Run in interactive mode'
    )
    
    parser.add_argument(
        '--info',
        action='store_true',
        help='Show information about doshas'
    )
    
    parser.add_argument(
        '--version',
        action='store_true',
        help='Show version information'
    )
    
    args = parser.parse_args()
    
    # Show version
    if args.version:
        print("Ayurvedic Health Monitoring System v1.0")
        print("Based on traditional Ayurvedic principles from Charaka Samhita")
        return
    
    # Show dosha information
    if args.info:
        print_dosha_info()
        return
    
    # Initialize predictor
    print("🕉️ AYURVEDIC HEALTH MONITORING SYSTEM")
    print("=" * 50)
    print("Loading AI model...")
    
    predictor = AyurvedicPredictor()
    predictor.load_model()
    
    if not predictor.model_loaded:
        print("❌ Model not found. Please run setup.py first to train the model.")
        print("\nTo setup:")
        print("python setup.py")
        return
    
    print("✅ Model loaded successfully!")
    
    # Interactive mode
    if args.interactive:
        interactive_mode(predictor)
        return
    
    # Prediction from arguments
    if args.symptoms:
        symptoms = [s.lower() for s in args.symptoms]
        predict_from_args(predictor, symptoms)
        return
    
    # Default: show help and start interactive mode
    parser.print_help()
    print("\nNo symptoms provided. Starting interactive mode...")
    interactive_mode(predictor)

if __name__ == "__main__":
    main()