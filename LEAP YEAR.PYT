year=float(input("enter a year "))
if(year==0):
    print("invalid enter a valid year ")
elif(year==19.47):
    print("invalid enter a valid year ")
elif(year%400==0)&(year%100==0):
    print("then it is a leap year ")
elif(year%4==0)&(year%100!=0):
    print("then it is a leap year ")
else:
    print("then it is not a leap year ")
