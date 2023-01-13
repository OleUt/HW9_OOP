class Car(object):

    def __init__(self, model, color, engine_capacity):
        self.model = model
        self.color = color
        self.engine_capacity = engine_capacity

    def move_forvard(self):
        return f'method "move forward" for {self.color, self.model} called'

    def move_back(self):
        return f'method "move back" for {self.color, self.model} called'


class CarAdd(Car):

     def turn_right(self):
        return f'method "turn right" for {self.color, self.model} called'

     def turn_left(self):
        return f'method "turn left" for {self.color, self.model} called'


opel = Car('Opel', 'white', 1.6)
print(opel.move_forvard())
print(opel.move_back())

mazda = CarAdd('Mazda', 'red', 2.0)
print(mazda.move_forvard())
print(mazda.move_back())
print(mazda.turn_left())
print(mazda.turn_right())
