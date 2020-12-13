# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# Import libraries
import csv
from pathlib import Path


# Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path("Resources/menu_data.csv")
sales_filepath = Path("Resources/sales_data.csv")
report_filepath = Path("Resources/sales_report.txt")

# @Initialize list objects to hold our menu and sales data
menu = []
sales = []

# Read in the menu data into the menu list
with open(menu_filepath, mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    for row in csv_reader:
        menu.append(row)

# Read in the sales data into the sales list
with open(sales_filepath, mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    for row in csv_reader:
        sales.append(row)

# Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Loop over every row in the sales list object
for sale in sales:

    # Initialize sales data variables
    quantity = float(sale[3])
    menu_item = sale[4]

    # If the item value not in the report, add it as a new entry with initialized metrics
    if menu_item not in report.keys():
        report[menu_item] = {
            "01-count": 0,
            "02-revenue": 0,
            "03-cogs": 0,
            "04-profit": 0
        }

    # For every row in our sales data, loop over the menu records to determine a match
    for record in menu:

        # Initialize menu data variables
        item = record[0]
        price = float(record[3])
        cost = float(record[4])

        if item == menu_item:
            # print(f"matched data: item = {item}, price = {price}, cost = {cost}")
            report[menu_item]["01-count"] += quantity
            report[menu_item]["02-revenue"] += price * quantity
            report[menu_item]["03-cogs"] += cost * quantity
            report[menu_item]["04-profit"] += (price - cost) * quantity
        # else:
            # print(f"{item} does not equal {menu_item} ! NO MATCH!")

# Write out report to a text file (won't appear on the command line output)
with open(report_filepath, mode="w") as file:
    for key, value in report.items():
        row = f"{key} : {{\"01-count\":{value['01-count']}, \"02-revenue\": {value['02-revenue']}, \"03-cogs\": {value['03-cogs']}, \"04-profit\": {value['04-profit']}}}\n"
        file.write(row)

    file.close()

# Print total number of records in sales data
print(f"total number of records in sales data = {len(sales)}")


