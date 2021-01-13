import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")

correct_guesses = []

while len(correct_guesses) < 50:
    user_answer = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                   prompt="Enter the name of a state, or 'exit' to quit").title()
    if user_answer == "Exit":
        new_data = {"state": [item for item in data["state"].values if item not in correct_guesses]}
        final_data = pandas.DataFrame(new_data)
        final_data.to_csv("states_to_learn.csv")
        break
    if user_answer in data["state"].values:
        correct_guesses.append(user_answer)
        i_val = data[data["state"] == user_answer].index.values.astype(int)[0]
        x_cor = data["x"][i_val]
        y_cor = data["y"][i_val]
        writer = turtle.Turtle()
        writer.penup()
        writer.hideturtle()
        writer.goto(x_cor, y_cor)
        writer.write(user_answer, align="center", font=("Arial", 8, "bold"))
