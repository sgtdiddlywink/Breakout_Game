"""This script is my own take on the breakout game. Lot's of areas for improvement but it's a start."""
import random
# Import Modules
from turtle import Turtle, Screen
import time

# CONSTANTS
COLOR_LIST = ["blue", "yellow", "orange", "red", "green", "white"]


# --------------------------------------------------------Classes------------------------------------------------------#
# Create paddle class
class Paddle(Turtle):

    def __init__(self):  # Set initializer for all Paddle objects.
        super().__init__()  # Take attributes from Turtle class
        self.shape(name="square")  # Set the initial shape of the paddle
        self.shapesize(stretch_wid=.5, stretch_len=3)  # Stretch the paddle the appropriate shape
        self.color("white")  # Set the paddle color.
        self.penup()  # Put the pen up on the turtle.
        self.goto(x=0, y=-275)  # Set the initial position of the paddle.

    # Create a method for moving the paddle right
    def go_right(self):
        new_x = self.xcor() + 20  # Variable determines current x-coordinate and adds 20 movement to it.
        self.goto(x=new_x, y=self.ycor())  # Utilize turtle function goto to move the paddle "new_x" distance.

    # Create a method for moving the paddle left
    def go_left(self):
        new_x = self.xcor() - 20  # Variable determines current x-coordinate and subtracts 20 movement to it.
        self.goto(x=new_x, y=self.ycor())  # Utilize turtle function goto to move the paddle "new_x" distance.


class Ball(Turtle):

    def __init__(self):  # Set initializer for all ball objects
        super().__init__()  # Inherit attributes from the Turtle Class
        self.shape(name="circle")  # Set the shape of the object
        self.penup()  # Lift the pen from the object to avoid drawing lines
        self.color("white")  # Set the color of the ball
        self.speed(speed="fastest")  # This is a turtle method for determining the speed of the ball
        # Set the initial start of the ball centered on x-axis and right above paddle
        self.goto(x=0, y=random.choice(range(-100, -50)))
        x_direction_start = random.choice([1, -1])
        random_heading = random.choice(range(8, 10))
        self.x_move = random_heading * x_direction_start  # This will randomize whether the ball goes left or right
        self.y_move = random_heading

    # Method to move the ball
    def move(self):
        new_x = self.xcor() + self.x_move  # Takes the initial location of the ball and adds the new distance to it
        new_y = self.ycor() + self.y_move  # Takes the initial location of the ball and adds the new distance to it
        self.goto(x=new_x, y=new_y)  # Function to move the ball to it's new location

    # Method for rebounding the ball off the top of the screen
    def bounce_y(self):
        self.y_move *= -1  # It will change the sign of the variable and in turn cause it to go the opposite direction

    # Method for rebounding the ball off the left and right side of the screen
    def bounce_x(self):
        self.x_move *= -1  # Will change the sign of the variable and in turn cause it to go the opposite direction

    # Method for rebounding the ball off the paddle
    def bounce_paddle(self):
        self.y_move *= -1  # Will change the sign of the variable and in turn cause it to go the opposite direction

    # Method for rebounding the ball off the blocks
    def bounce_block(self):
        self.y_move *= -1  # Have the ball change direction in the y and x axis
        self.x_move *= -1

    # Method to create new ball
    def refresh(self):
        self.goto(x=0, y=random.choice(range(-100, -50)))  # Send the ball back to original starting position
        self.x_move *= random.choice([1, -1])  # Choose a random x direction for the ball to start
        self.y_move *= -1  # Send the ball in the positive y direction


# Create Block Class
class Block(Turtle):
    def __init__(self, position, color):  # Set initializer for Block objects
        super().__init__()  # Inherit attributes from Turtle Class
        self.shape(name="square")  # Set shape of the block objects
        # Set color of blocks utilizing random choice of colors
        self.color(color)
        self.shapesize(stretch_wid=2, stretch_len=7.5)  # Stretch the blocks to their appropriate sizes
        self.penup()  # Probably not necessary since the objects don't move
        self.goto(position)  # Set the initial positions for the blocks on the screen


# Create Winner Title Screen
class Winner(Turtle):
    def __init__(self):  # Set initializer for Winner Object
        super().__init__()  # Inherit attributes from Turtle Class
        self.color("white")  # Change color of text to white
        self.penup()  # Raise the penup
        self.goto(0, 0)  # Place in the center of the screen
        # The message to be displayed
        self.write("Winner! Winner! Chicken Dinner!", False, align="center", font=("Arial", 18, "normal"))


# Create window for the game
screen = Screen()  # Set up screen object from the Screen Class
screen.setup(width=800, height=600)  # Set the screen dimensions
screen.bgcolor("black")  # Change screen background color
screen.title(titlestring="Breakout")  # Set the window title

