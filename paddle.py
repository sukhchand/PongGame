from turtle import Turtle

STARTING_POSITION = [(350,40),(350,20),(350,0), (350,-20), (350, -40)]
class Paddle(Turtle):
    def __init__(self, coordinate):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.coordinate = coordinate
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.teleport(self.coordinate[0], self.coordinate[1])


    def up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        self.goto(self.xcor(), self.ycor()-20)

