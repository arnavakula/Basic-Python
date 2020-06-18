'''
account is the object
attributes: init balance, 
instance vars: filepath, balance
'''
class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as f:
            self.balance = int(f.read())

    def get_balance(self):
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= int(amount)
        self.commit()
    
    def deposit(self, amount):
        self.balance += int(amount)
        self.commit()

    def commit(self):
        with open(self.filepath, 'w') as f:
            f.write(str(self.balance))


acc1 = Account('balance.txt')
acc1.deposit(100)
print(acc1.balance)