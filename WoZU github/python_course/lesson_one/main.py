from multiprocessing.connection import wait
from time import time
from unicodedata import name
import sys
import time 

print("This will tell you how many months your age is equal to.")
time.sleep(2) #Sleep for 2 seconds
print("Example")
time.sleep(2) #Sleep for 2 seconds
print("What is your name?")
time.sleep(2)  # Sleep for 2 seconds
print('My name is "Billy"')
time.sleep(2)  # Sleep for 2 seconds
print("How old are you?")
time.sleep(2)  # Sleep for 2 seconds
print("30")
time.sleep(2)  # Sleep for 2 seconds
print("How many months is that?")
time.sleep(2)  # Sleep for 2 seconds
print("360")

print("")

time.sleep(2)  # Sleep for 2 seconds
print("Your turn!")
time.sleep(2)  # Sleep for 2 seconds
name = input("What is your name? ");
time.sleep(2)  # Sleep for 2 seconds
print("Your name is " + name)
time.sleep(2)  # Sleep for 2 seconds
age = input("How old are you? ")
time.sleep(2)  # Sleep for 2 seconds
print("You are " + age)
time.sleep(2)  # Sleep for 2 seconds
print("How many months is that? ")
time.sleep(2)  # Sleep for 2 seconds
my_integer = 12*int(age)
print(my_integer)

my_string = "I hope you like the code!"
print(my_string)
my_float = 1.1
print("Version")
print(my_float)
