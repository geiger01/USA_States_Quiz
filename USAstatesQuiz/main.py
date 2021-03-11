import turtle 
import pandas

screen=turtle.Screen()
screen.title("U.S. States Game")
image= "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

text= screen

data = pandas.read_csv('50_states.csv')
countries= data.state
guessed_states=[]

states_list=[]
for state in countries:
    states_list.append(state)



while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states=[state for state in countries if state not in guessed_states]
        new_data= pandas.DataFrame(missing_states)
        new_data.to_csv("States_You_Did_Not_Get.csv")

        break

    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state==answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state,align="center",font=("ariel",11, "normal"), move=True )
   







screen.exitonclick()