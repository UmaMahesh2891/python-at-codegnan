users={
        1001:{'name':"Uma",'gmail':"umamahesh.2891@gmail.com",'balance':5000,'password':'1001'},
        1002:{'name':"Mahesh",'gmail':"ramisettiumamahesh3165@gmail.com",'balance':1000,'password':'1002'}
        }

def get_balance(account:int)-> str:
    curr_balance = users[account]['balance']
    return f"Current Balance is:{curr_balance}"