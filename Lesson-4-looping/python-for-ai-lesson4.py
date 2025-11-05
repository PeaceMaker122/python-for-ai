##############################################
# SECTION 4.1: PROCESSING ALL PATIENTS
##############################################

print("SECTION 4.1: PROCESSING ALL PATIENTS")

# Our patient dataset
patients = [
    {"name": "James Beans", "age": 45, "temperature": 98.6, "symptoms": ["fatigue", "headache"]},
    {"name": "Sarah Jackson", "age": 32, "temperature": 99.1, "symptoms": ["cough", "fever"]},
    {"name": "Raj Patel", "age": 28, "temperature": 97.8, "symptoms": ["fatigue"]},
    {"name": "Lisa Chen", "age": 51, "temperature": 100.2, "symptoms": ["fever", "headache"]},
    {"name": "Mike Torres", "age": 39, "temperature": 98.9, "symptoms": ["cough"]}
]

print("Dataset with", len(patients), "patients loaded")

print("\nPROCESSING ALL PATIENTS:")

for patient in patients:
    print(patient["name"], "is", patient["age"], "years old")

print("✅ We just processed every patient in our dataset!")