import turtle as t

# Set background color
t.bgcolor('green')

# Set drawing speed
t.speed(8)

# Set pen width
t.width(4)

# Move turtle to starting position
t.penup()
t.lt(90)
t.fd(100)
t.lt(87)
t.pendown()

# Set base color
t.color('black')

# Begin filling the face
t.begin_fill()

# Draw the outline of the face
t.circle(180, 30)
t.rt(70)
t.fd(30)
t.circle(5, 150)
t.fd(40)
t.circle(-60, 30)
t.fd(10)
t.circle(60, 30)
t.rt(10)
t.fd(40)
t.circle(190, 40)
t.circle(70, 90)
t.circle(190, 40)
t.fd(40)
t.rt(10)
t.circle(60, 30)
t.fd(10)
t.circle(-60, 30)
t.fd(40)
t.circle(5, 150)
t.fd(30)
t.rt(70)
t.circle(180, 30)

# End filling the face
t.end_fill()

# Add more detailing to the face
t.color('purple')

# Draw highlights
t.rt(5)
t.circle(180, 25)
t.circle(15, 75)
t.fd(40)
t.circle(15, 55)
t.fd(60)
t.rt(70)
t.fd(10)
t.rt(45)
t.fd(10)
t.rt(85)
t.circle(80, 50)
t.lt(45)
t.fd(10)
t.lt(80)
t.fd(30)
t.circle(40, 50)
t.fd(10)
t.rt(60)
t.fd(30)
t.lt(100)
t.circle(-37, 80)
t.lt(100)
t.fd(30)
t.rt(60)
t.fd(10)
t.circle(40, 50)
t.fd(30)
t.lt(80)
t.fd(10)
t.lt(45)
t.circle(80, 50)
t.rt(85)
t.fd(10)
t.rt(45)
t.fd(10)
t.rt(70)
t.fd(60)
t.circle(15, 55)
t.fd(40)
t.circle(15, 75)
t.circle(180, 30)

# Draw ears
t.penup()
t.goto(-106, -50)
t.pendown()
t.lt(105)
t.circle(90, 40)
t.rt(30)
t.fd(40)
t.rt(60)
t.circle(90, 20)

t.penup()
t.goto(106, -50)
t.pendown()
t.rt(12)
t.circle(-90, 40)
t.lt(30)
t.fd(40)
t.lt(60)
t.circle(-90, 20)

# Add more details to the face
t.penup()
t.goto(-30, -35)
t.width(1)
t.rt(65)
t.pendown()

# Draw nose
t.begin_fill()
t.circle(-37, 90)
t.rt(115)
t.fd(25)
t.circle(-15, 38)
t.fd(20)
t.end_fill()

t.penup()
t.goto(30, -35)
t.pendown()

# Draw nose
t.begin_fill()
t.circle(37, 90)
t.lt(115)
t.fd(25)
t.circle(15, 38)
t.fd(20)
t.end_fill()

# Hide turtle
t.hideturtle()
t.penup()
t.goto(0, 200)
t.color("orange")
t.write("PANTHER", font=("Times New Roman", 26, "bold","italic"),)

# Finish drawing
t.done()
