# Inventory Management System

This is a Python-based console application designed to manage product inventory. It allows users to add, consult, update prices, delete products, and calculate the total value of the inventory.

## Functionalities

1.  *Add Products:* Add new products to the inventory with their name, price, and quantity. If a product with the same name already exists, its quantity will be updated.
2.  *Consult Products:* Search for a product by its name and display its current details (price and quantity).
3.  *Update Product Prices:* Modify the price of an existing product.
4.  *Delete Products:* Remove a product from the inventory after a confirmation prompt.
5.  *Calculate Total Inventory Value:* Compute and display the sum of (price * quantity) for all products in the inventory, showing the total and a breakdown for each item.

## Acceptance Criteria Met

* *Initial Products:* The program initializes with at least 5 pre-added products when it starts.
* *Product Consultation:* If a product is not found during consultation, a clear "not found" message is displayed.
* *Price Update Validation:* New prices must be positive numbers. The system validates this input.
* *Product Deletion Confirmation:* Before deleting a product, the system asks for confirmation.
* *Total Inventory Value Precision:* The total inventory value is calculated precisely and displayed with two decimal places.
* *Code Structure and Comments:* The code is well-structured into functions for each operation and includes explanatory comments.
* *Language:* All code and comments are 100% in English.

## How to Run the Program

1.  *Save the code:* Save the provided Python code into a file named inventory_manager.py.
2.  *Open a terminal or command prompt:* Navigate to the directory where you saved the inventory_manager.py file.
3.  *Execute the script:* Run the program using the Python interpreter:

    bash
    python inventory_manager.py
    

4.  *Interact with the menu:* Follow the on-screen instructions to choose from the available options (add, consult, update price, delete, calculate total value, or exit).

## Example of Input and Output

Upon running the program, you will see an initial set of products added and the main menu:
