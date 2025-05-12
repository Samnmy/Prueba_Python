import sys  # This line "imports" or "brings in" a special set of tools called the 'sys' module. These tools help the program interact with the computer's system, like exiting the program.

# Global dictionary to store inventory.
# Key: product name (string) - Think of this as the unique name for each product, which is text.
# Value: dictionary with 'price' (float) and 'quantity' (int) - For each product, we store its details:
#   'price' (float): The product's price, which can have decimal points (like $1.99).
#   'quantity' (int): How many of the product we have, which is a whole number.
inventory = {} # This creates an empty "container" or "storage box" named 'inventory'. It's a special type of container called a 'dictionary', perfect for storing items with unique names.

def add_product(name: str, price: float, quantity: int) -> None:
    # This line starts defining a "function" called 'add_product'.
    # A function is like a mini-program that performs a specific task.
    # It needs three pieces of information (called "arguments" or "parameters") to work:
    #   'name': The product's name (expected to be text, 'str').
    #   'price': The product's price (expected to be a number with decimals, 'float').
    #   'quantity': The product's quantity (expected to be a whole number, 'int').
    # '-> None' indicates that this function doesn't return any specific value; it just performs an action.
    """
    Adds a new product to the inventory.
    If the product already exists, its quantity is updated.

    Args:
        name (str): The name of the product.
        price (float): The price of the product. Must be a positive number.
        quantity (int): The quantity of the product. Must be a positive integer.
    """
    # This block of text enclosed in triple quotes is called a "docstring".
    # It's a detailed explanation of what the function does, what information it expects,
    # and any special conditions. It's for documentation, helping other people (and yourself later)
    # understand how to use this function.

    if not isinstance(name, str) or not name.strip():
        # This is a "check" or "validation". It makes sure the 'name' input is valid.
        # 'if': Means "if the following condition is true, then do what's indented below."
        # 'not isinstance(name, str)': Checks if 'name' is NOT text (a 'string').
        # 'or': Means "if the first condition is true, OR if the second condition is true."
        # 'not name.strip()': '.strip()' removes any extra spaces from the beginning/end of the name.
        #                    'not name.strip()' checks if the name is empty after removing spaces.
        # So, this line means: "If the name is not text, OR if the name is empty (after cleaning up spaces)..."
        print("Error: Product name cannot be empty.") # ...then, display this error message to the user.
        return # ...and stop this function right here, without doing anything else.

    if not isinstance(price, (int, float)) or price <= 0:
        # Another validation check for the 'price'.
        # 'not isinstance(price, (int, float))': Checks if 'price' is NOT a whole number ('int') AND NOT a decimal number ('float').
        # 'or price <= 0': Checks if the 'price' is zero or a negative number.
        # So, this means: "If the price is not a number, OR if the price is zero or negative..."
        print("Error: Price must be a positive number.") # ...display this error.
        return # ...and stop the function.

    if not isinstance(quantity, int) or quantity <= 0:
        # Another validation check for the 'quantity'.
        # 'not isinstance(quantity, int)': Checks if 'quantity' is NOT a whole number ('int').
        # 'or quantity <= 0': Checks if the 'quantity' is zero or a negative number.
        # So, this means: "If the quantity is not a whole number, OR if the quantity is zero or negative..."
        print("Error: Quantity must be a positive integer.") # ...display this error.
        return # ...and stop the function.

    # Normalize name to lowercase for case-insensitive storage and lookup
    # This is a comment explaining the next line's purpose.
    # "Normalize" means to make it consistent. "Case-insensitive" means it won't matter if you type "apple" or "Apple".
    normalized_name = name.lower() # Converts the 'name' (e.g., "Computer") to all lowercase (e.g., "computer").
                                   # This ensures that "Apple" and "apple" are treated as the same product in our inventory.

    if normalized_name in inventory:
        # 'if normalized_name in inventory:': This checks if the 'normalized_name' (e.g., "computer")
        # is already a "key" (a product name) in our 'inventory' dictionary (our address book).
        print(f"Product '{name}' already exists. Updating quantity.") # If it exists, tell the user we're updating its quantity.
        inventory[normalized_name]['quantity'] += quantity
        # 'inventory[normalized_name]': Goes to the entry for this product in our 'inventory'.
        # "['quantity']": Specifically looks at the 'quantity' value for that product.
        # '+= quantity': This is a shorthand. It means: "Take the current quantity, add the new 'quantity'
        #                from the function's input to it, and then save that new total back as the quantity."
    else:
        # 'else:': If the product was NOT found in the 'inventory' (meaning it's a new product)...
        inventory[normalized_name] = {'price': price, 'quantity': quantity}
        # ...then, create a brand new entry in the 'inventory'.
        # 'inventory[normalized_name] = ...': Use the 'normalized_name' as the unique name for this new product.
        # '{'price': price, 'quantity': quantity}': The value stored for this new product is a small dictionary
        #                                          containing its 'price' and 'quantity'.
    print(f"Product '{name}' added/updated successfully.") # After adding or updating, display a success message.
                                                        # 'f"..."' is an "f-string", a way to easily put variable values into text.

