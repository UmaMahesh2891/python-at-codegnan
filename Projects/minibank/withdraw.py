# import requirements
from emailsend import singleEmailSend

users={
        1001:{'name':"Uma",'gmail':"umamahesh.2891@gmail.com",'balance':5000,'password':'1001'},
        1002:{'name':"Mahesh",'gmail':"ramisettiumamahesh3165@gmail.com",'balance':1000,'password':'1002'}
        }

def withdraw(account:int,withdraw_amount:int)-> str:
    curr_balance = users[account]['balance']
    if curr_balance >= withdraw_amount:
        users[account]['balance'] -= withdraw_amount
        # send email
        singleEmailSend(to_email=users[account]['gmail'] ,subject="withdraw Alert",body=f"{withdraw_amount} withdraw successful and\
                         current balance is :{users[account]['balance']}")
        return f"{withdraw_amount} withdraw successful and\
                         current balance is :{users[account]['balance']}"
    return "Insufficient Amount" 