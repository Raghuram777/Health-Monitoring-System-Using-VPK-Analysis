import pandas as pd
import numpy as np
from typing import List, Dict

class AyurvedicDatasetCreator:
    def __init__(self):
        """
        Create dataset based on Ayurvedic principles from Charaka Samhita
        and traditional Ayurvedic knowledge
        """
        
        # Vata (Vatham) symptoms - Air and Space elements
        self.vata_symptoms = [
            "dry skin", "constipation", "anxiety", "joint pain", "irregular digestion",
            "insomnia", "nervousness", "dizziness", "trembling", "muscle twitches",
            "cold hands feet", "dry cough", "hoarse voice", "cracking joints",
            "restlessness", "worry", "fear", "confusion", "memory loss",
            "thin body", "weight loss", "bloating", "gas formation", "abdominal pain",
            "irregular appetite", "scanty urination", "dry hair", "brittle nails",
            "rough skin", "premature aging", "wrinkles", "stiffness", "arthritis",
            "sciatica", "paralysis", "convulsions", "epilepsy", "depression mood swings",
            "rapid speech", "talkativeness", "hyperactivity", "palpitations",
            "irregular heartbeat", "low blood pressure", "fainting", "weakness",
            "fatigue", "exhaustion", "noise sensitivity", "light sensitivity",
            "touch sensitivity", "irregular menstruation", "painful periods",
            "dry vagina", "premature ejaculation", "impotence", "infertility"
        ]
        
        # Pitta (Pitham) symptoms - Fire and Water elements  
        self.pitta_symptoms = [
            "acidity", "burning sensation", "anger", "skin inflammation", "excessive heat",
            "irritability", "impatience", "jealousy", "criticism", "perfectionism",
            "hyperacidity", "heartburn", "ulcers", "diarrhea", "loose stools",
            "yellow urine", "excessive urination", "sweating", "body odor",
            "premature graying", "baldness", "red eyes", "yellow eyes",
            "skin rashes", "acne", "eczema", "psoriasis", "hives",
            "fever", "inflammation", "infection", "boils", "abscesses",
            "excessive appetite", "thirst", "craving cold drinks", "aversion to heat",
            "yellow complexion", "red complexion", "hot flashes", "night sweats",
            "sharp hunger", "cannot skip meals", "nausea", "vomiting bile",
            "bitter taste", "sour taste", "metallic taste", "bleeding gums",
            "nose bleeding", "heavy periods", "early periods", "red blood",
            "hypertension", "migraine", "tension headache", "eye strain",
            "photophobia", "conjunctivitis", "stye", "visual disturbances",
            "liver disorders", "gallbladder problems", "jaundice", "hepatitis"
        ]
        
        # Kapha (Kapham) symptoms - Water and Earth elements
        self.kapha_symptoms = [
            "congestion", "weight gain", "lethargy", "cold limbs", "excessive sleep",
            "sluggishness", "heaviness", "dullness", "attachment", "greed",
            "possessiveness", "depression", "lack motivation", "procrastination",
            "excess mucus", "phlegm", "cough with mucus", "runny nose",
            "sinus congestion", "post nasal drip", "allergies", "asthma",
            "bronchitis", "pneumonia", "fluid retention", "swelling", "edema",
            "obesity", "slow digestion", "slow metabolism", "nausea after eating",
            "sweet taste mouth", "excess saliva", "thick white coating tongue",
            "pale skin", "oily skin", "large pores", "thick hair", "oily hair",
            "slow healing", "slow movements", "slow speech", "monotone voice",
            "cold skin", "cold extremities", "low body temperature", "feeling cold",
            "high cholesterol", "diabetes", "hypothyroid", "low blood pressure",
            "slow pulse", "regular appetite", "craving sweets", "craving dairy",
            "difficulty waking", "oversleeping", "daytime sleepiness", "mental fog",
            "slow comprehension", "good memory", "loyal nature", "calm disposition",
            "delayed periods", "heavy periods", "white discharge", "cysts", "tumors"
        ]

    def generate_symptom_combinations(self, symptoms: List[str], dosha: str, num_combinations: int = 50) -> List[Dict]:
        """Generate realistic symptom combinations for a dosha"""
        combinations = []
        
        for _ in range(num_combinations):
            # Random number of symptoms (2-8 symptoms per case)
            num_symptoms = np.random.randint(2, 9)
            
            # Select random symptoms
            selected_symptoms = np.random.choice(symptoms, num_symptoms, replace=False)
            
            # Join symptoms into a string
            symptom_text = ' '.join(selected_symptoms)
            
            combinations.append({
                'symptoms': symptom_text,
                'dosha': dosha,
                'num_symptoms': num_symptoms
            })
            
        return combinations

    def create_mixed_combinations(self, num_combinations: int = 30) -> List[Dict]:
        """Create combinations that mix symptoms from different doshas"""
        combinations = []
        
        all_symptoms = {
            'vata': self.vata_symptoms,
            'pitta': self.pitta_symptoms, 
            'kapha': self.kapha_symptoms
        }
        
        for _ in range(num_combinations):
            # Choose primary dosha (60-80% of symptoms)
            primary_dosha = np.random.choice(['vata', 'pitta', 'kapha'])
            
            # Choose number of symptoms
            total_symptoms = np.random.randint(3, 8)
            primary_count = int(total_symptoms * np.random.uniform(0.6, 0.8))
            secondary_count = total_symptoms - primary_count
            
            # Select primary symptoms
            primary_symptoms = np.random.choice(
                all_symptoms[primary_dosha], 
                primary_count, 
                replace=False
            ).tolist()
            
            # Select secondary symptoms from other doshas
            secondary_doshas = [d for d in all_symptoms.keys() if d != primary_dosha]
            secondary_dosha = np.random.choice(secondary_doshas)
            
            secondary_symptoms = np.random.choice(
                all_symptoms[secondary_dosha],
                secondary_count,
                replace=False
            ).tolist()
            
            # Combine symptoms
            all_case_symptoms = primary_symptoms + secondary_symptoms
            np.random.shuffle(all_case_symptoms)
            
            symptom_text = ' '.join(all_case_symptoms)
            
            combinations.append({
                'symptoms': symptom_text,
                'dosha': primary_dosha,
                'num_symptoms': total_symptoms,
                'mixed': True
            })
            
        return combinations

    def create_no_match_cases(self, num_cases: int = 20) -> List[Dict]:
        """Create cases that shouldn't match any dosha"""
        no_match_symptoms = [
            "broken bone", "car accident", "gunshot wound", "appendicitis",
            "heart attack", "stroke", "cancer tumor", "chemotherapy side effects",
            "surgical complications", "antibiotic reaction", "food poisoning bacteria",
            "viral pneumonia", "covid symptoms", "influenza fever",
            "malaria parasites", "dengue fever", "typhoid bacteria",
            "kidney stones", "gallstones", "herniated disc",
            "torn ligament", "fractured skull", "concussion brain injury",
            "spinal cord injury", "nerve damage", "muscle tear",
            "dislocated shoulder", "tennis elbow", "carpal tunnel syndrome",
            "sports injury", "workplace accident", "burn injury"
        ]
        
        combinations = []
        
        for _ in range(num_cases):
            num_symptoms = np.random.randint(1, 4)
            selected_symptoms = np.random.choice(no_match_symptoms, num_symptoms, replace=False)
            symptom_text = ' '.join(selected_symptoms)
            
            combinations.append({
                'symptoms': symptom_text,
                'dosha': 'no_match',
                'num_symptoms': num_symptoms
            })
            
        return combinations

    def create_comprehensive_dataset(self, output_file: str = 'symptoms_dataset.csv'):
        """Create a comprehensive dataset for training"""
        
        print("Creating Ayurvedic symptoms dataset...")
        
        all_data = []
        
        # Generate pure dosha cases
        vata_cases = self.generate_symptom_combinations(self.vata_symptoms, 'vata', 80)
        pitta_cases = self.generate_symptom_combinations(self.pitta_symptoms, 'pitta', 80)
        kapha_cases = self.generate_symptom_combinations(self.kapha_symptoms, 'kapha', 80)
        
        # Generate mixed cases
        mixed_cases = self.create_mixed_combinations(60)
        
        # Generate no-match cases
        no_match_cases = self.create_no_match_cases(30)
        
        # Combine all cases
        all_data.extend(vata_cases)
        all_data.extend(pitta_cases) 
        all_data.extend(kapha_cases)
        all_data.extend(mixed_cases)
        all_data.extend(no_match_cases)
        
        # Create DataFrame
        df = pd.DataFrame(all_data)
        
        # Shuffle the data
        df = df.sample(frac=1).reset_index(drop=True)
        
        # Save to CSV
        df.to_csv(output_file, index=False)
        
        print(f"Dataset created successfully!")
        print(f"Total records: {len(df)}")
        print(f"Dosha distribution:")
        print(df['dosha'].value_counts())
        print(f"Saved to: {output_file}")
        
        return df

    def add_expert_cases(self) -> List[Dict]:
        """Add expert-curated cases based on classical Ayurvedic texts"""
        expert_cases = [
            # Classic Vata cases
            {
                'symptoms': 'dry skin constipation joint pain anxiety irregular digestion insomnia',
                'dosha': 'vata'
            },
            {
                'symptoms': 'nervousness trembling cold hands feet dry cough restlessness memory loss',
                'dosha': 'vata'
            },
            {
                'symptoms': 'weight loss bloating gas formation abdominal pain irregular appetite',
                'dosha': 'vata'
            },
            
            # Classic Pitta cases  
            {
                'symptoms': 'acidity heartburn anger excessive heat irritability yellow urine',
                'dosha': 'pitta'
            },
            {
                'symptoms': 'skin inflammation burning sensation fever red eyes excessive sweating',
                'dosha': 'pitta'
            },
            {
                'symptoms': 'ulcers diarrhea sharp hunger bitter taste excessive thirst',
                'dosha': 'pitta'
            },
            
            # Classic Kapha cases
            {
                'symptoms': 'congestion weight gain lethargy excessive sleep cold limbs sluggishness',
                'dosha': 'kapha'
            },
            {
                'symptoms': 'excess mucus cough with mucus runny nose slow digestion sweet taste mouth',
                'dosha': 'kapha'
            },
            {
                'symptoms': 'fluid retention swelling obesity slow metabolism oily skin thick hair',
                'dosha': 'kapha'
            }
        ]
        
        return expert_cases

# Create dataset when script is run directly
if __name__ == "__main__":
    creator = AyurvedicDatasetCreator()
    dataset = creator.create_comprehensive_dataset()
    
    print("\nSample records:")
    print(dataset.head(10))
    
    print(f"\nDataset statistics:")
    print(f"Shape: {dataset.shape}")
    print(f"Columns: {list(dataset.columns)}")
    
    # Show some examples from each dosha
    print(f"\nExample Vata case:")
    vata_example = dataset[dataset['dosha'] == 'vata'].iloc[0]
    print(f"Symptoms: {vata_example['symptoms']}")
    
    print(f"\nExample Pitta case:")
    pitta_example = dataset[dataset['dosha'] == 'pitta'].iloc[0]
    print(f"Symptoms: {pitta_example['symptoms']}")
    
    print(f"\nExample Kapha case:")
    kapha_example = dataset[dataset['dosha'] == 'kapha'].iloc[0]
    print(f"Symptoms: {kapha_example['symptoms']}")