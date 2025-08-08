""""
a=51
if(a%2==0):
    print("even")
    if(a>30):
        print("great")
print("bye")
"""

height=int(input("enter height : "))
if(height>=3):
    print("can ride")
    age=int(input("enter age : "))
    if(age<=12):
        print("you need to pay 150 rs")
    elif(age<=18):
        print("you need to pay 250 rs")
    else:
        print("pay 500 rs")
else:
    print("you cannot ride")
print("bye")

