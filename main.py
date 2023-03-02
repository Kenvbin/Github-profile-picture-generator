import turtle as ts
import random
import turtle as trtl
import turtle
turtle.screensize(canvwidth=5, canvheight=10, bg="white")

trtl.setposition(0,-200)
painter = trtl.Turtle()
painter.hideturtle()
trtl.hideturtle()
trtl.speed(0)
trtl.penup()
trtl.setposition(0,-200)
trtl.forward(200)
trtl.left(90)
trtl.pendown()

savec = "whee"
saves = "whee"

colourlor = random.randint(1,5)
def box():
  trtl.pensize(5)
  for i in range(5):
    trtl.forward(400)
    trtl.left(90)
  trtl.pensize(1)
if colourlor == 1:
  trtl.color("orange red")
  savec = "orange red"
if colourlor == 2:
  trtl.color("dark red")
  savec = "dark red"
if colourlor == 3:
  trtl.color("deep sky blue")
  savec = "deep sky blue"
if colourlor == 4:
  trtl.color("royal blue")
  savec = "royal blue"
if colourlor == 5:
  trtl.color("hot pink")
  savec = "hot pink"
trtl.begin_fill()
trtl.color("Black")
box()
trtl.color(savec)
trtl.end_fill()
trtl.color("Black")
trtl.penup()
trtl.forward(200)
trtl.left(90)
trtl.forward(400)

def square():
  for i in range(5):
    trtl.forward(50)
    trtl.left(90)

def squaree():
  for i in range(5):
    trtl.forward(50)
    trtl.right(90)

colourlor = random.randint(1,5)
if colourlor == 1:
  trtl.color("crimson")
  saves = "crimson"
if colourlor == 2:
  trtl.color("spring green")
  saves = "spring green"
if colourlor == 3:
  trtl.color("gold")
  saves = "gold"
if colourlor == 4:
  trtl.color("navajo white")
  saves = "navajo white"
if colourlor == 5:
  trtl.color("Violet")
  saves = "Violet"
trtl.left(180)

for i in range(25):
  mooverlooverx = random.randint(0,145)
  mooverloovery = random.randint(0,345)
  trtl.setposition(0,-200)
  trtl.forward(mooverloovery)
  trtl.right(90)
  trtl.forward(mooverlooverx)
  trtl.pendown()
  trtl.begin_fill()
  trtl.color(saves)
  square()
  trtl.color(saves)
  trtl.end_fill()
  trtl.penup()
  trtl.setposition(0,-200)
  trtl.forward(mooverloovery)
  trtl.left(90)
  trtl.forward(mooverlooverx)
  trtl.pendown()
  trtl.begin_fill()
  trtl.color(saves)
  squaree()
  trtl.color(saves)
  trtl.end_fill()
  trtl.penup()


ts.getscreen()
funke = random.randint(0,99999)
wonger = str(funke) + ".eps"
ts.getcanvas().postscript(file=wonger)
