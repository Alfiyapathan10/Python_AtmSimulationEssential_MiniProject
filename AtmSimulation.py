# ------------------ ATM Simulation Project ------------------

class ATM:
    def __init__(self, balance=0.0, pin="1234"):
        self.balance = float(balance)
        self.pin = pin

    # PIN Verification
    def verify_pin(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your 4-digit PIN: ")
            if entered_pin == self.pin:
                print("Login successful!\n")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. {attempts} attempt(s) remaining.\n")

        print("Too many incorrect attempts. Account locked.")
        return False

    # Check Balance
    def check_balance(self):
        print(f"Current Balance: ₹{self.balance:.2f}")

    # Deposit Money
    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                self.balance += amount
                print(f"₹{amount:.2f} deposited successfully.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Withdraw Money
    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                print("Amount must be greater than zero.")
            elif amount > self.balance:
                print("Insufficient balance!")
            else:
                self.balance -= amount
                print(f"₹{amount:.2f} withdrawn successfully.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Main Menu
    def menu(self):
        while True:
            print("\n------ ATM MENU ------")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Select an option (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice! Please select between 1 and 4.")


# ----------- Run Program -----------
atm = ATM(balance=5000, pin="1234")

print("Welcome to Python ATM Simulation")

if atm.verify_pin():
    atm.menu()