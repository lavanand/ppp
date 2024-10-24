days=int(input("Enter your days"))
if(days==0):
    print("NO fine")
elif days>=1 and days<=5:
    print("fine amount",days*5)
elif days>=6 and days<=10:
    print("Fine amount=",days*10)     
elif days>=11 and days<=15:
    print("fine amount=",days*15)
else:
    print("Membership cancel")    
 