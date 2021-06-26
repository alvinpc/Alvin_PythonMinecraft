from mcpi.minecraft import Minecraft as mcs
import time
mc = mcs.create()
while True:
    time.sleep(1)
    x,y,z = mc.player.getTilePos()
    mc.postToChat("you are located on x = "+str(x)\
                  +"y = "+str(y)+"z = "+str(z))

