from turtle import *
import colorsys
bgcolor('black')
tracer(5)
h = 0
for i in range(1000):
    c = colorsys.hsv_to_rgb(h , 1 , 1)
    color(c)
    begin_fill()
    forward(i)
    left(19)
    backward(i * 0.5)
    circle(i*0.1,100)
    end_fill()
    h += 0.008
done()