users={
        1001:{'name':"Uma",'gmail':"umamahesh.2891@gmail.com",'balance':5000,'password':'1001'},
        1002:{'name':"Mahesh",'gmail':"ramisettiumamahesh3165@gmail.com",'balance':1000,'password':'1002'}
        }

def deposit(account:int,deposit_amount:int)-> str:
    users[account]['balance'] += deposit_amount
    return f"{deposit_amount} deposite successful and\
                             current balance is :{users[account]['balance']}"
