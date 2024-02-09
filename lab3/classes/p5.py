class bank:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        print("you had", self.balance)
        self.balance += amount
        print("you deposited",amount,"and your balance is", self.balance,"\n\n")
    def withdraw(self,amount):
        if amount > self.balance:
            print("error,you do not have enough money")
        else:
            print("your balance before withdraw",self.balance)
            print("you took ",amount)
            self.balance -= amount
            print("your balance after withdraw ", self.balance)

bank = bank("Aibar",42000)
bank.deposit(42500)
bank.withdraw(10000000)