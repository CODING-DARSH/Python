# generate a bank acc system with constructor and args

class Bank:
    def __init__(self,*deposit):
        self.deposit=deposit    #it will store tuple in it so we need to use loop
    def deposit_amount(self):
        amount=0
        for d in self.deposit:
            amount+=d
        return amount
B=Bank(100,200,300)
netamount=B.deposit_amount()
print(netamount)
