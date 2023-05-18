from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
from datetime import datetime

name=input("enter your name:")

lists='''
cashews Rs 600/kg
honey Rs 225/kg
sugar Rs 25/kg
salt Rs 5/kg
ghee Rs 500/kg
oil Rs 125/kg
'''
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

items={'cashews': 600,
        'honey': 225, 
        'sugar': 25, 
        'salt': 5, 
        'ghee': 500, 'oil': 125}
option=int(input("for list of items press 1"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input('Enter the name of items:')
        quantity=int(input("Enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Please enter a correct item")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","United Brothers Super market",25*"=")
            print(28*"","Newark")
            print("Name",name,30*"","Date",datetime.now())
            print(75*"-")
            print("sno",6*"",'items',6*"",'quantity',3*"",'price')         
            for i in range(len(pricelist)):
                print(i,6*'',6*'',ilist[i],qlist[i],3*'',plist[i])
            print(75*"-")
            print(50*"",'Total amount:','Rs',totalprice)
            print("gst amount", 50*"","Rs",gst)
            print(75*"-")
            print(50*"",'Finalamount:','Rs',finalamount)
            print(75*"-")
            print(50*"", "Thanks for visiting")
            print(50*"")


