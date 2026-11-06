print("=" * 40)
print("E-Commerce Product & Order Management System")
print("=" * 40)

users = {}


products = {
    "id": [101, 102, 103, 104],
    "name": ["Rice", "Butter", "Bread", "Sugar"],
    "category": ["Food", "Food", "Food", "Food"],
    "price": [96.0, 45.0, 30.0, 50.0],
    "stock": [100, 5, 0, 20],
    "status": ["Available", "Available", "Out of Stock", "Available"]
}


def register_user():
    print("\n--- New User Registration ---")

    name = input("Enter Your Name :- ").strip()
    if name == "":
        print("Name cannot be empty.")
        return

    if name in users:
        print("This name is already registered.")
        return

    password = input("Enter Your Password :- ").strip()
    if password == "":
        print("Password cannot be empty.")
        return

    users[name] = password
    print("Registration successful. Please login.")


def login_user():
    print("\n--- Existing User Login ---")

    name = input("Enter Your Name :- ").strip()
    password = input("Enter Your Password :- ").strip()

    if name in users and users[name] == password:
        print("Login successful. Welcome, " + name )
        return name

    print("Invalid name or password.")
    return None


def login_menu():
    while True:
        print("\n1. New User Registration")
        print("2. Existing User Login")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            user = login_user()
            if user is not None:
                return user
        elif choice == "0":
            print("Program closed.")
            return None
        else:
            print("Invalid choice.")


def add_product():
    print("\n--- Add Product ---")

   
    try:
        product_id = int(input("Enter Product ID: "))
    except ValueError:
        print("Product ID must be a number.")
        return

    if product_id in products["id"]:
        print("Product ID already exists. It must be unique.")
        return

    
    name = input("Enter Product Name: ").strip()
    if name == "":
        print("Product name cannot be empty.")
        return

    
    category = input("Enter Category: ").strip()
    if category == "":
        print("Category cannot be empty.")
        return

  
    try:
        price = float(input("Enter Price (Rs.): "))
    except ValueError:
        print("Price must be a number.")
        return

    if price <= 0:
        print("Price must be greater than Rs. 0.")
        return

    # Stock
    try:
        stock = int(input("Enter Stock: "))
    except ValueError:
        print("Stock must be a non-negative integer.")
        return

    if stock < 0:
        print("Stock must be a non-negative integer.")
        return

    
    if stock > 0:
        status = "Available"
    else:
        status = "Out of Stock"

    # Add the product to every list
    products["id"].append(product_id)
    products["name"].append(name)
    products["category"].append(category)
    products["price"].append(price)
    products["stock"].append(stock)
    products["status"].append(status)

    print("Product added successfully.")


def view_products():
    print("\n--- View Products ---")

    if len(products["id"]) == 0:
        print("No products available.")
        return

    print("ID\tName\tCategory\tPrice\tStock\tStatus")

    for i in range(len(products["id"])):
        print(
            products["id"][i],
            products["name"][i],
            products["category"][i],
            "Rs. " + str(products["price"][i]),
            products["stock"][i],
            products["status"][i],
            sep="\t"
        )


def product_menu():
    while True:
        print("\n1. Add Product")
        print("2. View Products")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "0":
            print("Program closed.")
            break
        else:
            print("Invalid choice.")


current_user = login_menu()

if current_user is not None:
    print("\nWelcome, " + current_user + "!")
    product_menu()
