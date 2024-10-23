account_balance = 10000.0  
account_pin = "2003"  
transaction_history = []  


def display_menu():
    print("\n***** ATM Menu *****")
    print("1. Account Balance Inquiry")
    print("2. Cash Withdrawal")
    print("3. Cash Deposit")
    print("4. Change PIN")
    print("5. Transaction History")
    print("6. Exit")


def check_balance():
    print(f"\nYour current balance is: ${account_balance:.2f}")

def cash_withdrawal():
    global account_balance
    amount = float(input("Enter the amount to withdraw: $"))
    
    if amount > account_balance:
        print("\nInsufficient balance!")
    else:
        account_balance -= amount
        transaction_history.append(f"Withdrew ${amount:.2f}")
        print(f"\nYou have withdrawn ${amount:.2f}. Your new balance is: ${account_balance:.2f}")


def cash_deposit():
    global account_balance
    amount = float(input("Enter the amount to deposit: $"))
    account_balance += amount
    transaction_history.append(f"Deposited ${amount:.2f}")
    print(f"\nYou have deposited ${amount:.2f}. Your new balance is: ${account_balance:.2f}")


def change_pin():
    global account_pin
    old_pin = input("Enter your current PIN: ")
    
    if old_pin != account_pin:
        print("\nIncorrect PIN!")
    else:
        new_pin = input("Enter your new PIN: ")
        confirm_pin = input("Confirm your new PIN: ")
        
        if new_pin == confirm_pin:
            account_pin = new_pin
            print("\nPIN changed successfully!")
        else:
            print("\nPINs do not match!")

def view_transaction_history():
    if transaction_history:
        print("\n***** Transaction History *****")
        for transaction in transaction_history:
            print(transaction)
    else:
        print("\nNo transactions found.")

def validate_pin():
    for _ in range(3): 
        entered_pin = input("Enter your PIN: ")
        if entered_pin == account_pin:
            return True
        else:
            print("Incorrect PIN. Try again.")
    
    print("Too many incorrect attempts. Exiting...")
    return False


def atm_program():
    print("Welcome to the ATM!")

    if not validate_pin():
        return

    while True:
        display_menu()
        choice = input("\nChoose an option (1-6): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            cash_withdrawal()
        elif choice == "3":
            cash_deposit()
        elif choice == "4":
            change_pin()
        elif choice == "5":
            view_transaction_history()
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    atm_program()
