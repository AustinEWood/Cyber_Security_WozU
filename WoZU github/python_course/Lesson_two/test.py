import datetime
import this

this_year = datetime.datetime.now().year
this_day = datetime.datetime.now().day
this_month = datetime.datetime.now().month




while 1==1:
    try:
        month = int(input("Month? "))
    except:
        print("Numbers only please! ") 
    try:
        day = int (input("Day? "))
    except:
        print("Numbers only please! ")
    try:
        year = int(input("Year? "))
    except:
        print("Numbers only please! ")

    birthdate = str(month) + " " + str(day) + ", " + str(year)
    print(birthdate)
    break
   

  
#day = input("Birthday? ")
#year = input("Birth year? ")










#if int(day) == int(this_day) and int(month) == int(this_month) :
 #   print("It is your birthday")
#else:
 #   print("It is not your birthday")


#if int(month) == int(this_month) and int(day) <= int(this_day):
    #age = int(this_year) - int(year) 
    #print("You are " + str(age) + " years old!")
#elif  int(month) == int(this_month) and int(day) > int(this_day):
    #age = int(this_year) - int(year) - 1
    #print("You are " + str(age) + " years old!")
#elif int(month) < int(this_month):    
    #age = int(this_year) - int(year)
    #print("You are " + str(age) + " years old!")
#else:
    #age = int(this_year) - int(year) - 1
    #print("You are " + str(age) + " years old!")


#print(this_month)

#age = int(this_year) - int(year)
#print("You are " + str(age) + " years old!")

#if age >= 18:
    #print("Permitted to attend alone")
#elif age >= 15:
    #print("Permitted with anyone over 18")    
#elif age >= 10:
    #print("Permitted with a parent")
#else:
    #print("Not permitted")
