import turtle


class WritingTurtle(turtle.Turtle):
    """This class has only an attributes which moves the turtle to the location specified in the parameter and
    writes at that particular location"""
    def __init__(self, xcor, ycor, user_guess):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(xcor, ycor)
        self.write(f"{user_guess}", False, "center", ("arial", 9, "bold"))


