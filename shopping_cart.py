#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Shopping Cart Management System

This module allows users to create and manage a shopping cart system with a list
of available products and their details. Users can add records, calculate the total
cost of items, and display the purchase history. The system supports basic validation 
for product codes, quantity, and shipping methods.

Attributes:
    price_list (list): A list containing product details in the format 'code/name/price'.
    shopping_record_list (list): A list of records for items that have been added to the cart.
"""

# List of products and their prices
price_list = [
    "0/Salad Server Set/18.70", "1/Party Serviette Holder/11.95", "2/Tea Set/39.95", 
    "3/Mixing Bowl Set/49.95", "4/Knife Block Set/99.95", "5/Coffee Capsule Holder/29.95", 
    "6/Plastic Sensor Soap Pump/79.95", "7/Storage Bucket/24.95", "8/Oven Glove/9.95", 
    "9/Apron/29.95", "10/Biscuit Barrel/19.95", "11/Chopping Board/12.95", 
    "12/Carioca Cups/54.95", "13/Soup Bowls/43.00", "14/Elevate Wood Turner/19.95", 
    "15/Pasta Machine/114.95", "16/Teapot/29.95", "17/Cake Pop Scoop/9.95", 
    "18/Cookbook Stand/34.95", "19/Chocolate Station/34.95", "20/Coffee Maker/29.00", 
    "21/Pepper Mill/84.94", "22/Salt Mill/84.95", "23/Glass Storage Jar/4.95", 
    "24/Measuring Jug/19.95", "25/Kitchen Scale/39.95", "26/Tenderiser/34.95", 
    "27/Pizza Docker/19.95", "28/Knife Sharpener/79.95", "29/Steel Cork Opener/36.95", 
    "30/Steel Garlic Press/34.95", "31/Steel Can Opener/36.95", 
    "32/Stainless Steel Crank Flour Sifter/33.95", "33/Mineral Stone Mortar and Pestle/74.95", 
    "34/Citrus Catcher/19.95", "35/Cherry & Olive Pitter/27.95", 
    "36/Multi Grater-Detachable/26.95", "37/Stainless Steel Colander/44.95", 
    "38/Steel Pizza Pan/12.95", "39/Pop Container/22.95"
]

# List of shopping records for items added to the cart
shopping_record_list = []

def is_valid_code(code: int) -> bool:
    """
    Check if the product code is valid (0-39).
    
    Args:
        code (int): The product code to validate.

    Returns:
        bool: True if the code is valid, False otherwise.
    """
    if code in range(0, 40):
        return True

    print("Incorrect product code!")
    return False


def is_valid_quantity(quantity: int) -> bool:
    """
    Check if the quantity is valid (1-49).

    Args:
        quantity (int): The quantity to validate.

    Returns:
        bool: True if the quantity is valid, False otherwise.
    """
    if quantity in range(1, 50):
        return True

    print("Incorrect quantity!")
    return False


def split_product(product_str: str):
    """
    Split a product string into its component parts (code, name, price).

    Args:
        product_str (str): The product string to split, formatted as 'code/name/price'.

    Returns:
        tuple: (code, name, price) if successful, None otherwise.
    """
    try:
        parts = product_str.split("/")
        return int(parts[0]), parts[1], float(parts[2])
    except (ValueError, IndexError) as e:
        print(f"Error processing product: {e}")
        return None


def split_record(record: str):
    """
    Split a shopping record string into its component parts:
    code, name, value, price, quantity, and shipping method.

    Args:
        record (str): The shopping record string to split, formatted as 
                      'code/name/value/price/quantity/shipping_method'.

    Returns:
        tuple: (code, name, value, price, quantity, shipping method) if successful, None otherwise.
    """
    try:
        parts = record.split("/")
        return int(parts[0]), parts[1], parts[2], float(parts[3]), int(parts[4]), parts[5]
    except (ValueError, IndexError) as e:
        print(f"Error processing record: {e}")
        return None


def total_cost(record_list: list):
    """
    Calculate and print the total cost of the items in the shopping record list.
    Applies a delivery charge and high-value item surcharge if applicable.
    """
    total = 0.0
    for record in record_list:
        _, _, value, unit_price, quantity, shipping_method = split_record(record)
        product_cost = unit_price * quantity

        # Add 10% for delivery costs
        if shipping_method == "Delivery":
            product_cost *= 1.10

            # Additional $2 surcharge for each high-value item
            if value == "High":
                product_cost += 2 * quantity

        total += product_cost

    print(f"\nTotal cost is: ${total:.2f}")


def show_records(headers: list, record_list: list) -> None:
    """
    Display the shopping records in a formatted table along with the total cost.
    
    Args:
        headers (list): A list of lists containing tuples for column names and their widths.
        records (list): A list of strings representing the shopping records.
    """
    # Print the headers
    for header in headers:
        output_string = ""
        for column in header:
            output_string += f"{column[0]:<{column[1]}}  "
        print(output_string.rstrip())

    # Print each record
    for record_string in record_list:
        record_array = record_string.split('/')
        output_string = ""
        for (_, width), value in zip(headers[0], record_array):
            try:
                if "." in value:
                    value = f"{float(value):<.2f}  "
                else:
                    value = f"{int(value):<d}  "
            except ValueError:
                pass
            output_string += f"{value:<{width}}  "

        print(output_string.rstrip(),)


def create_record_string(record_list: list) -> str:
    """
    Create a formatted string from the given record list.

    Args:
        record_list (list): A list of product details to be joined into a string.

    Returns:
        str: A formatted string with all elements of the list joined by slashes.
    """
    return "/".join(str(item) for item in record_list)


def add_record():
    """
    Allow the user to add a new shopping record interactively.

    This method prompts the user to input a product code, quantity, and shipping method. 
    It validates these inputs, then creates a new record and appends it to the 
    `shopping_record_list`. If the user inputs 'END', the process stops and the shopping 
    records are displayed.
    """
    headers = [
        [
            ("Code", 4), ("Product", 35), ("Value", 5), ("Price $", 7),
            ("Quantity", 8), ("Shipping Method", 15)
        ],
        [
            ("-" * 4, 4), ("-" * 35, 35), ("-" * 5, 5), ("-" * 7, 7),
            ("-" * 8, 8), ("-" * 15, 15)
        ]
    ]

    while True:
        user_input = input("Please enter a valid product code (0-39): ")

        if user_input == "END":
            print()
            show_records(headers, shopping_record_list)
            total_cost(shopping_record_list)
            return

        product_code = int(user_input) if user_input.isdigit() else None
        if not (product_code and is_valid_code(product_code)):
            continue

        product_name, unit_price, value = "", 0.0, ""
        for product in price_list:
            product_data = split_product(product)
            if product_data and product_data[0] == product_code:
                product_name, unit_price = product_data[1], product_data[2]
                value = "High" if unit_price >= 30.00 else "Low"
                break

        while True:
            quantity = input("Please enter a valid quantity (1-49): ")
            if quantity.isdigit() and is_valid_quantity(int(quantity)):
                break

        while True:
            shipping_method = input("Please enter a valid shipping method: ('Pick-up', 'Delivery'): ")
            if shipping_method in ("Pick-up", "Delivery"):
                break

        shopping_record_list.append(create_record_string([product_code, product_name, value, unit_price, quantity, shipping_method]))


def search_record():
    """
    Allow the user to search for a product by name in the shopping records.
    """
    search_results = {}
    headers = [
        [
            ("Code", 4), ("Product", 35), ("Value", 5), ("Price $", 7),
            ("Quantity", 8), ("Cost $", 6)
        ],
        [
            ("-" * 4, 4), ("-" * 35, 35), ("-" * 5, 5), ("-" * 7, 7),
            ("-" * 8, 8), ("-" * 6, 6)
        ]
    ]

    while True:
        user_input = input("Please enter a search keyword (Case Insensitive): ").strip()
        if not user_input:
            print("Error: Please enter a keyword.")
            continue

        for record in shopping_record_list:
            product_code, product_name, value, unit_price, quantity, shipping_method = split_record(record)

            if user_input.lower() in product_name.lower():
                if product_code not in search_results:
                    search_results[product_code] = {
                        "name": product_name, "value": value, "unit_price": unit_price,
                        "quantity": 0, "total_cost": 0.0
                    }
                search_results[product_code]["quantity"] += quantity
                product_cost = unit_price * quantity

                if shipping_method == "Delivery":
                    product_cost *= 1.10
                    if value == "High":
                        product_cost += 2 * quantity

                search_results[product_code]["total_cost"] += product_cost

        if not search_results:
            print("No records found matching the keyword.")
            return

        formatted_results = [create_record_string([code] + list(details.values())) for code, details in search_results.items()]
        show_records(headers, formatted_results)
        print(f"\nTotal cost is: ${float(formatted_results[0].split('/')[-1]):.2f}")
        break


if __name__ == "__main__":
    while True:
        print("""
Welcome!
Please select an option from the menu.

1 - Add Record
2 - Search Record
3 - Exit
""")
        menu_selection = input("> ")

        if menu_selection == "1":
            add_record()
        elif menu_selection == "2":
            search_record()
        elif menu_selection == "3":
            break
        else:
            print("Incorrect selection!")
