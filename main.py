import turtle
import pandas
from writing_turtle import WritingTurtle

# This creates the screen set the title and an image to
# shapes available in turtle and uses that shape as a background image
my_screen = turtle.Screen()
my_screen.title("U.S. States Game")
image = "blank_states_img.gif"
my_screen.addshape(image)
my_turtle = turtle.Turtle()
my_turtle.shape(image)

# This part uses panda to read the csv data and converts the CSV to a dictionary
us_state = pandas.read_csv("50_states.csv")
states_dict = us_state.to_dict()

score = 0
Question = True
while Question:
    # This asks the user for an input
    if score == 0:
        user_guess = my_screen.textinput("Guess the States", "Guess a State in the U.S").title()
    else:
        user_guess = my_screen.textinput(f"{score}/50 States Correct", "Guess a State in the U.S").title()
    xcor = ""
    ycor = ""
    # This part checks if the question is in the dictionary, writes it on the screen if it is
    # and also increases the score
    for i in range(50):
        if user_guess == states_dict["state"][i]:
            score += 1
            xcor = states_dict["x"][i]
            ycor = states_dict["y"][i]
            write = WritingTurtle(xcor, ycor, user_guess)

my_screen.exitonclick()

