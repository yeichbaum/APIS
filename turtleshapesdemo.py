import turtle

# opens a window to draw on
window = turtle.Screen()
# makes the window white
window.bgcolor("white")


def draw_square(new_turtle):
    for x in range(0, 4):
        new_turtle.pendown()
        new_turtle.right(90)
        new_turtle.forward(100)


def draw_star(new_turtle):
    for x in range(0, 5):
        new_turtle.pendown()
        new_turtle.right(144)
        new_turtle.forward(30)


def draw_circle(new_turtle):
    for x in range(0, 36):
        new_turtle.pendown()
        new_turtle.right(10)
        new_turtle.circle(50)


def main():
    # create an instance of Turtle
    jane = turtle.Turtle()

    # set values on attributes in the Turtle module
    jane.shape("turtle")
    jane.color("green", "yellow")  # outline color, fill color
    jane.penup()
    jane.setx(150)

    # create another instance of Turtle and set its values
    ginger = turtle.Turtle()
    ginger.shape("classic")
    ginger.color("blue")
    ginger.penup()
    ginger.setx(-150)

    star = turtle.Turtle()
    star.shape("arrow")
    star.color("green")
    star.penup()
    star.setx(50)

    circle = turtle.Turtle()
    circle.shape("arrow")
    circle.color("blue")
    circle.penup()
    circle.setx(0)
    draw_circle(circle)

    draw_star(star)
    turtle.bye()

    # draw one square filled with color with the jane instance
    jane.begin_fill()
    draw_square(jane)
    jane.end_fill()

    for x in range(0, 36):
    # draw offset squares in a loop with the ginger instance
        draw_square(ginger)
        ginger.right(10)

    window.exitonclick()


# The following code will only call the `main` function if we are running *this*
# file from the command line. The main function won't be called if we import
# this file.
# Want to learn more about if __name__ == '__main__':?
# Check out:
# http://stackoverflow.com/a/20158605 and/or
# https://www.youtube.com/watch?v=sugvnHA7ElY
if __name__ == '__main__':
    main()
