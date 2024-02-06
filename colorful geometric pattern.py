import turtle as t
import colorsys as cs

# Set up the turtle environment
t.tracer(2)
t.bgcolor("black")
t.pensize(2)

# Function to draw the letters of the name
def draw_letter(letter_size, color):
    t.color(color)
    t.circle(letter_size, 180)
    t.forward(letter_size * 2)
    t.left(180)
    t.forward(letter_size)
    t.left(180)

# Function to draw the personalized pattern
def draw_personalized_pattern(name):
    n = len(name)  # Number of letters in the name
    h = 0

    for _ in range(1000):
        for _ in range(4):
            c = cs.hsv_to_rgb(h, 1, 1)
            h += 1 / n
            t.color(c)
            t.circle(49, 90)
            t.forward(100)
            t.left(90)

        t.right(10)

    # Move the turtle to a starting position for the name
    t.penup()
    t.goto(-50 * n / 2, -150)
    t.pendown()

    # Draw the personalized name
    for letter in name:
        draw_letter(25, cs.hsv_to_rgb(h, 1, 1))
        h += 1 / n

# Main execution
draw_personalized_pattern("Luyanda")

# Keep the window open
t.done()
