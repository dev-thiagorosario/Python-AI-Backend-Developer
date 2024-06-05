# Import necessary modules
import textwrap
from abc import ABC, abstractmethod
from datetime import datetime

# Define a class for clients
class Client:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.accounts = []
    
    def perform_transactions(self, account, transaction):
        transaction.register(account)

    def add_account(self, account):
        self.accounts.append(account)

# Define a class for individuals (inheriting from Client)
class Individual(Client):
    def __init__(self, name, birth_date, cpf, address):
        super().__init__(name, address)
        self.birth_date = birth_date
        self.cpf = cpf

# Define a class for accounts
class Account:
    def __init__(self, number, client):
        self._balance = 0
        self._number = number
        self._agency = "0001"
        self._client = client
        self._history = History()

    @classmethod
    def new_account(cls, client, number):
        return cls(number, client)
        
    @property
    def balance(self):
        return self._balance
        
    @property
    def number(self):
        return self._number
        
    @property
    def agency(self):
        return self._agency

    @property
    def client(self):
        return self._client 

    @property
    def history(self):
        return self._history

    def withdraw(self, value):
        if value <= self._balance:
            self._balance -= value
            self._history.add_transaction("Withdrawal", value)
            return True
        else:
            print("Insufficient balance")
            return False

    def deposit(self, value):
        if value > 0:
            self._balance += value
            self._history.add_transaction("Deposit", value)
            return True
        else:
            print("Invalid deposit value")
            return False

# Define a class for transaction history
class History:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, type, value):
        transaction = {"type": type, "value": value, "date": datetime.now()}
        self.transactions.append(transaction)

# Define an abstract class for transactions
class Transaction(ABC):
    @abstractmethod
    def register(self, account):
        pass

# Define a class for withdrawals (inheriting from Transaction)
class Withdrawal(Transaction):
    def __init__(self, value):
        self.value = value

    def register(self, account):
        account.withdraw(self.value)

# Define a class for deposits (inheriting from Transaction)
class Deposit(Transaction):
    def __init__(self, value):
        self.value = value

    def register(self, account):
        account.deposit(self.value)

# Define a function to display the menu
def menu():
    menu_text = """
    ====== MENU ======
    [d] Deposit
    [s] Withdraw
    [c] Check Balance
    [e] Statement
    [m] Change Password
    [nc] New Account
    [dc] Account Details
    [l] List Accounts
    [n] New User
    [x] Exit System
    """
    print(textwrap.dedent(menu_text))
    return input("Choose an option: ").strip().lower()

# Define a function to deposit funds
def deposit(account, value):
    if account.deposit(value):
        print("\nDeposit successful!")
        print("Current Balance: R$ {:.2f}".format(account.balance))
    else:
        print("\nOperation failed! Invalid deposit value.")

# Define a function to withdraw funds
def withdraw(account, value):
    if account.withdraw(value):
        print("\nWithdrawal successful!")
    else:
        print("\nOperation failed! Insufficient balance or invalid value.")

# Define a function to check balance
def check_balance(account):
    print("\nYour current balance is R$ {:.2f}".format(account.balance))

# Define a function to display account statement
def display_statement(account):
    if not account.history.transactions:
        print("\nStatement is empty.")
        return
    print("\nStatement:\n-----------------------------")
    for movement in account.history.transactions:
        type = movement["type"]
        value = movement["value"]
        date = movement["date"].strftime('%Y-%m-%d %H:%M:%S')
        print(f"Type: {type} | Value: R$ {value:.2f} | Date: {date}")
    print('-----------------------------')

# Define a function to create a new user
def create_user(users):
    cpf = input('\nEnter your CPF (only numbers): ')
    user = filter_user(cpf, users)

    if user:
        print("\nUser with this CPF already exists!")
        return

    name = input("Enter your full name: ")
    birth_date = input("Enter your birth date in the format DD/MM/YYYY: ")
    address = input("Enter the complete address (Street, Number, Neighborhood, City/State): ")

    # Create a new user and add it to the list of users
    users.append(Individual(name, birth_date, cpf, address))
    print("User created successfully!\n")

# Function to filter users by CPF
def filter_user(cpf, users):
    for user in users:
        if isinstance(user, Individual) and user.cpf == cpf:
            return user
    return None

# Function to create a new account
def create_account(users, accounts):
    cpf = input("Enter the CPF of the account holder: ")
    user = filter_user(cpf, users)

    if not user:
        print("User not found. Create a new user first.")
        return

    number = input("Enter the new account number: ")
    new_account = Account.new_account(user, number)
    user.add_account(new_account)
    accounts.append(new_account)
    print("Account created successfully!\n")

# Function to print account details
def print_account_details(account):
    print(f"\nCPF: {account.client.cpf}")
    print(f"Agency: {account.agency} \nAccount Number: {account.number}\nAccount Holder: {account.client.name}")
    print(f"Available Balance: R$ {account.balance:.2f}")

# Function to list all accounts
def list_accounts(accounts):
    for account in accounts:
        line = f"Agency: {account.agency}, Number: {account.number}, Account Holder: {account.client.name}"
        print(line)

# Main function
def main():
    users = []
    accounts = []

    while True:
        option = menu()
        if option == 'd':
            value = float(input("\nEnter the deposit amount: R$ "))
            account_number = input("Enter the account number: ")
            account = next((account for account in accounts if account.number == account_number), None)
            if account:
                deposit(account, value)
            else:
                print("Account not found.")
        elif option == 's':
            value = float(input("\nEnter the withdrawal amount: R$ "))
            account_number = input("Enter the account number: ")
            account = next((account for account in accounts if account.number == account_number), None)
            if account:
                withdraw(account, value)
            else:
                print("Account not found.")
        elif option == 'c':
            account_number = input("Enter the account number: ")
            account = next((account for account in accounts if account.number == account_number), None)
            if account:
                check_balance(account)
            else:
                print("Account not found.")
        elif option == 'e':
            account_number = input("Enter the account number: ")
            account = next((account for account in accounts if account.number == account_number), None)
            if account:
                display_statement(account)
            else:
                print("Account not found.")
        elif option == 'm':
            print("Change password option not implemented yet.")
        elif option == 'nc':
            create_account(users, accounts)
        elif option == 'dc':
            account_number = input("Enter the account number: ")
            account = next((account for account in accounts if account.number == account_number), None)
            if account:
                print_account_details(account)
            else:
                print("Account not found.")
        elif option == 'l':
            list_accounts(accounts)
        elif option == 'n':
            create_user(users)
        elif option == 'x':
            print("Exiting the system...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
