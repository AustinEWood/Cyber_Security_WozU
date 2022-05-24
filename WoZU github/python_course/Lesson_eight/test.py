class Animal:
    """This is an animal"""

    def giveBirth(self):
        """Return the birthing method"""
        return "I don't know how"


class Mammal(Animal):

  def giveBirth(self):
    return "I give live birth"


class Bird(Animal):

  def giveBirth(self):
    return "I lay eggs"


class Animal:
  def __init__(self, name, birthMethod):
    self.name = name
    self.birthMethod = birthMethod

  def giveBirth(self):
    return self.birthMethod


class Bird(Animal):
    """This is a bird"""

    def __init__(self, name, flies):
        """Initializer"""
        super().__init__(name, "eggs")
        self.flies = flies

