#
# Code by Alexander Pruss and under the MIT license
#

from mineturtle import *

t = Turtle()
t.pendelay(0)
radius = 20
circumference = 2 * radius * pi
t.penwidth(1)
t.penblock(Block(1))
t.angles()
for j in range(36):
    for i in range(90):
        t.go(circumference/90.)
        t.up(4)
    t.left(10)
# t.penwidth(7)
# t.penblock(block.GOLD_BLOCK)
# for i in range(90):
#     t.go(circumference/90.)
#     t.left(4)
t.penup()
t.back(20)
