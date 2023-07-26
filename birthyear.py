from datetime import date
today = date.today()

birthYear = int(input("your birthday: "))
age = today.year - birthYear

if(age >= 15 and age <20):
    print("teenager")
print("your age: %d" %age)


