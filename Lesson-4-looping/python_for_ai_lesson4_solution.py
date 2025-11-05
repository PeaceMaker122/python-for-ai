#############################################
# EXERCISE SOLUTION: LOOP THROUGH YOUR OWN DATASET
#############################################

print("EXERCISE SOLUTION: LOOP THROUGH YOUR OWN DATASET")
print("================================================")

# TODO 1: Create a list of dictionaries for 4 products
products = [
    {"name": "Laptop", "price": 899.99, "category": "electronics"},
    {"name": "T-Shirt", "price": 19.99, "category": "clothing"},
    {"name": "Python Book", "price": 39.99, "category": "books"},
    {"name": "Smartphone", "price": 699.99, "category": "electronics"}
]

print("✅ Created dataset with", len(products), "products")

# TODO 2: Process all products
print("PROCESSING ALL PRODUCTS - PRICE INFO:")
for product in products:
    print("Product:", product["name"], "costs $" + str(product["price"]))

# TODO 3: Process all products in a different way
print("PROCESSING ALL PRODUCTS - CATEGORY INFO:")
for product in products:
    print(product["name"], "is in the", product["category"], "category")

print("✅ Great job! You just processed your own dataset!")