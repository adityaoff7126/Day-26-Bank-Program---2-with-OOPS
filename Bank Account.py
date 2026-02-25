import random


class BankAccount:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.__pin = pin
        self.account_number = random.randint(10000, 99999)
        self.balance = balance
        self.history = []

    def __check_pin(self, pin):
        return self.__pin == pin

    def deposit(self, amount, pin):
        if not self.__check_pin(pin):
            print("Wrong PIN")
            return
        self.balance += amount
        self.history.append(f"Deposited {amount}")
        print("Deposit successful")

    def withdraw(self, amount, pin):
        if not self.__check_pin(pin):
            print("Wrong PIN")
            return
        if amount > self.balance:
            print("Insufficient balance")
            return
        self.balance -= amount
        self.history.append(f"Withdrawn {amount}")
        print("Withdraw successful")

    def transfer(self, other, amount, pin):
        if not self.__check_pin(pin):
            print("Wrong PIN")
            return
        if amount > self.balance:
            print("Insufficient balance")
            return
        self.balance -= amount
        other.balance += amount
        self.history.append(f"Transferred {amount} to {other.name}")
        other.history.append(f"Received {amount} from {self.name}")
        print("Transfer successful")

    def show_history(self, pin):
        if not self.__check_pin(pin):
            print("Wrong PIN")
            return
        print("\nTransaction History:")
        for h in self.history:
            print("-", h)


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, pin, balance):
        acc = BankAccount(name, pin, balance)
        self.accounts[acc.account_number] = acc
        print(f"Account created. Account No: {acc.account_number}")

    def get_account(self, acc_no):
        return self.accounts.get(acc_no)

bank = Bank()

while True:
    print("\n====== BANK MENU ======")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        pin = int(input("Set 4-digit PIN: "))
        balance = int(input("Initial deposit: "))
        bank.create_account(name, pin, balance)

    elif choice == "2":
        acc_no = int(input("Enter Account Number: "))
        acc = bank.get_account(acc_no)

        if not acc:
            print("Account not found")
            continue

        pin = int(input("Enter PIN: "))

        while True:
            print(f"\nWelcome {acc.name}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Balance")
            print("5. History")
            print("6. Logout")

            opt = input("Choose: ")

            if opt == "1":
                amt = int(input("Amount: "))
                acc.deposit(amt, pin)

            elif opt == "2":
                amt = int(input("Amount: "))
                acc.withdraw(amt, pin)

            elif opt == "3":
                to_acc = int(input("Transfer to Account No: "))
                target = bank.get_account(to_acc)
                if target:
                    amt = int(input("Amount: "))
                    acc.transfer(target, amt, pin)
                else:
                    print("Target account not found")

            elif opt == "4":
                print("Balance:", acc.balance)

            elif opt == "5":
                acc.show_history(pin)

            elif opt == "6":
                break

            else:
                print("Invalid option")

    elif choice == "3":
        print("Exiting program")
        break

    else:
        print("Invalid choice")