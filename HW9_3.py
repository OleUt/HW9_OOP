import math

class Parallelogram():

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self, angle):
        area = self.width * self.length * math.sin(angle)
        return area

class Square(Parallelogram):

    def get_area(self):
        area = Parallelogram.get_area(self, math.pi/2)
        return area


p1 = Parallelogram(2, 3)
my_angle = 1.57
print('parallelogram area =', p1.get_area(my_angle))

p2 = Square(2, 3)
print('square area =', p2.get_area())

