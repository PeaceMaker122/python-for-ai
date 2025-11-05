##############################################
# SECTION 3: LISTS OF DICTIONARIES - AI DATASETS
##############################################

print("SECTION 3: LISTS OF DICTIONARIES - AI DATASETS")

print("\n1. FROM ONE PATIENT TO MANY PATIENTS:")
# What we had - one patient
single_patient = {
    "name": "James Beans",
    "age": 45,
    "temperature": 98.6,
    "symptoms": ["fatigue", "headache"]
}

print("Single patient:", single_patient["name"])



print("\n2. CREATING A REAL AI DATASET:")

# Multiple patients - this is how real AI datasets look!
patients = [
    {"name": "James Beans", "age": 45, "temperature": 98.6, "symptoms": ["fatigue", "headache"]},
    {"name": "Sarah Jackson", "age": 32, "temperature": 99.1, "symptoms": ["cough", "fever"]},
    {"name": "Raj Patel", "age": 28, "temperature": 97.8, "symptoms": ["fatigue"]}
]

print("Dataset created with", len(patients), "patients")

print("\n3. ACCESSING DATASET:")

print("First patient name:", patients[0]["name"])
print("Second patient age:", patients[1]["age"])
print("Third patient symptoms:", patients[2]["symptoms"])

print("✅ This is how real AI datasets work!")

# Netflix

netflix = [
    {"user_id": 123, "age": 22, "genre_watched": ["action", "comedy"]}
]

# Bank

bank = [
    {"transaction_id": "T01", "amount": 100.00, "location": "London", "time": "12:00"}
]