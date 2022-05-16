# Part 1
list_of_names = ['Kurt', 'David', 'Katherine']

for name in list_of_names:
    print("Where is " + name + " today?")

# Part 2

my_favorite_cars = ["BMW", "Toyota", "Mazda"]
my_favorite_flowers = ["Rose", "Sunflower", "Tulip", "Daisy"]
my_favorite_animals = ["Cat", "Dog", "Giraffe", "Elephant", "Lion"]

my_favorite_things = my_favorite_cars + \
    my_favorite_flowers + my_favorite_animals

for thing in my_favorite_things:
    if len(thing) % 2 == 0:
        print(thing)

# Part 3

number_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for number in number_range:
    if number % 3 == 0 and number % 5 == 0:
        print('ZipZap')
    elif number % 3 == 0:
        print('Zip')
    elif number % 5 == 0:
        print('Zap')
    else:
        print(number)
