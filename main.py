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

correct_states = []
learn_states = []
score = 0
Question = True
while Question:
    # This asks the user for an input
    if score == 0:
        user_guess = my_screen.textinput("Guess the States", "Guess a State in the U.S").title()
    else:
        user_guess = my_screen.textinput(f"{score}/50 States Correct", "Guess a State in the U.S").title()

    # This ends the game anytime the user press exit and make a csv file of states to learn
    if user_guess == "Exit":
        for i in range(len(states_dict["state"])):
            if states_dict["state"][i] not in correct_states:
                learn_states.append(states_dict["state"][i])
        new_data_frame = pandas.DataFrame(learn_states)
        new_data_frame.to_csv("states_to_learn.csv")
        break

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
            correct_states.append(user_guess)

    # This makes sure the while loop ends after the user has gotten all the states
    if score == 51:
        Question = False
