# Module for drwaing graphics
import turtle

# creating turtle object 
canvas = turtle.Turtle()

# defining colors for pen
colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']

# create a pen to start drawing
t= turtle.Pen()

# set the speed of turtle to fastest
t.speed(0)

# set background color to black
turtle.bgcolor("white")


for x in range(200):
	t.pencolor(colors[x%6])
	t.width(x/100 + 1) # setting width
	t.forward(x) # moving forward
	t.left(59) # moving left

turtle.done()