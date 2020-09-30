import turtle
import math
import random

# import libdw.sm as sm

# assumes perfectly elastic, head-on collision. all objects of equal mass!

# each turtle obj around 20 pixels
# screen res
screen_height = 800  # screen height
screen_width = 800  # screen width

# setup screen
wn = turtle.Screen()
wn.setup(screen_width, screen_height)
wn.bgcolor('blue')
wn.tracer(0)

# graphics
graphic = turtle.Turtle()  # set graphics as a turtle object
graphic.pensize(5)  # size of trail left by the turtle
graphic.penup()
graphic.speed(0)  # animation speed of turtle; 0 means no animation
graphic.hideturtle()

graphic.write('Please enter your name in your IDE', align="center", font=("Arial", 20, "italic"))
name = input(">>>")
graphic.clear()
graphic.write('         Welcome, \n             ' + name + '\n\n Press G to continue \n\n       Good Luck!', align = "center", font=("Arial", 30, "bold"))

class Game:  # create a class called Border
    def __init__(self, width, height):  # initializer with parameters width and height
        self.width = width  # each instance will have it's width refer to width parameter
        self.height = height  # each instance will have it's height refer to height parameter
        self.state = 'menu'

    def drawBorder(self, graphic):  # create method to draw border of game, takes in graphics (turtle) as arg
        graphic.color('black')
        graphic.goto(-self.width, self.height)
        graphic.pendown()
        graphic.goto(self.width, self.height)
        graphic.goto(self.width, -self.height)
        graphic.goto(-self.width, -self.height)
        graphic.goto(-self.width, self.height)
        graphic.hideturtle()

    def start(self):
        self.state = 'playing'

    def win(self):
        self.state = 'victory'
        graphic.write('YOU DID IT,  ' + name, align="center", font=("Arial", 20, "italic"))


class Characters:  # create a class called Characters
    def __init__(self, xcor, ycor, shape, color, angle, num):  # the attributes that characters will have
        self.xcor = xcor  # name variable same as argument to avoid confusion!
        self.ycor = ycor
        self.shape = shape
        self.color = color
        self.angle = angle
        self.num = num
        self.width = 20
        self.height = 20
        self.xVel = 0  # assign a 'velocity' to every char. initially stationary
        self.yVel = 0
        self.force = 0  # force on char initially 0
        self.state = 'active'

    def drawChar(self, graphic):  # create a method to draw each character using turtle! arg is turtle
        if self.state == 'active' or self.state == 'playing':
            graphic.penup()
            graphic.goto(self.xcor, self.ycor)  # turtle will go to specified coordinates
            graphic.shape(self.shape)  # turtle will take the specified shape
            graphic.color(self.color)
            graphic.setheading(self.angle)
            graphic.stamp()  # turtle will leave a stamp of it's position. w/o this, shape will disappear after 1 loop
            graphic.hideturtle()

    def refresh(self):  # create a method that checks for updated location and displays it
        if self.xcor >= (game.width - 5):
            self.xcor = self.xcor - 25
        if self.xcor <= (-game.width + 5):
            self.xcor = self.xcor + 25
        if self.ycor >= (game.height - 5):
            self.ycor = self.ycor - 25
        if self.ycor <= (-game.height + 5):
            self.ycor = self.ycor + 25
        self.xcor += self.xVel
        self.ycor += self.yVel

    def borderCollide(self):
        if self.xcor >= (game.width - 10) or self.xcor <= (-game.width + 10):
            self.xVel = -self.xVel

        if self.ycor >= (game.height - 10) or self.ycor <= (-game.height + 10):
            self.yVel = -self.yVel

    def charCollide(self, target):
        distBtwn = math.sqrt((self.xcor - target.xcor) ** 2 + (self.ycor - target.ycor) ** 2)
        if distBtwn == 0:
            return False
        if distBtwn < 20:
            return True
        else:
            return False


