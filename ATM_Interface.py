import time

class ATM:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +${amount}")
        print("Deposit successful!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            print("Withdrawal successful!")

    def transfer(self, recipient, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            recipient.balance += amount
            self.transactions.append(f"Transfer to {recipient.name}: -${amount}")
            recipient.transactions.append(f"Transfer from {self.name}: +${amount}")
            print("Transfer successful!")

    def transaction_history(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

def main():
    users = [
        ATM("Emma Jacob", "1234", 1000),
        ATM("Liam Noah", "2345", 2000),
        ATM("Benjamin Lucas","3456",3000),
        ATM("Evelyn Ethan","4567",4000),
        ATM("David Lucas","5678",5000),
        ATM("Sofia Martin","6789",6000),
        ATM("Logan James","7890",7000),
        ATM("Olivia Ryan","8901",8000),
        ATM("Mia Jones","9012",9000),
        ATM("Isabella Williams","0123",10000),
        ATM("Sophia Smith","1234",11000),
    ]

    while True:
        print("Welcome to the ATM!")
        user_id = input("Enter your account number: ")
        user = next((user for user in users if user.account_number == user_id), None)

        if user:
            pin = input("Enter your PIN: ")
            if pin == user.account_number:
                print(f"Welcome, {user.name}!")
                while True:
                    print("\nWhat would you like to do?")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Transfer")
                    print("5. Transaction History")
                    print("6. Quit")

                    choice = input("Enter your choice (1-6): ")

                    if choice == "1":
                        user.check_balance()
                    elif choice == "2":
                        amount = float(input("Enter the amount to deposit: "))
                        user.deposit(amount)
                    elif choice == "3":
                        amount = float(input("Enter the amount to withdraw: "))
                        user.withdraw(amount)
                    elif choice == "4":
                        recipient_id = input("Enter the recipient's account number: ")
                        recipient = next((u for u in users if u.account_number == recipient_id), None)
                        if recipient:
                            amount = float(input("Enter the amount to transfer: "))
                            user.transfer(recipient, amount)
                        else:
                            print("Invalid recipient account number!")
                    elif choice == "5":
                        user.transaction_history()
                    elif choice == "6":
                        print("Thank you for using the ATM. Goodbye!")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid PIN. Access denied.")
        else:
            print("Invalid account number. Access denied.")

        time.sleep(2)  # Pause for 2 seconds before restarting the loop

if __name__ == "__main__":
    main()