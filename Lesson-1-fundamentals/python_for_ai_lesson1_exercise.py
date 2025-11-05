
#############################################
# EXERCISE: BASIC DATA TYPES FOR AI
#############################################

print("EXERCISE: BASIC DATA TYPES FOR AI")
print("==================================")

# TODO 1: Create variables for a new patient

# Create the following variables:
# - patient_age (integer): 34
# - patient_weight (float): 72.5
# - patient_id (string): "P12345"
# - diagnosis (string): "Hypertension"

# Your code here:

patient_age = 34
patient_weight = 72.5
patient_id = "P12345"
diagnosis = "Hypertension"

print("Patient created:")
print(f"Age: {patient_age}, Weight: {patient_weight}, ID: {patient_id}, Diagnosis: {diagnosis}")
# TODO 2: Create lists for multiple patients

# Create the following lists:
# - ages: [34, 45, 28, 67, 52]
# - weights: [72.5, 80.2, 65.0, 78.9, 70.1]
# - patient_ids: ["P12345", "P12346", "P12347", "P12348", "P12349"]

# Your code here:

ages = [34, 45, 28, 67, 52]
weights = [72.5, 80.2, 65.0, 78.9, 70.1]
patient_ids = ["P12345", "P12346", "P12347", "P12348", "P12349"]

print(f"\nCreated data for {len(ages)} patients")

# TODO 3: Practice accessing list data

# Print the following:
# - The first patient's age
# - The last patient's weight
# - The total number of patients
# - The middle patient's ID (hint: use index 2)

# Your code here:

print("\nAccessing list data:")
print("\nFirst patient's age:", ages[0])
print("Last patient's weight:", weights[-1])
print("Total number of patients:", len(patient_ids))
print("Middle patient's ID:", patient_ids[2])

# TODO 4: Simple data analysis

# Calculate and print:
# - The average age (hint: use sum() and len())
# - Whether any patient weighs more than 75kg
# - How many patient IDs start with "P123"

# Your code here:

print("\nData analysis:")
average_age = sum(ages) / len(ages)
print("Average age:", round(average_age, 1))

any_over_75kg = any(weight > 75 for weight in weights)
print("Any patient over 75kg?", any_over_75kg)

count_ids_starting_P123 = sum(1 for pid in patient_ids if pid.startswith("P123"))
print("Count of patient IDs starting with 'P123':", count_ids_starting_P123)

print("\n✅ Exercise Complete!")