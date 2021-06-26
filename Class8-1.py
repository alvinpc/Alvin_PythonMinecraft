from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z=mc.player.getTilePos
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            mc.setBlock(x+1,y+k,z+i,2)
for i in range(0,3):
    mc.setBlock(x,+1,y-i,z+1,2)