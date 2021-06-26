from mcpi.minecraft import Minecraft as mcs
import time
mc = mcs.create()
x,y,z, = mc.player.getTilePos()
i = 0
while i<3:
    time.sleep(5)
    y = y+1
    mc.player.setTilePos(x,y,z)
    i = i+1

