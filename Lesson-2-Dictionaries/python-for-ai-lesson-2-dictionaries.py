##############################################
# SECTION 2: DICTIONARIES - CONNECTING DATA
##############################################

print("SECTION 2: DICTIONARIES - CONNECTING DATA")
print("==============================================")


print("\n1. THE PROBLEM WITH SEPARATE VARIABLES:")

# What we had before - disconnected data
temperature = 98.6
patient_name = "John Smith"
age = 45
symptoms = ["fatigue", "headache"]

print("Temperature:", temperature)
print("Name:", patient_name)
print("Age:", age)
print("Symptoms:", symptoms)
print("❌ Problem: Which temperature belongs to which patient?")



print("\n2. THE SOLUTION: DICTIONARIES")

# A single patient record as a dictionary
patient = {
    "name": "John Smith",
    "age": 45,
    "temperature": 98.6,
    "symptoms": ["fatigue", "headache", "fever"]
}

print("Patient record:", patient)
print("Patient name:", patient["name"])
print("Patient age:", patient["age"])
print("Patient temperature:", patient["temperature"])
print("First symptom:", patient["symptoms"][0])



# WHAT MAKES DICTIONARIES SPECIAL

# ✅ All related data grouped together
# ✅ Clear labels for each piece of information
# ✅ Easy to access specific data
# ✅ Perfect structure for AI datasets