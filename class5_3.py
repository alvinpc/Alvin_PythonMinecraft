from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
username = input("what is your name?")
message = input("what is your message?")
mc.postToChat("<"+unername+">"+message)
