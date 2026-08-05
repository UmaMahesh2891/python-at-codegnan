from auth import login, register, logout
from banking import (
    get_balance,
    withdraw,
    deposit,
    transfer
)
from statement import mini_statement


print("Welcome to Mini Bank")

print("1. Login")
print("2. Register")

choice = int(input("Enter your choice: "))

if choice == 1:

    account = int(input("Enter account number: "))
    password = input("Enter password: ")

    if login(account, password):

        while True:

            print("\n1. Get Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Mini Statement")
            print("6. Logout")

            choice = int(input("Enter your choice: "))

            if choice == 1:

                print(get_balance(account))

            elif choice == 2:

                amount = int(input("Enter amount: "))

                print(withdraw(account, amount))

            elif choice == 3:

                amount = int(input("Enter amount: "))

                print(deposit(account, amount))

            elif choice == 4:

                receiver = int(
                    input("Enter receiver account: ")
                )

                amount = int(input("Enter amount: "))

                print(
                    transfer(
                        account,
                        receiver,
                        amount
                    )
                )

            elif choice == 5:

                mini_statement(account)

            elif choice == 6:

                logout()

            else:

                print("Invalid choice")

    else:

        print("Invalid credentials")

elif choice == 2:

    username = input("Enter username: ")
    gmail = input("Enter gmail: ")
    balance = int(input("Enter balance: "))
    password = input("Enter password: ")

    print(register(username, gmail, balance, password))

else:

    print("Invalid choice")