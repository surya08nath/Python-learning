import turtle as t
import random as ra
import colorgram

colors=colorgram.extract('image.jpg',40)
set_clr=[]
t.colormode(255)
for i in colors:
    r=i.rgb.r
    g=i.rgb.g
    b=i.rgb.b
    new_clr=(r,g,b)
    set_clr.append(new_clr)

number=100
t.penup()
t.speed("fastest")
t.hideturtle()
t.setheading(220)
t.forward(300)
t.setheading(0)
for i in range(1,number+1):
    
    t.dot(20,ra.choice(set_clr))
    t.forward(50)
    if i%10==0:
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(500)
        t.setheading(0)

screen=t.Screen()
screen.exitonclick()

