#############################################
# EXERCISE: SIMPLE DICTIONARIES
#############################################

print("EXERCISE: SIMPLE DICTIONARIES")
print("==============================")


# TODO 1: Create first patient dictionary

# Create a dictionary called 'patient1' with:

# - name: "Sarah Wilson"
# - age: 29
# - symptoms: ["cough", "fever"]

# Your code here:

patient1 = {
    "name": "Sarah Wilson",
    "age": 29,
    "symptoms": ["cough", "fever"]
}


# TODO 2: Create second patient dictionary  

# Create a dictionary called 'patient2' with:

# - name: "Mike Chen"
# - age: 52
# - symptoms: ["fatigue", "headache"]

# Your code here:

patient2 = {
    "name": "Mike Chen",
    "age": 52,
    "symptoms": ["fatigue", "headache"]
}


# TODO 3: Access and print data

# Print the following:

# - Patient1's name
# - Patient1's age
# - Patient1's symptoms
# - Patient2's name
# - Patient2's age  
# - Patient2's symptoms

# Your code here:

print("Patient 1 Name:", patient1["name"])
print("Patient 1 Age:", patient1["age"])
print("Patient 1 Symptoms:", patient1["symptoms"])

print("Patient 2 Name:", patient2["name"])
print("Patient 2 Age:", patient2["age"])
print("Patient 2 Symptoms:", patient2["symptoms"])


print("✅ Exercise Complete!")