from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z,=mc.player.getTilePos()
for i in range(10):
    mc.setBlock(x+i,y-1,z+i+j,20)