# Turn turtle animation on/off with tracer function
screen.tracer(n=0)  # Tracer turned off when n = 0

# Create a paddle object from the Paddle Class
paddle = Paddle()

# Create ball object from Ball Class
ball = Ball()

# Create blocks objects from the Block Class. There should be a more pythonic way to do this.
# First Row
block_1 = Block(position=(0, 0), color=random.choice(COLOR_LIST))
block_2 = Block(position=(160, 0), color=random.choice(COLOR_LIST))
block_3 = Block(position=(-160, 0), color=random.choice(COLOR_LIST))
block_4 = Block(position=(320, 0), color=random.choice(COLOR_LIST))
block_5 = Block(position=(-320, 0), color=random.choice(COLOR_LIST))
# Second Row
block_6 = Block(position=(0, 50), color=random.choice(COLOR_LIST))
block_7 = Block(position=(160, 50), color=random.choice(COLOR_LIST))
block_8 = Block(position=(-160, 50), color=random.choice(COLOR_LIST))
block_9 = Block(position=(320, 50), color=random.choice(COLOR_LIST))
block_10 = Block(position=(-320, 50), color=random.choice(COLOR_LIST))
# Third Row
block_11 = Block(position=(0, 100), color=random.choice(COLOR_LIST))
block_12 = Block(position=(160, 100), color=random.choice(COLOR_LIST))
block_13 = Block(position=(-160, 100), color=random.choice(COLOR_LIST))
block_14 = Block(position=(320, 100), color=random.choice(COLOR_LIST))
block_15 = Block(position=(-320, 100), color=random.choice(COLOR_LIST))
# Fourth Row
block_16 = Block(position=(0, 150), color=random.choice(COLOR_LIST))
block_17 = Block(position=(160, 150), color=random.choice(COLOR_LIST))
block_18 = Block(position=(-160, 150), color=random.choice(COLOR_LIST))
block_19 = Block(position=(320, 150), color=random.choice(COLOR_LIST))
block_20 = Block(position=(-320, 150), color=random.choice(COLOR_LIST))

# List of all block objects to call up for interaction with for loop
block_list = [
    block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8, block_9, block_10, block_11, block_12,
    block_13, block_14, block_15, block_16, block_17, block_18, block_19, block_20
]

# Tell the screen object to start listening for keystrokes
screen.listen()
# Keys for the screen object to listen to and the functions to bind them to
screen.onkey(paddle.go_left, "Left")  # Use arrow keys on keyboard to make the paddle go left & right
screen.onkey(paddle.go_right, "Right")

ball_time = .1  # Time between screen object refreshes
game_is_on = True  # Boolean to initialize the while loop
while game_is_on:  # While loop to move the initial segments
    time.sleep(ball_time)  # Refresh the screen object
    screen.update()  # Used in conjunction with tracer method when it is turned off. Updates the screen object
    ball.move()  # Call move method on ball object
    # Detect collision with top of the screen object
    if ball.ycor() > 279:
        ball.bounce_y()  # Call bounce method to send the ball back down
    # Detect collision with left and right of screen object
    if ball.xcor() > 379 or ball.xcor() < -379:
        ball.bounce_x()  # Call bounce method to send ball opposite of the wall
    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -250:  # Use distance from other turtle object and wall to bounce
        ball.bounce_paddle()  # Call bounce method to reverse direction of ball
        ball_time *= .95  # Increase ball speed everytime it hits the paddle
    # Detect when the paddle misses the ball
    if ball.ycor() < -300:  # Use bottom of the screen object to display that the ball was missed
        ball.refresh()  # Call the refresh method for the ball to return it to its original position.
        """Look into way to add lives to the player and reduce life count after each miss"""
        ball_time = .1  # Reset the ball speed back to its original speed.
    # Detect when the ball hits a block
    for n in block_list:  # Use for loop to go through block list and determine whether the ball interacts with blocks
        # This isn't a great way to do this. Would be better to have big blocks, multiple turtle objects.
        if ball.distance(n) < 70:
            ball.bounce_block()  # Call method to bounce ball
            n.goto(x=1000, y=1000)  # Instead of clearing the object it moves it offscreen.
            block_list.remove(n)  # Remove the object it encountered from the list.
            if not block_list:  # Checks to see if list is empty which means you won.
                print("Winner! Winner! Chicken Dinner!")  # Prints winner on terminal.
                winner = Winner()  # Call Winner Class to create text object on screen
                time.sleep(5)  # Sleep for 5 seconds before closing the window
                screen.bye()  # Exit from the window
            ball_time *= .95  # Increase the speed of the ball with each block hit

# Exit the screen when it is clicked
screen.exitonclick()
