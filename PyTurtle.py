import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Sreen().bgcolor('black')
t.speed(8)
n = 70
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h+= 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
for i in range