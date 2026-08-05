from database import users


def get_balance(account):

    return users[account]["balance"]


def withdraw(account, amount):

    balance = users[account]["balance"]

    if balance >= amount:

        users[account]["balance"] -= amount

        return f"Withdraw successful.\nCurrent balance: {users[account]['balance']}"

    return "Insufficient balance"


def deposit(account, amount):

    users[account]["balance"] += amount

    return f"Deposit successful.\nCurrent balance: {users[account]['balance']}"


def transfer(sender, receiver, amount):

    if receiver not in users:
        return "Receiver account not found"

    if sender == receiver:
        return "Cannot transfer to the same account"

    if users[sender]["balance"] >= amount:

        users[sender]["balance"] -= amount
        users[receiver]["balance"] += amount

        return (
            f"{amount} transferred successfully.\n"
            f"Current balance: {users[sender]['balance']}"
        )

    return "Insufficient balance"