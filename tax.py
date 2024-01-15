def calc(money,month,taxrate,incomerate):
    income = money*incomerate*month
    tax = income*taxrate
    total = money+income-tax
    return total
    

money = input('enter the money you want to save:')
month = input('how many month will you save:')


#money = int(money)
#month = int(month)
if int(money) < 5000 :
    incomerate =12/100
    taxrate=0
    print(calc(int(money),int(month),taxrate,incomerate))
elif int(money) <10000:
    incomerate =15/100
    taxrate=10/100
    print(calc(int(money),int(month),taxrate,incomerate))
elif int(money) >10000:
    incomerate =18/100
    taxrate=15/100
    print(calc(int(money),int(month),taxrate,incomerate))
else:
    print('error')

