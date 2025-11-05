#############################################
# EXERCISE SOLUTION: BUILD YOUR FIRST AI DATASET
#############################################

print("EXERCISE SOLUTION: BUILD YOUR FIRST AI DATASET")

# TODO 1: Create a list of dictionaries for 3 customers
customers = [
    {"name": "Alice Smith", "age": 25, "purchase_amount": 299.99, "product_category": "electronics"},
    {"name": "Bob Johnson", "age": 34, "purchase_amount": 89.50, "product_category": "clothing"},
    {"name": "Carol Davis", "age": 28, "purchase_amount": 45.00, "product_category": "books"}
]

print("✅ Created dataset with", len(customers), "customers")

# TODO 2: Access specific data from your dataset
print("ACCESSING SPECIFIC DATA:")

print("First customer name:", customers[0]["name"])
print("Third customer age:", customers[2]["age"])
print("Last customer purchase amount:", customers[-1]["purchase_amount"])
print("Total number of customers:", len(customers))

# TODO 3: Add a new customer to your dataset
new_customer = {"name": "Emma Brown", "age": 31, "purchase_amount": 125.75, "product_category": "clothing"}
customers.append(new_customer)

print("✅ Added new customer: {new_customer['name']}")
print("Dataset now has", len(customers), "customers")

# Display all customers to verify
print("\FINAL DATASET:")
for customer in customers:
    print("- {customer['name']}, Age: {customer['age']}, Spent: ${customer['purchase_amount']}, Category: {customer['product_category']}")

print("✅ Congratulations! You built your first AI dataset!")
print("This is exactly how real recommendation systems work!")