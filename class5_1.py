from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z = mc.player.getTilePos()
block = input("What is ID numbe?")
#block = int(block)
mc.setBlock(x,y,z,block)