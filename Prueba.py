import sys # We call the sys module
# Global dictionary to store inventory.
# Key: product name (string), Value: dictionary with 'price' (float) and 'quantity' (int)
inventory = {}


def add_product(name: str, price: float, quantity: int) -> None:
    """
    Adds a new product to the inventory.
    If the product already exists, its quantity is updated.

    Args:
        name (str): The name of the product.
        price (float): The price of the product. Must be a positive number.
        quantity (int): The quantity of the product. Must be a positive integer.
    """
    if not isinstance(name, str) or not name.strip():
        print("Error: Product name cannot be empty.")
        return

    if not isinstance(price, (int, float)) or price <= 0:
        print("Error: Price must be a positive number.")
        return

    if not isinstance(quantity, int) or quantity <= 0:
        print("Error: Quantity must be a positive integer.")
        return
    # Normalize name to lowercase for case-insensitive storage and lookup
    normalized_name = name.lower()
    
    if normalized_name in inventory:
        print(f"Product '{name}' already exists. Updating quantity.")
        inventory[normalized_name]['quantity'] += quantity
    else:
        inventory[normalized_name] = {'price': price, 'quantity': quantity}
    print(f"Product '{name}' added/updated successfully.")


def consult_product(name: str) -> None:
    """
    Consults and displays the details of a product in the inventory.

    Args:
        name (str): The name of the product to consult.
    """
    if not isinstance(name, str) or not name.strip():
        print("Error: Product name cannot be empty for consultation.")
        return

    normalized_name = name.lower()

    if normalized_name in inventory:
        product_details = inventory[normalized_name]
        print(f"\n    Product Details for '{name}'   ")
        print(f"Name: {name}")
        print(f"Price: ${product_details['price']:.2f}")
        print(f"Quantity: {product_details['quantity']}")
        print(f"----------------------------------------\n")
    else:
        print(f"Product '{name}' not found in inventory.")

def update_product_price(name: str, new_price: float) -> None:
    """
    Updates the price of an existing product in the inventory.

    Args:
        name (str): The name of the product whose price is to be updated.
        new_price (float): The new price for the product. Must be a positive number.
    """
    if not isinstance(name, str) or not name.strip():
        print("Error: Product name cannot be empty for price update.")
        return

    if not isinstance(new_price, (int, float)) or new_price <= 0:
        print("Error: New price must be a positive number.")
        return

    normalized_name = name.lower()

    if normalized_name in inventory:
        old_price = inventory[normalized_name]['price']
        inventory[normalized_name]['price'] = new_price
        print(f"Price for '{name}' updated from ${old_price:.2f} to ${new_price:.2f}.")
    else:
        print(f"Product '{name}' not found in inventory. Cannot update price.")

def delete_product(name: str) -> None:
    """
    Deletes a product from the inventory after confirming its existence.

    Args:
        name (str): The name of the product to delete.
    """
    if not isinstance(name, str) or not name.strip():
        print("Error: Product name cannot be empty for deletion.")
        return

    normalized_name = name.lower()

    if normalized_name in inventory:
        print(f"The product '{name}' exists")
        confirm = input(f"Are you sure you want to delete '{name}' with a price of '{inventory[normalized_name]['price']}' and with '{str(inventory[normalized_name]['quantity'])}' quantities? (yes/no): ").lower()
        if confirm == 'yes':
            del inventory[normalized_name]
            print(f"Product '{name}' deleted successfully.")
        else:
            print(f"Deletion of '{name}' cancelled.")
    else:
        print(f"The product '{name}' does not exist")
        print(f"Product '{name}' not found in inventory. Cannot delete.")

def calculate_total_inventory_value() -> None:
    """
    Calculates and displays the total monetary value of all products in the inventory.
    """
    total_value = 0.0
    if not inventory:
        print("Inventory is empty. Total value: $0.00")
        return

    print("\n--- Inventory Value Breakdown ---")
    for name_key, details in inventory.items():
        product_name = name_key.capitalize() # Display with initial capital for readability
        item_value = details['price'] * details['quantity']
        total_value += item_value
        print(f"{product_name} (Price: ${details['price']:.2f}, Qty: {details['quantity']}) = ${item_value:.2f}")

    print("------------------------------------------")
    print(f"Total Inventory Value: ${total_value:.2f}")
    print("------------------------------------------")

def display_menu() -> None:
    """
    Displays the main menu of the inventory management system.
    """
    print("\n--- Inventory Management System ---")
    print("1. Add Product")
    print("2. Consult Product")
    print("3. Update Product Price")
    print("4. Delete Product")
    print("5. Calculate Total Inventory Value")
    print("6. Exit")
    print("-----------------------------------")

def main() -> None:
    """
    Main function to run the inventory management system.
    Initializes with at least 5 products and provides an interactive menu.
    """
    # Add at least 5 initial products as per acceptance criteria
    add_product("Computer monitor", 600000.85, 15)
    add_product("Computer case", 300000.26, 15)
    add_product("Motherboard", 3000000.322155, 15)
    add_product("RAM", 80000.45, 30)
    add_product("Graphics card", 4000000.12, 40)
    add_product("hard disk SSD", 100000.14451, 35) # Adding one more for good measure

    while True:
        display_menu()
        option = input("Enter your choice: ")

        if option == '1':
            name = input("Enter product name: ").strip()
            try:
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                add_product(name, price, quantity)
            except ValueError:
                print("Invalid input. Price must be a number and quantity an integer.")
        elif option == '2':
            name = input("Enter product name to consult: ").strip()
            consult_product(name)
        elif option == '3':
            name = input("Enter product name to update price: ").strip()
            try:
                new_price = float(input("Enter new price: "))
                update_product_price(name, new_price)
            except ValueError:
                print("Invalid input. Price must be a number.")
        elif option == '4':
            name = input("Enter product name to delete: ").strip()
            delete_product(name)
        elif option == '5':
            calculate_total_inventory_value()
        elif option == '6':
            print("Exiting Inventory Management System. Goodbye!")
            sys.exit()
        else:
            print("Invalid option. Please try again.")
main()