#############################################
# EXERCISE: BUILD YOUR FIRST AI DATASET
#############################################

print("EXERCISE: BUILD YOUR FIRST AI DATASET")


# TODO 1: Create a list of dictionaries for 3 customers

# Each customer should have:
# - name (string)
# - age (integer) 
# - purchase_amount (float)
# - product_category (string): "electronics", "clothing", or "books"

# Customer data to use:

# Customer 1: "Alice Smith", 25, 299.99, "electronics"
# Customer 2: "Bob Johnson", 34, 89.50, "clothing" 
# Customer 3: "Carol Davis", 28, 45.00, "books"

# Your code here:

customers = [
    {"name": "Alice Smith", "age": 25, "purchase_amount": 299.99, "product_category": "electronics"},
    {"name": "Bob Johnson", "age": 34, "purchase_amount": 89.50, "product_category": "clothing"},
    {"name": "Carol Davis", "age": 28, "purchase_amount": 45.00, "product_category": "books"}

]



# TODO 2: Access specific data from your dataset

# Print the following:

# - The name of the first customer
# - The age of the third customer
# - The purchase amount of the last customer
# - The total number of customers in your dataset

# Your code here:

print("First customer name:", customers[0]["name"])
print("Third customer age:", customers[2]["age"])
print("Last customer purchase amount:", customers[-1]["purchase_amount"])
print("Total number of customers:", len(customers))



# TODO 3: Add a new customer to your dataset

# Add this customer to your list:

# "Emma Brown", 31, 125.75, "clothing"

# Your code here:

customers.append({"name": "Emma Brown", "age": 31, "purchase_amount": 125.75, "product_category": "clothing"})



print("✅ Congratulations! You built your first AI dataset!")
print("This is exactly how real recommendation systems work!")