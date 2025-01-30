#   a123_apple_1.py
import random
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

pear_image = "pear.gif"

#drawer = trtl.Turtle()

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)

#apple = trtl.Turtle()
# pear = trtl.Turtle()



#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def draw_pear(active_pear):
  active_pear.shape(pear_image)
  wn.update()

#def apple_fall():
 # global apple
  #erase_an_A()
  #x = apple.xcor()
  #y = apple.ycor()
  #apple.penup()
  #apple.goto(x, y-140)

# def draw_an_A():
#   drawer.hideturtle()
#   drawer.goto(-18,-35)
#   drawer.color("white")
#   drawer.write("A", font=("Arial", 40, "bold")) 

# def erase_an_A():
#   global drawer
#   drawer.clear()

letters = ["a","s","d","f"]
def make_turtles(letters):
  turtles = []
  for _ in letters:
    t = trtl.Turtle()
    t.penup()
    draw_apple(t)
    t.goto(random.randint(-100,100), random.randint(-10,90) )
    turtles.append(t)
  return turtles

def draw_letters(letters, turtles):
  drawers=[]
  for i in range(len(turtles)):
    drawer = trtl.Turtle()
    drawer.penup()
    drawer.hideturtle()
    turtle = turtles[i]
    drawer.goto(turtle.xcor()-18, turtle.ycor()-35)
    drawer.write(letters[i], font = ("Arial", 40, "bold"))
    drawers.append(drawer)
  return drawers

#-----function calls-----

#draw_apple(apple)
#draw_an_A()
#wn.onkeypress(apple_fall, "a")
turtles = make_turtles(letters)
drawers = draw_letters(letters, turtles)



wn.listen()
wn.mainloop()
