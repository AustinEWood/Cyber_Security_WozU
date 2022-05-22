class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width*self.height

area = Rectangle(3,6)

print(area.area())


class Greeter:
    """ This is a greeter"""

    @staticmethod
    def greet(people):
        """Static method to greet a list of people"""
        greetings = []
        for person in people:
            greeting = "Hello " + person.firstName + " " + person.lastName + "!"
            greetings.append(greeting)
        return greetings