def consult_product(name: str) -> None:
    # Defines another function called 'consult_product'.
    # It takes one piece of information: the 'name' of the product to look up.
    # It doesn't return any specific value.
    """
    Consults and displays the details of a product in the inventory.

    Args:
        name (str): The name of the product to consult.
    """
    # Docstring explaining the 'consult_product' function.

    if not isinstance(name, str) or not name.strip():
        # Validation check for the 'name' input, ensuring it's valid text and not empty.
        print("Error: Product name cannot be empty for consultation.") # Error message if name is invalid.
        return # Stop the function.

    normalized_name = name.lower() # Converts the input 'name' to lowercase for consistent searching.

    if normalized_name in inventory:
        # Checks if the 'normalized_name' (e.g., "computer monitor") exists in our 'inventory'.
        product_details = inventory[normalized_name] # If found, get all the details (price, quantity) for that product.
        print(f"\n Product Details for '{name}' ") # Print a nice header. '\n' creates a new line.
        print(f"Name: {name}") # Print the product's name.
        print(f"Price: ${product_details['price']:.2f}")
        # Print the product's price. '${product_details['price']:.2f}' formats the number to always show two decimal places (like $12.50).
        print(f"Quantity: {product_details['quantity']}") # Print the product's quantity.
        print(f"----------------------------------------\n") # Print a separator line.
    else:
        # 'else:': If the product was NOT found in the 'inventory'...
        print(f"Product '{name}' not found in inventory.") # ...display a message saying it wasn't found.

def update_product_price(name: str, new_price: float) -> None:
    # Defines a function called 'update_product_price'.
    # It takes the 'name' of the product and the 'new_price' (a decimal number) as input.
    # It doesn't return any specific value.
    """
    Updates the price of an existing product in the inventory.

    Args:
        name (str): The name of the product whose price is to be updated.
        new_price (float): The new price for the product. Must be a positive number.
    """
    # Docstring explaining the 'update_product_price' function.

    if not isinstance(name, str) or not name.strip():
        # Validation check for the 'name' input.
        print("Error: Product name cannot be empty for price update.") # Error message if name is invalid.
        return # Stop the function.

    if not isinstance(new_price, (int, float)) or new_price <= 0:
        # Validation check for the 'new_price' input, ensuring it's a positive number.
        print("Error: New price must be a positive number.") # Error message if new price is invalid.
        return # Stop the function.

    normalized_name = name.lower() # Converts the input 'name' to lowercase for consistent searching.

    if normalized_name in inventory:
        # Checks if the product exists in the 'inventory'.
        old_price = inventory[normalized_name]['price'] # If found, save the current price in 'old_price' before changing it.
        inventory[normalized_name]['price'] = new_price # Update the product's price in the 'inventory' to the 'new_price'.
        print(f"Price for '{name}' updated from ${old_price:.2f} to ${new_price:.2f}.")
        # Display a success message, showing both the old and new prices, formatted to two decimal places.
    else:
        # 'else:': If the product was NOT found in the 'inventory'...
        print(f"Product '{name}' not found in inventory. Cannot update price.") # ...display an error message.

