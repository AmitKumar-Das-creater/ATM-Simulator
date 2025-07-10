def show_menu():
    print("\n--- ATM Simulator ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def check_balance(balance):
    print(f"Your current balance is ₹{balance}")

def deposit(balance):
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Please enter a valid amount.")
    except ValueError:
        print("Invalid input! Please enter a number.")
    return balance

def withdraw(balance):
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Please enter a valid amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"₹{amount} withdrawn successfully.")
    except ValueError:
        print("Invalid input! Please enter a number.")
    return balance

# Initial balance (in-memory)
balance = 1000.0  # Starting balance

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        check_balance(balance)
    elif choice == "2":
        balance = deposit(balance)
    elif choice == "3":
        balance = withdraw(balance)
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
