'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
jeffery=turtle.Turtle()
x = 70
jeffery.begin_fill()
# This is for the 2
jeffery.penup()
jeffery.speed(10)
jeffery.pensize(10)
jeffery.goto(-200, 60)
jeffery.pendown()
jeffery.color("#BCFF00")
jeffery.left(x)
jeffery.forward(75)
jeffery.right(30)
for i in range(38):
    jeffery.right(2)
    jeffery.forward(5)
for i in range(35):
    jeffery.right(2)
    jeffery.forward(2)
print("cool debugging")
jeffery.forward(60)
for i in range(7):
    jeffery.right(7)
    jeffery.forward(8)
jeffery.forward(120)
for i in range(7):
    jeffery.right(-9)
    jeffery.forward(3)
jeffery.left(90)
jeffery.forward(25)
for i in range(35):
    jeffery.right(-2)
    jeffery.forward(.4)
jeffery.forward(15)
jeffery.right(x)
jeffery.forward(110)
jeffery.right(110)
jeffery.forward(100)
jeffery.right(x)
jeffery.forward(235)
jeffery.right(110)
jeffery.forward(100)
for i in range(30):
    jeffery.right(1.85)
    jeffery.forward(4)
for i in range(20):
    jeffery.left(2)
    jeffery.forward(4)
for i in range(20):
    jeffery.left(9)
    jeffery.forward(4)
jeffery.forward(15)
jeffery.right(50)
jeffery.forward(x)
jeffery.end_fill()
"This is now the 4"
jeffery.penup()
jeffery.color("#BCFF00")
jeffery.goto (20,-20)
jeffery.pendown()
jeffery.begin_fill()
jeffery.right(120)
jeffery.forward(180)
jeffery.right(60)
jeffery.forward(100)
jeffery.right(100)
jeffery.forward(180)
jeffery.left(90)
jeffery.forward(50)
jeffery.right(90)
jeffery.forward(x)
jeffery.right(90)
jeffery.forward(50)
jeffery.left(90)
jeffery.forward(90)
jeffery.right(90)
jeffery.forward(90)
jeffery.right(90)
jeffery.forward(x)
jeffery.left(90)
jeffery.forward(x)
jeffery.right(90)
jeffery.forward(80)
jeffery.end_fill()
jeffery.penup()
'''jeffery.color('black')
jeffery.goto(100, 20)
jeffery.pendown()
for i in range(3):
    jeffery.right(120)
    jeffery.forward(50)
    '''
jeffery.penup()
jeffery.goto(105,10)
jeffery.pendown()
jeffery.color('white')
jeffery.begin_fill()
jeffery.right(35)
jeffery.forward(35)
jeffery.right(135)
jeffery.forward(30)
jeffery.right(45)
jeffery.forward(30)
'''for i in range(3):
    jeffery.right(120)
    jeffery.forward(30)
'''
jeffery.end_fill()

jeffery.color('black')
jeffery.penup()
jeffery.goto(180,180)
jeffery.pendown()
jeffery.write("Matthew Flyr", font=("Comic Sans MS", 23, "italic"))
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing