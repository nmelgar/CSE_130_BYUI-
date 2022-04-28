from datetime import datetime

today = datetime.now()
today_year = today.year

name = str(input("Please enter your name: "))
birth_year = int(input("Please enter your birth year (Ex. 1996): "))
age = today_year - birth_year

if age > 1:
    print(f"Hello {name.capitalize()}. You are {age} years old.")
else:
    print(f"Hello {name.capitalize()}. You are {age} year old.")