import turtle as t

class Rectangle(t.RawTurtle):
    def __init__(self, screen=t.Screen(), width=0, height=0):
        super().__init__(screen)
        self.screen = screen
        self.width = width
        self.height = height

    def draw(self):
        for i in range(2):
            self.fd(self.height)
            self.right(90)
            self.fd(self.width)
            self.right(90)

    def move_forward(self, unit):
        self.clear()
        self.penup()
        self.fd(unit)
        self.pendown()
        self.draw()

    def move_backward(self, unit):
        self.clear()
        self.penup()
        self.bk(unit)
        self.pendown()
        self.draw()

    def turn_right(self, angle=90):
        self.right(angle)
        self.clear()
        self.draw()

    def turn_left(self, angle=90):
        self.left(angle)
        self.clear()
        self.draw()
