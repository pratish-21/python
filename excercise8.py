year=int(input("enter a year : "))
if (year%4 == 0):
    if(year%100==0):
        if(year%400==0):
            print("leap year - has 366 days")
        else:
            print("not a leap year - has 365 days")

    else:
        print("leap year - has 366 days")
else :
    print("not a leap year - has 365 days")






