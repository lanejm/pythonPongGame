import turtle

#game screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("green")
screen.setup(width = 800, height = 600)
screen.tracer(0)

def drawField():
	draw = turtle.Turtle()
	draw.penup()
	draw.speed(0)
	draw.color('white')
	draw.hideturtle()
	draw.goto(-390,295)
	draw.pendown()
	for i in range(2):
		draw.forward(770)
		draw.right(90)
		draw.forward(580)
		draw.right(90)
	draw.goto(0,295)
	draw.right(90)
	draw.goto(0,-285)
	draw.penup()
	draw.goto(-50,0)
	draw.pendown()
	draw.circle(50)

drawField()

#score counters
score1 = 0
score2 = 0

#left paddle
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("black")
paddle1.shapesize(stretch_wid=5, stretch_len=1) 
paddle1.penup()
paddle1.goto(-350, 0)

#right paddle
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("black")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(500)
ball.shape("circle")
ball.color("White")
ball.penup()
ball.goto(0, 0)
ball.dx = -2
ball.dy = 2

#game rules
game_over = False
winner = None
points = {
    "player1": 0,
    "player2": 0
}
game_rules = {
    "max_points": 3,
    "ball_speed": 3
}


#score display
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))

#player controls
def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)


def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)

# Set up keyboard bindings
screen.listen()
screen.onkeypress(paddle1_up, "w")
screen.onkeypress(paddle1_down, "s")
screen.onkeypress(paddle2_up, "Up")
screen.onkeypress(paddle2_down, "Down")

#main game loop
score_display.goto(0, 0)
score_display.write("WELCOME", align = "center", font = ("Courier", 29, "bold"))
score_display.clear()
score_display.goto(0, 260)
while True:
    screen.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for ball collision with paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    # Check for ball going off screen
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        points["player1"] += 1
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        points["player2"] += 1

    # Check for ball colliding with top or bottom of screen
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Update score display
    score_display.clear()
    score_display.write("Player 1: {}  Player 2: {}".format(points["player1"], points["player2"]), align="center", font=("Arial", 24, "normal"))

