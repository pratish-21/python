weight=int(input("enter weight in kgs : "))
height=float(input("enter height in mtrs : "))
BMI=round(weight/height**2)
print("Your BMI is : ",str(BMI))
if(BMI<18.5):
    print("You are under weight :(")
elif(BMI<25):
    print("You are ok :)")
elif(BMI<35):
    print("You are obseity 1")
elif(BMI<55):
    print("You are obseity 2")
elif(BMI<75):
    print("You are obseity 3")
else:
    print("please check your existence!!!")