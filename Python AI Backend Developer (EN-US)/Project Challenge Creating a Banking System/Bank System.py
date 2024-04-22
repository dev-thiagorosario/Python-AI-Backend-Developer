# Initialization of variables
balance = 0
limit = 1000
statement = []
number_of_withdrawals = 0
WITHDRAWAL_LIMIT = 3

# Options menu
menu = """
[d] Deposit
[w] Withdraw
[b] Check balance
[t] Transfer
[s] Statement
[q] Quit

Choose an option: """

while True:
    option = input(menu)
    if option == 'd':  # Deposit money into the account
        amount = float(input("How much would you like to deposit? "))
        balance += amount
        statement.append(['Deposit', amount])

    elif option == 'w':  # Withdraw money from the account
        if number_of_withdrawals >= WITHDRAWAL_LIMIT:
            print(f'You have already made {WITHDRAWAL_LIMIT} consecutive withdrawals!')
        else:
            amount = float(input("How much would you like to withdraw? "))
            if amount > balance:
                print('\033[0;31mYou do not have that amount available!\033[m')
            else:
                balance -= amount
                number_of_withdrawals += 1
                statement.append(['Withdrawal', amount])

    elif option == 'b':  # Check the account balance
        print(f"\nCurrent balance: ${balance:.2f}")
        print(f"Credit limit: ${limit:.2f}\n")

    elif option == 't':  # Bank Transfer
        recipient_account = input("Enter the recipient's account number: ")
        amount = float(input("What is the amount you want to transfer? "))
        if amount <= balance:
            balance -= amount
            statement.append(['Transfer', amount, recipient_account])
        else:
            print('\033[0;31mYou do not have that amount available.\033[m')

    elif option == 's':  # Transaction History
        print('\n\033[7;40;44mTransaction History:\033[m')
        for transaction in statement:
            print(f"Type: {transaction[0]}, Amount: ${transaction[1]:.2f}, Details: {transaction[2] if len(transaction) > 2 else ''}")

    elif option == 'q':  # Close and exit the program
        print('\nThank you for using our services! See you soon!')
        break
