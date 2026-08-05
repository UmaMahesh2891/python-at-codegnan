users={
        1001:{'name':"Uma",'gmail':"umamahesh.2891@gmail.com",'balance':5000,'password':'1001'},
        1002:{'name':"Mahesh",'gmail':"ramisettiumamahesh3165@gmail.com",'balance':1000,'password':'1002'}
        }

def transfer(sender_account:int,receiver_account:int,transfer_amount:int)-> str:
    if receiver_account not in users:
        return "Receiver account does not exist"
    if sender_account == receiver_account:
        return "Cannot transfer to the same account"

    sender_balance = users[sender_account]['balance']
    if sender_balance >= transfer_amount:
        users[sender_account]['balance'] -= transfer_amount
        users[receiver_account]['balance'] += transfer_amount
        return f"{transfer_amount} transferred successfully to account {receiver_account} and\
                         current balance is :{users[sender_account]['balance']}"
    return "Insufficient Amount"