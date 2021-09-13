from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x + 10
y = pos.y
z = pos.z + 10

mc.setBlock(x, y, z, STONE)


