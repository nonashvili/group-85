from turtle import *


#we want to paint a house

#step 1:  draw a square
speed(5)
width(7)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#drawing a door


forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)    #height on the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("purple")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# window 1 (left
penup()
left(30)
forward(70)
left(90)
forward(30)
pendown()
color("red")
begin_fill()
forward(20)  
left(90)
forward(50)
left(90)
forward(20)
left(90)
forward(50)
end_fill()

# window 2 (right)
penup()
goto(200,200)
forward(70)
right(90)
forward(30)
pendown()
color("red")
pendown()
begin_fill()
forward(20)  
right(90)
forward(50)
right(90)
forward(20)
right(90)
forward(50)
end_fill()



exitonclick()

