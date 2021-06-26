from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
from random import randint
x,y,z=mc.player.getTilePos()
com = randint(0,16)
print("com =",com)
for i in range(10):
    for j in range(10):
        num = randint(0,16)
        mc.setBlock(x+i,y,z+j,35,num)
while True:
    hits= mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        print("data =",data)
        if data == com:
            mc.postToChat("you win > - <")
            break
        elif data < com:
            mc.postToChat("your anwser < com")
        elif data > com:
            mc.postToChat("your anwser > com")