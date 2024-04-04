from turtle import Turtle,Screen
START_POSTION=[(0,0),(-20,0),(-40,0)]
MOVE_FORWARD=20
class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
    def createa_snake(self):
         for postion in START_POSTION:
            new_tom = Turtle("square")
            new_tom.color("white")
            new_tom.penup()
            new_tom.goto(postion)
            self.segment.append(new_tom)

    def move(self):
        for seg_num in range(len(self.segment) - 1,0,-1):
            new_x= self.segment[seg_num-1].xcor()
            new_y =self. segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(MOVE_FORWARD)





