def plantTree(x,y,z):
    mc.setBlocks(x+1,y+5,z+1,x-1,y,z-1,35.5)
    mc.setBlocks(x,y,z,x,y+5,z,3)
from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z=mc.player.getTilePos()
for i in range(10):
    for j in range(10):
        plantTree(x+i*5,y+j*i,z)