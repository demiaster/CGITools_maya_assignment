#importing Python Maya commands
import maya.cmds as cmds

#creating a sphere and storing its name
cmds.polySphere(name = 'dome_right', radius = 1, subdivisionsX = 10, subdivisionsY = 10)
name = 'dome_right'

