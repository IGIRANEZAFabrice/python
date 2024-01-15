class User() :
    def  __init__(self,fName,lName,gender,age,tel):
        self.fName = fName
        self.lName = lName
        self.gender = gender
        self.age = age
        self.tel = tel
    def details(self):
        print("PERSOAL DETAILS")
        print("")
        print("names: ",self.fName," " ,self.lName)
        print("gender: ",self.gender)
        print("age: ",self.age)
        print("tel: ",self.tel)

class Bank(User):
    def __init__(self, fName, lName, gender, age, tel):
        super().__init__(fName, lName, gender, age, tel)
        self.balance = 0
    
    def accountBalance(self):
       print(self.balance)
    def deposit(self,deposited):
        self.deposited = deposited
        self.balance= self.balance + deposited
        print("new balance is : ",self.balance)
    def withdraw(self,withdrawn):
        self.withdrawn = withdrawn 
        if self.balance < self.withdrawn :
            print("insuficient amount")
        else:
            self.balance = self.balance - self.withdrawn
            print("withrawn ",withdrawn," new balance is ",self.balance)
    

fab = Bank("IGIRANEZA","Fabrice","male",20,"0784444314")
fab.details()
fab.deposit(60)
fab.accountBalance()
fab.withdraw(50)
fab.accountBalance()


