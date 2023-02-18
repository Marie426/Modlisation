# Essai Pong game 

import turtle

wn = turtle.Screen() #create a window 
wn.title("Pong?")
wn.bgcolor("black") #backgroung color
wn.setup(width=800, height=600) #change of the size # (0,0) is at the center 
wn.tracer(0) #stop the windown for uptdating to update it manually 

# Score 
score_a = 0
score_b = 0

# Paddle A 
paddle_a = turtle.Turtle() #create a object
paddle_a.speed(0) #speed of animation, not on the screen 
# necessary for the turtle, set the speed to max 
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #initial size = 20pixels 
paddle_a.penup() #avoid the drawing of a line 
paddle_a.goto(-350, 0) #position in the beginning


# Paddle B
paddle_b = turtle.Turtle() #create a object
paddle_b.speed(0) #speed of animation, not on the screen 
# necessary for the turtle, set the speed to max 
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #initial size = 20pixels 
paddle_b.penup() #avoid the drawing of a line 
paddle_b.goto(350, 0) #position in the beginning

# Ball 
ball = turtle.Turtle() #create a object
ball.speed(0) #speed of animation, not on the screen 
# necessary for the turtle, set the speed to max 
ball.shape("square")
ball.color("white") 
ball.penup() #avoid the drawing of a line 
ball.goto(0, 0) #position in the beginning

# range of movement of the ball 
ball.dx = 0.2 # variation on the x axis 
ball.dy = 0.2 

# Pen -> to write the score on the screen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() #ifnot see a line moving 
pen.hideturtle() #don't want to see it but only the score 
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions 
def paddle_a_up():
    y = paddle_a.ycor() #return the y coordinate -> asign to a value y
    y += 20 # to go up, add 20 to the y coord
    paddle_a.sety(y) #assign the new position

def paddle_a_down():
    y = paddle_a.ycor() #return the y coordinate -> asign to a value y
    y -= 20 # to go down, substracte 20 to the y coord
    paddle_a.sety(y) #assign the new position

def paddle_b_up():
    y = paddle_b.ycor() #return the y coordinate -> asign to a value y
    y += 20 # to go up, add 20 to the y coord
    paddle_b.sety(y) #assign the new position

def paddle_b_down():
    y = paddle_b.ycor() #return the y coordinate -> asign to a value y
    y -= 20 # to go down, substracte 20 to the y coord
    paddle_b.sety(y) #assign the new position

# Keyboard binding -> will call the functions 
wn.listen() #listen for keyboard input 
wn.onkeypress(paddle_a_up, "w") #call the function when w is press
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up") #call the function when w is press
wn.onkeypress(paddle_b_down, "Down") #Up and Down = Arrow on keyboard

# Main game loop -> necessary for all game 
while True: 
    wn.update() #everytime it run it update the screen 

    # Move the ball 
    ball.setx(ball.xcor() + ball.dx) #current x coordinate + change
    ball.sety(ball.ycor() + ball.dy)

    # Border checking (bounce at end of (length) window)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *=-1 #reverse the direction of the ball 

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1
    
    # Going over the x axis = lost of the set 
    if ball.xcor() > 390: #pass the paddle and off the screen 
        ball.goto(0,0)
        ball.dx *=-1
        score_a += 1 
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        # format method on the string -> put score a in the first 

    if ball.xcor() < -390: #pass the paddle and off the screen 
        ball.goto(0,0)
        ball.dx *=-1
        score_b += 1
        pen.clear() # for the turtle model  
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions 
    if (ball.xcor() > 340 and ball.xcor()<350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *=-1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *=-1
