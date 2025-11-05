#############################################
# EXERCISE SOLUTION: BASIC DATA TYPES FOR AI
#############################################

print("EXERCISE SOLUTION: BASIC DATA TYPES FOR AI")
print("==========================================")

# TODO 1: Create variables for a new patient
patient_age = 34
patient_weight = 72.5
patient_id = "P12345"
diagnosis = "Hypertension"

print("Patient created:")
print(f"Age: {patient_age}, Weight: {patient_weight}, ID: {patient_id}, Diagnosis: {diagnosis}")

# TODO 2: Create lists for multiple patients
ages = [34, 45, 28, 67, 52]
weights = [72.5, 80.2, 65.0, 78.9, 70.1]
patient_ids = ["P12345", "P12346", "P12347", "P12348", "P12349"]

print(f"\nCreated data for {len(ages)} patients")

# TODO 3: Practice accessing list data
print("\nAccessing list data:")
print("First patient's age:", ages[0])
print("Last patient's weight:", weights[-1])
print("Total number of patients:", len(ages))
print("Middle patient's ID:", patient_ids[2])

# TODO 4: Simple data analysis
print("\nData analysis:")
average_age = sum(ages) / len(ages)
print("Average age:", round(average_age, 1))

heavy_patients = [w for w in weights if w > 75]
print("Any patient over 75kg?", len(heavy_patients) > 0)

p123_count = sum(1 for pid in patient_ids if pid.startswith("P123"))
print("Patient IDs starting with 'P123':", p123_count)

print("\n✅ Exercise Complete!")