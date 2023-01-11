import turtle
import random
import time

pencere = turtle.Screen()
pencere.title("Dinosaur Game")
pencere.bgcolor("black")
pencere.setup(height=500, width=800)
pencere.bgpic("back.gif")
pencere.tracer(0)

pencere.register_shape("dino.gif")
pencere.register_shape("cactus.gif")

dino = turtle.Turtle()
dino.speed(0)
dino.shape("dino.gif")
dino.color("green")
dino.penup()
dino.dy = 0
dino.dx = 0
dino.state = "ready"
dino.height = 100
dino.width = 120
dino.goto(-200, -50)

gravity = -0.5

kaktus = turtle.Turtle()
kaktus.speed(0)
kaktus.shape("cactus.gif")
kaktus.color("red")
kaktus.penup()
kaktus.dx = -5
kaktus.height = 60
kaktus.width = 28
kaktus.goto(200, -70)


def jump():
    if dino.state == "ready":
        dino.dy = 12
        dino.state = "jumping"


pencere.listen()
pencere.onkeypress(jump, "space")

while True:
    time.sleep(0.01)
    if dino.ycor() < -50:
        dino.sety(-50)
        dino.dy = 0
        dino.state = "ready"

    if dino.ycor() != -50 and dino.state == "jumping":
        dino.dy += gravity

    y = dino.ycor()
    y += dino.dy
    dino.sety(y)
    x = kaktus.xcor()
    x += kaktus.dx
    kaktus.setx(x)

    if kaktus.xcor() < -400:
        x = random.randint(400, 600)
        kaktus.setx(x)
        kaktus.dx *= 1.05
    if kaktus.distance(dino) < 30:
        print('GAME OVER')

    pencere.update()