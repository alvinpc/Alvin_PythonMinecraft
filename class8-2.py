def plantTree():
    mc.setBlock(x+1,y+3,z+1,x-1,y,z-1,35.5)
    mc.setBlock(x,y,z,x,y+4,z,3)
from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z=mc.player.getTilePos()
for i in range(0,3):
    for j in range(0,3):
    plantTree(x+i*5,y,z+j*5,2)
