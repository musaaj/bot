import turtle as t
from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, screen=t.Screen(), size=0):
        super().__init__(screen, size, size)