class Player(Characters):
    def __init__(self, xcor, ycor, shape, color, angle, num):
        super().__init__(xcor, ycor, shape, color, angle, num)
        self.changeAngle = 0

    def turnLeft(self):  # method to turn character left
        self.changeAngle = 10  # positive number turn left
        self.angle += self.changeAngle  # everytime method is called, self.angle increases by self.changeAngle

    def turnRight(self):
        self.changeAngle = -10
        self.angle += self.changeAngle

    def forward(self):  # method to move character forward
        self.state = 'playing'
        self.force += 0.05  # use TOA CAH SOH to resolve force into x and y components
        if self.force >= 1.1:  # set max force on object
            self.force = 1.1

        self.xVel = self.force * math.cos(math.radians(self.angle))
        self.yVel = self.force * math.sin(math.radians(self.angle))

        self.xcor += self.xVel
        self.ycor += self.yVel

    def brake(self):
        self.force -= 0.05  # use TOA CAH SOH to resolve force into x and y components
        if self.force <= 0:  # set max force on object
            self.force = 0

        self.xVel = self.force * math.cos(math.radians(self.angle))
        self.yVel = self.force * math.sin(math.radians(self.angle))

        self.xcor += self.xVel
        self.ycor += self.yVel


class Goal(Characters):
    def __init__(self, xcor, ycor, shape, color, angle, num):
        super().__init__(xcor, ycor, shape, color, angle, num)

    def charCollide(self, target):
        distBtwn = math.sqrt((self.xcor - target.xcor) ** 2 + (self.ycor - target.ycor) ** 2)
        if distBtwn < 20:
            return True
        else:
            return False


# in game
game = Game(300, 300)
player = Player(0, 100, 'triangle', 'green', 90, 1)
ball1 = Characters(random.randint(-290, 290), random.randint(-290, 290), 'circle', 'red', 0, 5)  # loop that can do this?
ball2 = Characters(random.randint(-290, 290), random.randint(-290, 290), 'circle', 'red', 0, 5)
ball3 = Characters(random.randint(-290, 290), random.randint(-290, 290), 'circle', 'red', 0, 5)
ball4 = Characters(random.randint(-290, 290), random.randint(-290, 290), 'circle', 'cyan', 0, 5)
ball5 = Characters(random.randint(-290, 290), random.randint(-290, 290), 'circle', 'cyan', 0, 5)
ball6 = Characters(random.randint(-290, 290), random.randint(-290, 290), 'circle', 'cyan', 0, 5)

objects = [player, ball1, ball2, ball3, ball4, ball5, ball6]
balls = [ball1, ball2, ball3, ball4, ball5, ball6]
avoid = [ball1, ball2, ball3]
goal = [ball4, ball5, ball6]
for ball in balls:
    ball.xVel = random.uniform(0.2, 0.8)  # uniform generates a random float
    ball.yVel = random.uniform(0.2, 0.8)

# keyboard inputs
turtle.listen()  # turtle checks for inputs
turtle.onkeypress(player.forward, 'w')
turtle.onkeypress(player.brake, 's')
turtle.onkeypress(player.turnLeft, 'a')
turtle.onkeypress(player.turnRight, 'd')
turtle.onkeypress(game.start, 'g')
turtle.onkeypress(game.start, 'G')

#main loop
while True:

    if ball4.state == 'inactive' and ball5.state == 'inactive' and ball6.state == 'inactive': #how to do this more efficiently?
        game.win()

    if game.state == 'menu':
        wn.update()

    elif game.state == 'playing':
        graphic.clear()   #clears screen every cycle so no trails
        player.drawChar(graphic)
        game.drawBorder(graphic)
        for obj in objects:
            obj.drawChar(graphic)

        for obj in objects:
            obj.refresh()

        if player.state == 'playing':
            for obj in avoid:
                if player.charCollide(obj):
                    dummyX = obj.xVel
                    obj.xVel = player.xVel
                    player.xVel = dummyX

                    dummyY = obj.yVel
                    obj.yVel = player.yVel
                    player.yVel = dummyY

            for obj in goal:
                if player.charCollide(obj):
                    obj.state = 'inactive'

        for i in range(0, len(balls) - 1):
            if balls[i].charCollide(balls[i + 1]):
                dummyX = balls[i + 1].xVel
                balls[i + 1].xVel = balls[i].xVel
                balls[i].xVel = dummyX

                dummyY = balls[i + 1].yVel
                balls[i + 1].yVel = balls[i].yVel
                balls[i].yVel = dummyY

        for obj in objects:
            obj.borderCollide()

    wn.update()
