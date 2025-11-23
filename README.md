# Bakery Billing System 🍞

A simple, console-based application written in Python to automate the ordering and billing process for a bakery. This project demonstrates the use of Python dictionaries, loops, and conditional logic to create a functional Command Line Interface (CLI).

## 📋 Features
* **Menu Display:** Automatically fetches items and prices from a dictionary.
* **Order Management:** Allows users to select items by ID and specify quantities.
* **Real-time Validation:** Checks if the item ID exists in the menu.
* **Bill Generation:** Displays a detailed receipt with item names, quantities, individual costs, and the grand total.
* **Continuous Operation:** The program loops to handle multiple customers until the user decides to exit.

## 🛠️ Technologies Used
* **Language:** Python 3.x
* **Concepts:** Dictionaries, Lists, While Loops, For Loops, Input/Output handling.

## 🚀 How to Run

1.  **Prerequisites:** Ensure you have Python installed on your machine.
    ```bash
    python --version
    ```

2.  **Download:** Save the script as `bakery.py` (or clone this repository).

3.  **Execute:** Open your terminal or command prompt, navigate to the folder, and run:
    ```bash
    python bakery.py
    ```

## 💻 Usage Example

When you run the program, you will see the following interaction:

```text
===== BAKERY MENU =====
1 Cake - ₹ 120
2 Bread - ₹ 40
3 Donut - ₹ 30
4 Cookie - ₹ 20
0. Finish & Show Bill

Enter item number (0 to finish): 2
Enter quantity: 2
Added!

Enter item number (0 to finish): 0

----- BILL -----
Bread      x 2    = ₹ 80
TOTAL BILL = ₹ 80
