#!/usr/bin/python
# -*- coding: utf-8 -*-


# from  turtle import  *
#
# # width(4)
# #
# # forward(200)
# # right(90)
# #
# # pencolor('cyan')
# # forward(100)
# # right(90)
# #
# # pencolor('yellow')
# # forward(200)
# # right(90)
# #
# # pencolor('brown')
# # forward(100)
# # right(90)
# #
# # done()
#
#
# # 设置色彩模式是RGB:
# colormode(255)
#
# lt(90)
#
# lv = 14
# l = 120
# s = 45
#
# width(lv)
#
# # 初始化RGB颜色:
# r = 0
# g = 0
# b = 0
# pencolor(r, g, b)
#
# penup()
# bk(l)
# pendown()
# fd(l)
#
# def draw_tree(l, level):
#     global r, g, b
#     # save the current pen width
#     w = width()
#
#     # narrow the pen width
#     width(w * 3.0 / 4.0)
#     # set color:
#     r = r + 1
#     g = g + 2
#     b = b + 3
#     pencolor(r % 200, g % 200, b % 200)
#
#     l = 3.0 / 4.0 * l
#
#     lt(s)
#     fd(l)
#
#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     rt(2 * s)
#     fd(l)
#
#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     lt(s)
#
#     # restore the previous pen width
#     width(w)
#
# speed("fastest")
#
# draw_tree(l, 4)
#
# done()

import turtle as tt
from random import randint
tt.TurtleScreen._RUNNING = True
tt.speed(0)  # 绘图速度为最快
tt.bgcolor("black")  # 背景色为黑色
tt.setpos(-25, 25)  # 改变初始位置，这可以让图案居中
tt.colormode(255)  # 颜色模式为真彩色
cnt = 0
while cnt < 10000:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tt.pencolor(r, g, b)  # 画笔颜色每次随机
    tt.forward(50 + cnt)
    tt.right(91)
    cnt += 1
tt.done()
