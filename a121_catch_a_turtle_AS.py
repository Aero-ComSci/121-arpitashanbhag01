# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
color = "pink"
size = 2
shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
colors = ["red", "orange", "yellow", "green", "purple"]
sizes = [0.5, 1, 1.5, 2, 2.5, 3]

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(shape)
spot.turtlesize(size)
spot.color(color)

score_writer = trtl.Turtle()
counter =  trtl.Turtle()

#-----game functions--------
def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
    
def change_position():
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    spot.penup()
    spot.goto(new_xpos, new_ypos)
    update_score()

def addcolor():
  randomcolor = rand.choice(colors)
  spot.color(randomcolor)
  spot.stamp()
  spot.color(color)

def changesize():
  randomsize = rand.choice(sizes)
  spot.turtlesize(randomsize)

def spot_clicked(x, y):
    global timer_up
    spot.penup()
    spot.hideturtle()
    change_position()
    spot.pendown()
    changesize()
    addcolor()
    spot.showturtle()
    if timer_up == True:
      spot.hideturtle()

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def start_game():
    global score, timer, timer_up
    score = 0
    timer = 30
    timer_up = False
    score_writer.clear()
    score_writer.write(score, font=font_setup)
    countdown()

#-----events----------------
spot.onclick(spot_clicked)
score_writer.penup()
score_writer.goto(100, -100)
counter.penup()
counter.goto(-100, -100)

wn = trtl.Screen()
wn.bgcolor("lightblue")
wn.ontimer(countdown, counter_interval) 
start_game()
wn.mainloop()
