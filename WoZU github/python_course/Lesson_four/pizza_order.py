while True: 

    pizza_order = {
        "Customer's name": "",
        "Pizza size": "small, medium, or large",
        "Pizza crust": "hand tossed, flat, or orginal",
        "Toppings": "extra cheese, sausage, or bacon",
    }


    pizza_order["Customer's name"] = input("Name? ")

    print("Please select a size " + pizza_order["Pizza size"])

    pizza_order["Pizza size"] = input("What size would you like? ")


    while True:
        if pizza_order["Pizza size"] == "small":
            print("Please select crust " + pizza_order["Pizza crust"])
            pizza_order["Pizza crust"] = input("What crust would you like? ")
            break
        elif pizza_order["Pizza size"] == "medium":
            print("Please select crust " + pizza_order["Pizza crust"])
            pizza_order["Pizza crust"] = input("What crust would you like? ")
            break
        elif pizza_order["Pizza size"] == "large":
            print("Please select crust " + pizza_order["Pizza crust"])
            pizza_order["Pizza crust"] = input("What crust would you like? ")
            break
        else:
            print("Please select only small, medium, or large")
            pizza_order["Pizza size"] = input("What size would you like? ")



    while True:
        if pizza_order["Pizza crust"] == "hand tossed":
            print("Please select toppings " + pizza_order["Toppings"])
            pizza_order["Toppings"] = input("what toppings would you like? ")
            break
        elif pizza_order["Pizza crust"] == "flat":
            print("Please select toppings " + pizza_order["Toppings"])
            pizza_order["Toppings"] = input("what toppings would you like? ")
            break
        elif pizza_order["Pizza crust"] == "original":
            print("Please select toppings " + pizza_order["Toppings"])
            pizza_order["Toppings"] = input("what toppings would you like? ")
            break
        else:
            print("Please select only hand tossed, flat, or orginal")
            pizza_order["Pizza crust"] = input("What crust would you like? ")

    while True:
        if pizza_order["Toppings"] == "extra cheese":
            break
        elif pizza_order["Toppings"] == "sausage":
            break
        elif pizza_order["Toppings"] == "bacon":
            break
        else:
            print("Please select only extra cheese, sausage, or bacon")
            pizza_order["Toppings"] = input("what toppings would you like? ")



    print("\n")

    print("Thank you for your order, " + pizza_order["Customer's name"])

    print("You have orderd a " + pizza_order["Pizza size"] + ", " + pizza_order["Pizza crust"] + " with the following toppings: " + pizza_order["Toppings"])

    print("\n")

    print("Would you like to make another order?")
    new_order = input("yes or no: ")

    if new_order == "yes":
        print("ok")
    elif new_order == "y":
        print("ok")
    else:
        print("goodbye " + pizza_order["Customer's name"])
        break