from turtle import *
import colorsys
bgcolor("black") # type: ignore
tracer (500) # type: ignore

def draw():
    h = 0
    for i in range(100):
        c = colorsys.hsv_to_rgb(h,1,1)
        h += 0.1
        up() # type: ignore
        goto(0,0) # type: ignore
        down() # type: ignore
        color("black") # type: ignore
        fillcolor (c) # type: ignore
        begin_fill() # type: ignore
        rt (98) # type: ignore
        circle(i, 12) # type: ignore
        fd (290) # type: ignore
        fd(i) # type: ignore
        lt (12) # type: ignore
        for j in range(129):
            fd(i) # type: ignore
            circle(j, 299, steps=2) # type: ignore
        end_fill() # type: ignore
draw()  
done() # type: ignore