# coding=utf-8

from mcpi.minecraft import Minecraft
from mcpi.block import *
import misaki_font

mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x + 10
y = pos.y
z = pos.z + 10

font = misaki_font.fonts['あ']
print font

for i in range(8):
    for j in range(8):
        dot = font[j * 8 + i]
        print dot
        if dot == '1':
            print 'set dot'
            mc.setBlock(x + 1, y + j, z, STONE)


