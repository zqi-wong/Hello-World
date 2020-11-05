import turtle
import math

msg = "请输入边长大小n："
n = float(input(msg))

t = turtle.Turtle()
t.pencolor("black")
t.pensize(n/14)  #14为参数
t.fillcolor("yellow")

t.begin_fill()
t.fd(n)
t.left(120)
t.fd(n)
t.left(120)
t.fd(n)
t.end_fill()
t.penup()

h1 = 0.12*n  #参数点的高度
t.goto(n/2,h1)
t.pensize(n/40)  #40为参数
t.fillcolor("black")
t.dot(n/11.5,"black")

h2 = 0.205*n  #参数叹号的高度
t.goto(n/2,h2)
k = 0.31  #参数叹号相对长度
de = 10   #参数叹号张开半角度
l = k*n*math.sin(math.radians(de))
t.pd()
t.begin_fill()
t.right(150+de)
t.fd(n*k)
t.left(de)
t.circle(l,180)
t.left(de)
t.fd(n*k)
t.end_fill()


t.hideturtle()
turtle.done()