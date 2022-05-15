import time
import datetime

this_year = datetime.datetime.now().year
this_day = datetime.datetime.now().day
this_month = datetime.datetime.now().month

print("What is your birthday?")

time.sleep(1)

print("Example. 3 19, 1992")

time.sleep(1)
month = int(input("Month? "))
day = input("Day? ")
year = input("Year? ")

time.sleep(1)

my_birthday = str.format("{} {}, {}", month, day, year)
print(my_birthday)

time.sleep(1)

first = "Happy"
second = "birthday"
third = "to"
fourth = "you!"

final = first + " " + second + " " + third + " " + fourth

if int(month) == int(this_month) and int(day) == int(this_day):
    print(final)
else:
    print("It is not your birthday.")    


if int(month) == int(this_month) and int(day) <= int(this_day):
    age = int(this_year) - int(year)
    print("You are " + str(age) + " years old!")
elif int(month) == int(this_month) and int(day) > int(this_day):
    age = int(this_year) - int(year) - 1
    print("You are " + str(age) + " years old!")
elif int(month) < int(this_month):
    age = int(this_year) - int(year)
    print("You are " + str(age) + " years old!")
else:
    age = int(this_year) - int(year) - 1
    print("You are " + str(age) + " years old!")

time.sleep(1)

if age >= 18:
    print("Permitted to attend alone!")
elif age >= 15:
    print("Permitted with anyone over 18!")
elif age >= 10:
    print("Permitted with a parent!")
else:
    print("Not permitted!")


