import turtle

#ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")

#game screen
turtle.setup(400, 300)
#background color
turtle.bgcolor("black")

#left paddle
paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.color("red")
paddle1.shapesize(stretch_wid=5, stretch_len=1) 
paddle1.penup()
paddle1.goto(-350, 0)
paddle1.dy = 0

#right paddle
