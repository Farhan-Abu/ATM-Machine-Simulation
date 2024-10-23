This code is a simple implementation of an ATM (Automated Teller Machine) program in Python. It allows users to perform basic banking operations through a console-based interface. Here’s a breakdown of its main components and functionalities:

Variables:

account_balance: Stores the user's current account balance, initialized to $10,000.00.
account_pin: Holds the user's PIN, initialized to "2003".
transaction_history: A list that records all transactions made by the user.
Functions:

display_menu(): Displays the main menu with options for the user to choose from.
check_balance(): Shows the user their current account balance.
cash_withdrawal(): Allows the user to withdraw a specified amount of money, checks for sufficient funds, and updates the transaction history.
cash_deposit(): Enables the user to deposit money into their account and updates the transaction history.
change_pin(): Provides functionality for the user to change their PIN after verifying the current one.
view_transaction_history(): Displays a history of all transactions made during the session.
validate_pin(): Prompts the user to enter their PIN, allowing up to three attempts before exiting if the PIN is incorrect.
Main Program:

The atm_program() function serves as the main driver of the ATM application. It welcomes the user, validates their PIN, and enters a loop that displays the menu and processes user choices until they choose to exit.
Execution:

The program starts execution in the if __name__ == "__main__": block, which calls the atm_program() function.
Overall, this ATM program provides a basic simulation of banking operations, allowing users to check their balance, withdraw and deposit money, change their PIN, and view their transaction history, all while ensuring security through PIN validation.
