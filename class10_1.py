from mcpi.minecraft import Minecraft as mcs
import random
mc = mcs.create()
x,y,z=mc.player.getPos()
for i in range(30):
    num = random.randint(1,6)
    if num == 1:
        mc.setBlocks(x,y,z,x+6,y,z,2)
        x=x+6
    elif num == 2:
        mc.setBlocks(x,y,z,x-6,y,z,2)
        x=x-6
    elif num == 3:
        mc.setBlocks(x,y,z,x,y,z+6,2)
        z=z+6
    elif num == 4:
        mc.setBlocks(x,y,z,x,y,z-6,2)
        z=z-6
    elif num == 5:
        mc.setBlocks(x,y,z,x,y+5,z,2)
        y=y+5
    elif num == 6:
        mc.setBlocks(x,y,z,x,y-5,z,2)
        y=y-5