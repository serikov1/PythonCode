'''
def right_justify(word):
    print(' ' * (70 - len(word)) + word)


right_justify('monty')


def print_spam(words):
    print(words)


def do_twice(foo, value):
    foo(value)
    foo(value)


do_twice(print_spam, 'now')


def print_tabular(str, col):
    print('+ - - - ' * col, '+')
    print('|       ' * col, '|')


print_tabular(2, 2)
'''
import math
import turtle


def squre(t, lenght):
    for i in range(4):
        t.fd(lenght)
        t.lt(90)
    turtle.mainloop()


tut = turtle.Turtle()


def polyline(t, lenght, n, angle, num):
    for i in range(n):
        if num == 1:
            t.fd(lenght)
        else:
            t.bk(lenght)
        if num == 1:
            t.lt(angle)
        else:
            t.rt(-angle)


def polygon(t, lenght, n, num):
    angle = 360/n
    polyline(t, lenght, n, angle, num)


def arc(t, r, angle, num):
    arc_length = 2 * math.pi * r * abs(angle)/360
    n = int(arc_length / 4) + 3
    step_angle = float(angle) / n
    step_length = arc_length / n
    t.rt(step_angle/2)
    polyline(t, step_length, n, step_angle, num)
    t.lt(step_angle/2)


t = turtle.Turtle()

for i in range(7):
    arc(t, 100, 60, 1)
    t.rt(60)
    arc(t, 100, 60, 0)

#
# def flower(t, n, r, angle):
#     arc(t, r, angle)
#
#
# flower(t, )


turtle.mainloop()