##################################################
# PYTHON FOR AI: LESSON 1 - FUNDAMENTALS
##################################################


# Section 1: Basic Data Types for AI
print("SECTION 1: BASIC DATA TYPES FOR AI")
print("----------------------------------")


# 1.1 Numbers - for measurements, counts, predictions
temperature = 98.6  # Floating-point number
patient_count = 5000  # Integer

print("Temperature:", temperature, "Type:", type(temperature))
print("Patient count:", patient_count, "Type:", type(patient_count))


# 1.2 Strings - for text and labels
patient_name = "John Doe"
diagnosis = "Pneumonia"

print("Patient name:", patient_name, "Type:", type(patient_name))
print("Diagnosis:", diagnosis, "Type:", type(diagnosis))


# 1.3 Booleans - for true/false conditions
is_alive = True
is_recovered = False

print("Is alive:", is_alive, "Type:", type(is_alive))
print("Is recovered:", is_recovered, "Type:", type(is_recovered))




# Section 2: Data Structures for AI
print("SECTION 2: DATA STRUCTURES FOR AI")
print("----------------------------------")


# 2.1 Lists - for collections of items
patients = ["John Doe", "Jane Doe", "Bob Doe"]
print("Patients:", patients)


# 2.2 Tuples - for immutable collections
patient_data = ("John Doe", 98.6, "Pneumonia")
print("Patient data:", patient_data)


# 2.3 Dictionaries - for key-value pairs
patient_info = {"name": "John Doe", "temperature": 98.6, "diagnosis": "Pneumonia"}
print("Patient info:", patient_info)




# Section 3: Control Flow for AI
print("SECTION 3: CONTROL FLOW FOR AI")
print("----------------------------------")


# 3.1 If statements - for conditional logic
if temperature > 100:
    print("Fever")
else:
    print("Normal temperature")


# 3.2 For loops - for iterating over collections
for patient in patients:
    print("Patient:", patient)


# 3.3 While loops - for repeating actions
while patient_count > 0:
    print("Patient count:", patient_count)
    patient_count -= 1




# Section 4: Functions for AI
print("SECTION 4: FUNCTIONS FOR AI")
print("----------------------------------")


# 4.1 Built-in functions
print("Length of patients:", len(patients))
print("Max temperature:", max(temperature))
print("Min temperature:", min(temperature))


# 4.2 Custom functions
def diagnose_patient(patient_name, temperature):
    if temperature > 100:
        return "Fever"
    else:
        return "Normal temperature"

print("Diagnosis:", diagnose_patient("John Doe", 98.6))