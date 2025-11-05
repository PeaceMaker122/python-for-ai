#############################################
# EXERCISE: LOOP THROUGH YOUR OWN DATASET
#############################################

print("EXERCISE: LOOP THROUGH YOUR OWN DATASET")
print("=======================================")



# TODO 1: Create a list of dictionaries for 4 products

# Each product should have:
# - name (string)
# - price (float)
# - category (string): "electronics", "clothing", or "books"

# Product data to use:
# Product 1: "Laptop", 899.99, "electronics"
# Product 2: "T-Shirt", 19.99, "clothing"
# Product 3: "Python Book", 39.99, "books"
# Product 4: "Smartphone", 699.99, "electronics"

# Your code here:

products = [
    {"name": "Laptop", "price": 899.99, "category": "electronics"},
    {"name": "T-Shirt", "price": 19.99, "category": "clothing"},
    {"name": "Python Book", "price": 39.99, "category": "books"},
    {"name": "Smartphone", "price": 699.99, "category": "electronics"}
]

print("✅ Dataset with", len(products), "products created")

# TODO 2: Process all products

# Use a loop to print each product's information
# Format: "Product: [name] costs $[price]"

# Your code here:

print("✅ PROCESSING ALL PRODUCTS - PRICE INFO:")

for product in products:
    print(f"Product: {product['name']} costs ${product['price']}")



# TODO 3: Process all products in a different way

# Use a loop to print each product's name and category
# Format: "[name] is in the [category] category"

# Your code here:

print("✅ PROCESSING ALL PRODUCTS - CATEGORY INFO:")

for product in products:
    print(f"{product['name']} is in the {product['category']} category")



print("✅ Great job! You just processed your own dataset!")