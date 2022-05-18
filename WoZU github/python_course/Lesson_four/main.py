#Part 1

print("List of animals")

print("\n")

willow = {
    "Type": "Dog" ,
    "Color": "Black & Brown" ,
    "Nickname": "None" ,
    "Owner's name": "Joe" ,
}

puff = {
    "Type": "Cat" ,
    "Color": "Grey & Black" ,
    "Nickname": "None" ,
    "Owner's name": "Jules"
}

for key, value in puff.items():
    print(key, ':', value)

print("\n")

for key, value in willow.items():
    print(key, ':', value)

print("\n")




#Part 2

print("List of citys")

print("\n")

florida = {
    'Capital': 'Tallahassee',
    'The population of Tallahassee is':'192,885 thousand',
    'Interesting fact': 'The oldest inhabited city in the country resides in Florida.',
    'Language': 'English',
}
ohio = {
    'Capital': 'Columbus', 
    'The population of Columbus is': '889.079 thousand', 
    'Interesting fact': 'Believed to have been the first state to have an African American elected to public office.',
    'Language': 'English'
}
texas = {
    'Capital': 'Austin',
    'The population of Austin is': '965,872 thousand',
    'Interesting fact': 'Dr Pepper was invented in Texas in 1885.',
    'Language': 'English'
}
england = {
    'Capital': 'London',
    'The population of England is': '53.01 million',
    'Interesting fact': 'The National dish is an Indian food.',
    'Language': 'English'
}
france = {
    'Capital': 'Paris', 
    'The population of France is': '66.9 million',
    'Interesting fact': 'The Tour de France cycle race has been running for over 100 years.',
    'Language most spoken': 'French'
}
belgium = {
    'Capital': 'Brussels', 
    'The population of Belgium is': '11.35 million', 
    'Interesting fact': 'Belgium produces more than 220,000 tons of chocolate per annum.',
    'Language most spoken': 'Dutch'
}

for key, value in florida.items():
    print(key, ':' , value)

print("\n")

for key, value in ohio.items():
    print(key, ':', value)

print("\n")

for key, value in texas.items():
    print(key, ':', value)

print("\n")

for key, value in england.items():
    print(key, ':', value)

print("\n")

for key, value in france.items():
    print(key, ':', value)

print("\n")

for key, value in belgium.items():
    print(key, ':', value)
