# Cafe Order App Code Style Guide

The Cafe Order App adheres to the PEP 8 Style Guide for Python Code. For a complete list of PEP 8 conventions, please refer to the official [PEP 8 Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).

## Feature: Welcome Message and Menu Display

**Description:** Display a visually appealing welcome message and a well-organized menu table, making it easy for users to browse through the available items and their prices.

## Feature: User-friendly Order Input and Validation

**Description:** Allow users to input their order by selecting items from the menu and specifying the desired quantity, with built-in input validation to ensure only valid items and quantities are added to the order.

## Feature: Order Modification and Removal

**Description:** Enable users to remove items from their order as needed, providing flexibility in making changes before proceeding to checkout.

## Feature: Order Summary and Total Calculation

**Description:** Calculate the total cost of the user's order and display an order summary in a formatted table, providing a clear overview of the items and their corresponding costs.

## Feature: Payment Processing and Receipt Generation

**Description:** Prompt users to enter their payment amount, validate that the payment is sufficient, and generate a receipt as a CSV file containing order details, total cost, and timestamp.

# Cafe Order App Development

## Display Welcome Message and Menu

**Deadline: End of Day 1**

1. Create a function to display a welcome message
2. Create a dictionary for the menu items and their prices
3. Create a function to display the menu using a formatted table
4. Integrate the display menu function with the welcome message
5. Test the display of the welcome message and menu

## Get Customer Order

**Deadline: End of Day 3**

1. Create a function to get the customer's order
2. Implement user input validation for menu items and quantity
3. Add items and their quantity to the order dictionary
4. Allow the user to enter 'done' to finish the order
5. Test the order input functionality
6. Modify the function so the user is able to remove items

## Calculate and Display Order Summary

**Deadline: End of Day 5**

1. Create a function to calculate the total order cost
2. Create a function to display the order summary using a formatted table
3. Integrate the order summary function with the order input
4. Display the total cost of the order
5. Test the order summary functionality

## Process Payment and Generate Receipt

**Deadline: End of Day 7**

1. Create a function to get the payment amount from the user
2. Validate the payment amount and handle insufficient payments
3. Calculate change and display the change amount
4. Create a function to generate a receipt as a CSV file
5. Test the payment processing and receipt generation functionality

## Main Program Execution

**Deadline: End of Day 9**

1. Organize the functions in the main program function
2. Add a conditional check for the main program execution
3. Test the complete application functionality
4. Fix any issues or bugs found during testing
5. Prepare the application for deployment

![project management plan](docs/Screenshot%202023-05-05%20202728.png)
[Link to Trello board](https://trello.com/b/W7HPhdrs)

# Cafe Order App Help Documentation

This documentation provides a detailed set of instructions on how to install and use the Cafe Order App.

## Installation

Follow these steps to install the application:

1. Ensure you have Python 3.6 or later installed on your system. If not, download and install it from the official [Python website](https://www.python.org/).

2. Download the application source code from the provided [repository](https://github.com/BuzSaliji/BurimSaliji_T1A3) or as a [ZIP file](https://github.com/BuzSaliji/BurimSaliji_T1A3/archive/refs/heads/main.zip).

3. Extract the source code to a folder of your choice.

4. Open a terminal and navigate to the folder containing the source code.

5. Run the following command to set up a virtual environment and install the required dependencies:

   ```
   ./run.sh
   ```

### Dependencies

The Cafe Order Application requires the following dependencies:

- Python 3.6 or later
- tabulate
- termcolor

These dependencies are listed in the `requirements.txt` file and will be installed automatically when running the `run.sh` script.

### System/Hardware Requirements

- A PC/Laptop with a modern CPU (Python is not very CPU intensive) and at least 8GB of RAM is recommended.
- Python 3.6 or later interpreter installed
- An active internet connection (optional, for downloading dependencies if not already installed)

## Usage

1. Ensure the virtual environment is activated by running:

   ```
   source myenv/bin/activate
   ```

2. Start the application by running:

   ```
   python3 main.py
   ```

3. Follow the on-screen prompts to interact with the application:

   - To select an item, type the name of the item from the menu (e.g., "espresso").
   - To add an item to the order, type the desired quantity (e.g., "2").
   - To remove an item from the order, type "remove" and enter the name of the item to be removed.

4. Provide the payment amount when prompted.
5. Review the order summary and change provided.
6. A receipt will be generated as a CSV file in the same folder as the application.
7. To exit the application, close the terminal or command prompt window.

### Links:

[Source code repository](https://github.com/BuzSaliji/BurimSaliji_T1A3)
[Link to Trello board](https://trello.com/b/W7HPhdrs)
[Link to slide deck presentation](https://vimeo.com/824431347)
