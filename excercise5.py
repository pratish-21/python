age=int(input("enter your age : "))
years_left=90-age
days_left=years_left*365
months_left=years_left*12
weeks_left=years_left*52

print("years left : ",years_left)
print("days left : ",days_left)
print("months_left : " ,months_left)
print("weeks left : " ,weeks_left)

print(f"you have {days_left} days , {weeks_left} weeks and {months_left} months")
