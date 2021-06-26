from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z=mc.player.getTilePos()
number=10
renumber = 0
for i in range(10):
    for j in range(3):
        mc.spawnEntity(x,y,z,99)
        renumber = renumber + 1
        mc.postToChat(str(renumber)+"bug") 