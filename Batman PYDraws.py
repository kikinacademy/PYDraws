import turtle

t = turtle.Turtle()

w = turtle.Screen()
w.bgcolor("navy")
w.title("BATMAN PYDRAW")


t.color("gold", "black")

t.begin_fill()

t.left(90)
t.circle(50, 85)
t.circle(15, 110)
t.right(180)

t.circle(30, 150)
t.right(5)
t.forward(10)

t.right(90)
t.circle(-70, 140)
t.forward(40)
t.right(110)

t.circle(100, 30)
t.circle(30, 100)
t.left(50)
t.forward(50)
t.right(145)

t.forward(30)
t.left(55)
t.forward(10)

t.forward(10)
t.left(55)
t.forward(30)

t.right(145)
t.forward(50)
t.left(50)
t.circle(30, 100)
t.circle(100, 30)

t.right(90)
t.right(20)
t.forward(40)
t.circle(-70, 140)

t.right(90)
t.forward(10)
t.right(5)
t.circle(30, 150)

t.left(180)
t.circle(15, 110)
t.circle(50, 85)

t.end_fill()
turtle.done()