def delete_product(name: str) -> None:
    # Defines a function called 'delete_product'.
    # It takes the 'name' of the product to be deleted as input.
    # It doesn't return any specific value.
    """
    Deletes a product from the inventory after confirming its existence.

    Args:
        name (str): The name of the product to delete.
    """
    # Docstring explaining the 'delete_product' function.

    if not isinstance(name, str) or not name.strip():
        # Validation check for the 'name' input.
        print("Error: Product name cannot be empty for deletion.") # Error message if name is invalid.
        return # Stop the function.

    normalized_name = name.lower() # Converts the input 'name' to lowercase for consistent searching.

    if normalized_name in inventory:
        # Checks if the product exists in the 'inventory'.
        print(f"The product '{name}' exists") # If found, tell the user the product exists.
        confirm = input(f"Are you sure you want to delete '{name}' with a price of '{inventory[normalized_name]['price']}' and with '{str(inventory[normalized_name]['quantity'])}' quantities? (yes/no): ").lower()
        # 'input(...)': This asks the user for confirmation. It displays a message and waits for the user to type and press Enter.
        #               It includes details about the product to be deleted.
        #               '.lower()' converts the user's typed response ("Yes", "No") to lowercase for easy comparison.
        if confirm == 'yes':
            # If the user types "yes" (in lowercase, due to '.lower()' above)...
            del inventory[normalized_name] # 'del': This keyword means "delete this item". It removes the entire product entry
                                          #        (name, price, and quantity) from our 'inventory' dictionary.
            print(f"Product '{name}' deleted successfully.") # Confirm the deletion to the user.
        else:
            # 'else:': If the user typed anything other than "yes"...
            print(f"Deletion of '{name}' cancelled.") # ...inform them that the deletion was cancelled.
    else:
        # 'else:': If the product was NOT found in the 'inventory' (from the initial 'if')...
        print(f"The product '{name}' does not exist") # ...tell the user it doesn't exist.
        print(f"Product '{name}' not found in inventory. Cannot delete.") # Reiterate that it couldn't be deleted because it's not there.

def calculate_total_inventory_value() -> None:
    # Defines a function called 'calculate_total_inventory_value'.
    # It calculates and displays the total monetary value of all products.
    # It takes no input and returns nothing.
    """
    Calculates and displays the total monetary value of all products in the inventory.
    """
    # Docstring explaining the 'calculate_total_inventory_value' function.

    total_value = 0.0 # Creates a variable named 'total_value' and sets its initial value to zero (as a decimal number).

    if not inventory:
        # 'if not inventory:': Checks if the 'inventory' dictionary is empty.
        # (An empty dictionary is considered "false" in a logical check, so 'not' makes it "true" if it's empty).
        print("Inventory is empty. Total value: $0.00") # If empty, print a message saying so.
        return # Stop the function here.

    print("\n--- Inventory Value Breakdown ---") # Print a heading for the breakdown.
    for name_key, details in inventory.items():
        # 'for name_key, details in inventory.items():': This is a "for loop".
        # It means: "For each product in our 'inventory' dictionary, do the following indented steps."
        # 'inventory.items()': Gives us both the product's unique name (stored in 'name_key')
        #                      and its full details (price and quantity, stored in 'details') for each item.
        product_name = name_key.capitalize() # Display with initial capital for readability.
                                              # '.capitalize()' makes the first letter of the product name uppercase.
        item_value = details['price'] * details['quantity'] # Calculates the value of the current single product (price multiplied by quantity).
        total_value += item_value # Adds the 'item_value' of the current product to our running 'total_value'.
                                  # 'total_value = total_value + item_value'
        print(f"{product_name} (Price: ${details['price']:.2f}, Qty: {details['quantity']}) = ${item_value:.2f}")
        # Prints a detailed line for each product, showing its name, price, quantity, and individual total value.

    print("------------------------------------------") # Print a separator line.
    print(f"Total Inventory Value: ${total_value:.2f}") # Print the grand total value of all products, formatted to two decimal places.
    print("------------------------------------------") # Print another separator line.

def display_menu() -> None:
    # Defines a function called 'display_menu'.
    # Its job is to show the user the list of available options.
    # It takes no input and returns nothing.
    """
    Displays the main menu of the inventory management system.
    """
    # Docstring explaining the 'display_menu' function.

    print("\n--- Inventory Management System ---") # Prints a heading for the menu.
    print("1. Add Product")     # Prints menu option 1.
    print("2. Consult Product") # Prints menu option 2.
    print("3. Update Product Price") # Prints menu option 3.
    print("4. Delete Product")  # Prints menu option 4.
    print("5. Calculate Total Inventory Value") # Prints menu option 5.
    print("6. Exit")            # Prints menu option 6 (to quit).
    print("-----------------------------------") # Prints a separator line.

