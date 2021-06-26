from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z = mc.player.getTilePos()
while Ture:    
    try:
        block = int(input("What is ID numbe?"))
        break
    expet:
      print("Error")
mc.setBlock(x,y,z,block)

