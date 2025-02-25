class Account():
    def __init__(self,bal, acc):
        self.balance = bal
        self.account = acc
    def debit(self,amount):
        self.balance -=amount
        print(f"{amount} has been debited from your account {self.account}")
        print(f'total balance :', self.get_balance())

    def credit(self, amount):
        self.balance +=amount
        print(f"{amount} has been credited to your account {self.account}")
        print(f'total balance :', self.get_balance())

    def get_balance(self):
        return self.balance
acc1= Account(100, 10575)
acc1.debit(30)
acc1.credit(50)
