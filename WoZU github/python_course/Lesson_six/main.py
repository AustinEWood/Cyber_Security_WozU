class Stadium:
    """class for stadium"""
    def __init__(self, name, city_state, capacity, sport, seats):
        """init method to apply names for self"""
        self.name = name
        self.city_state = city_state
        self.capacity = capacity
        self.sport = sport
        self.seats = seats

    def describe_stadium(self):
        """adding all the information togeather by using names applied"""
        return "The " + str(self.name) + " is located in " + str(self.city_state) + " and holds " + str(self.capacity) + " fans."

    def sport_played(self):
        """sport played at arena"""
        return "The following sport is mainly played in this stadium: " + str(self.sport)
    def seat_available(self):
        """number of seats in arena"""
        return "There are " + str(self.seats) + " still available for tonight's game."

stadium1 = Stadium("Mercedes Benz Arena", "Atlanta, GA", "70,0000", "Football", "15000")

print(stadium1.describe_stadium())
print(stadium1.sport_played())
print(stadium1.seat_available())