def main() -> None:
    # This is the 'main' function. In many programs, this is the "control center"
    # that gets everything started and manages the flow of the program.
    # It takes no input and returns nothing.
    """
    Main function to run the inventory management system.
    Initializes with at least 5 products and provides an interactive menu.
    """
    # Docstring explaining the 'main' function.

    # Add at least 5 initial products as per acceptance criteria
    # These lines "call" (or run) the 'add_product' function multiple times.
    # This pre-fills our 'inventory' with some example products when the program starts.
    add_product("Computer monitor", 600000.85, 15)
    add_product("Computer case", 300000.26, 15)
    add_product("Motherboard", 3000000.322155, 15)
    add_product("RAM", 80000.45, 30)
    add_product("Graphics card", 4000000.12, 40)
    add_product("hard disk SSD", 100000.14451, 35) # Adding one more for good measure

    while True:
        # 'while True:': This is a "while loop" that will run forever.
        # It means: "Keep doing all the indented steps below, repeatedly, until I specifically tell you to stop."
        display_menu() # Calls the 'display_menu' function to show the user the options.
        option = input("Enter your choice: ") # 'input(...)': Displays the message "Enter your choice: "
                                            # and waits for the user to type something and press Enter.
                                            # Whatever the user types is stored in the 'option' variable.

        if option == '1':
            # 'if option == '1'': Checks if the user typed '1' (meaning they want to Add Product).
            name = input("Enter product name: ").strip() # Ask for the product name and clean up spaces.
            try:
                # 'try:': This starts a "try block". The code inside this block will be attempted.
                # If a specific kind of error occurs, instead of crashing, the program will jump to the 'except' block.
                price = float(input("Enter product price: ")) # Ask for price, try to convert it to a decimal number.
                quantity = int(input("Enter product quantity: ")) # Ask for quantity, try to convert it to a whole number.
                add_product(name, price, quantity) # If both conversions are successful, call the 'add_product' function.
            except ValueError:
                # 'except ValueError:': This "catches" a 'ValueError' error.
                # A 'ValueError' happens if 'float()' or 'int()' can't convert the input (e.g., if the user types "abc" for price).
                print("Invalid input. Price must be a number and quantity an integer.") # If a ValueError occurs, print this error message.
        elif option == '2':
            # 'elif option == '2'': Else if the user typed '2' (Consult Product).
            name = input("Enter product name to consult: ").strip() # Ask for the name to consult.
            consult_product(name) # Call the 'consult_product' function.
        elif option == '3':
            # 'elif option == '3'': Else if the user typed '3' (Update Product Price).
            name = input("Enter product name to update price: ").strip() # Ask for the name to update.
            try:
                new_price = float(input("Enter new price: ")) # Ask for the new price and try to convert it to a decimal.
                update_product_price(name, new_price) # If conversion is successful, call the 'update_product_price' function.
            except ValueError:
                print("Invalid input. Price must be a number.") # Error message if the new price is not a number.
        elif option == '4':
            # 'elif option == '4'': Else if the user typed '4' (Delete Product).
            name = input("Enter product name to delete: ").strip() # Ask for the name to delete.
            delete_product(name) # Call the 'delete_product' function.
        elif option == '5':
            # 'elif option == '5'': Else if the user typed '5' (Calculate Total Inventory Value).
            calculate_total_inventory_value() # Call the 'calculate_total_inventory_value' function.
        elif option == '6':
            # 'elif option == '6'': Else if the user typed '6' (Exit).
            print("Exiting Inventory Management System. Goodbye!") # Print a goodbye message.
            sys.exit() # 'sys.exit()': This command, from the 'sys' module, tells the program to stop running immediately.
                       # This is how we exit the 'while True' loop.
        else:
            # 'else:': If the user typed anything other than '1', '2', '3', '4', '5', or '6'.
            print("Invalid option. Please try again.") # Display an error message, and the loop will repeat, showing the menu again.

main() # This line is outside of any function definition. It's the very first line of code that runs when you start the script.
       # It "calls" (or runs) our 'main' function, which then initializes the program and starts the interactive menu loop.