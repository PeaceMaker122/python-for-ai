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



# Section 1.2: Basic Data Types for AI - Strings
print("SECTION 1.2: Strings")
print("-----------------------------------")

# 1.2.1 Text - for language processing, classification
patient_name = "John Smith"
medical_notes = "Patient reports feeling tired."

print("\nPatient name:", patient_name, "Type:", type(patient_name))
print("Medical notes:", medical_notes, "Type:", type(medical_notes))



# Section 1.3: Basic Data Types for AI - Lists
print("SECTION 1.3: Lists")
print("-----------------------------------")

# 1.3 Lists - for collections of related items
temperatures = [98.6, 99.1, 97.8, 100.2, 98.7]
patient_names = ["John Smith", "Sarah Johnson", "Raj Patel"]

print("\nTemperatures:", temperatures, "Type:", type(temperatures))
print("First temperature:", temperatures[0])
print("Patient names:", patient_names, "Type:", type(patient_names))
print("Number of patients:", len(patient_names))





# Section 2: From Basic Types to Structured Data
print("\nSECTION 2: FROM BASIC TYPES TO STRUCTURED DATA")
print("==============================================")


# Review: What we've learned so far
print("\n1. BASIC DATA TYPES recap:")
print("Numbers:", 98.6, type(98.6))
print("Strings:", "John Smith", type("John Smith"))
print("Lists:", [98.6, 99.1, 97.8], type([98.6, 99.1, 97.8]))

print("\n2. THE PROBLEM WITH SEPARATE VARIABLES:")


# Separate, disconnected variables
temperature = 98.6
patient_name = "John Smith"
symptoms = ["fatigue", "headache"]

print("Temperature:", temperature)
print("Patient name:", patient_name)
print("Symptoms:", symptoms)
print("❌ Problem: No connection between these pieces of data!")

print("\n3. THE SOLUTION: STRUCTURED DATA")
print("Coming up next: Dictionaries!")