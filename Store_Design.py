import turtle

screen = turtle.getscreen()
t = turtle.Turtle()
# Draw out the grid
t.color("red")
StoreWidth = 300
StoreHeight = 300
t.goto(0, 0)
t.goto(StoreWidth, 0)
t.goto(StoreWidth, StoreHeight)
t.goto(0, StoreHeight)
t.goto(0, 0)
t.penup()
t.setpos(StoreWidth / 3, StoreHeight / 3)
t.pendown()
t.goto(StoreWidth / 3, 0)
t.showturtle()
t.goto(StoreWidth / 3, StoreHeight)
t.goto(StoreWidth / 1.5, StoreHeight)
t.goto(StoreWidth / 1.5, 0)
t.penup()
t.goto(0, StoreHeight / 3)
t.pendown()
t.goto(StoreWidth, StoreHeight / 3)
t.goto(StoreWidth, StoreHeight / 1.5)
t.goto(0, StoreHeight / 1.5)
t.penup()


# Draw the text separating the aisles
def writeText(xp, yp, row, column):
    t.color('black')
    t.goto(xp, yp)
    t.write(f"{row}{column}", move=False, font=('Arial', 16, 'normal'))


writeText(StoreWidth/6, StoreHeight - ((StoreHeight / 3) / 2), "A", "1")
writeText(StoreWidth/6,StoreHeight/2 ,"A","2")
writeText(StoreWidth/6,StoreHeight/6, "A","3")

writeText(StoreWidth/2, StoreHeight - ((StoreHeight / 3) / 2),"B", "1")
writeText(StoreWidth/2,StoreHeight/2,"B","2")
writeText(StoreWidth/2, StoreWidth/6,"B","3")

writeText(StoreWidth-(StoreWidth/6), StoreHeight - ((StoreHeight / 3) / 2),"C", "1")
writeText(StoreWidth-(StoreWidth/6),StoreHeight/2,"C","2")
writeText(StoreWidth-(StoreWidth/6), StoreWidth/6,"C","3")

# Fill each individual aisle
t.penup()
t.goto(StoreWidth/3,StoreHeight)
t.color('blue')
t.pendown()
t.goto(StoreWidth/3,0)

t.penup()
t.goto(StoreWidth - (StoreWidth/3),StoreHeight)
t.color('yellow')
t.pendown()
t.goto(StoreWidth - (StoreWidth/3),0)
turtle.Screen().exitonclick()
