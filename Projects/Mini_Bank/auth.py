from database import users


def register(username, gmail, balance, password):

    account = max(users.keys()) + 1

    users[account] = {
        "name": username,
        "gmail": gmail,
        "balance": balance,
        "password": password
    }

    return f"Registration successful.\nYour account number is {account}"


def login(account, password):

    if account in users:

        if users[account]["password"] == password:
            return True

    return False


def logout():

    print("Bye Bye buddy, see you later")
    exit()