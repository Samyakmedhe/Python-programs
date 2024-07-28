class BankAccount():
    
    def __init__(self):
        name = input("Enter name  : ")
        self.Money = 0
        
    def Deposit(self):
        Amount = int(input("Enter Amount to be deposit : "))
        self.Money +=  Amount
        print("Amount Deposit : ",Amount)

    def Withdraw(self):
        Amount = int(input("Enter Amount to be withdraw : "))
        self.Money -= Amount
        print("Balance Amount : ",self.Money)

    def CalculateIntrest(self):
        ROI = 10.5
        self.Money * ROI
        print("CalulateIntrest : ",ROI)

            
s = BankAccount()

s.Deposit()
s.Withdraw()
s.CalculateIntrest()



