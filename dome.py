#importing Python Maya commands
import maya.cmds as cmds

#creating a sphere and storing its name
cmds.polySphere(name = 'dome_right', radius = 1, subdivisionsX = 10, subdivisionsY = 10)
name = 'dome_right'

# get the selection of the object - you can do some error checking, if not polygon or if component selection...
listFaces = []
#    loop for each face...

for i in xrange(89, 80, -1):
    listFaces.append(name + '.f[' + str(i) +']')
        
for i in xrange(19, 0, -1):
    listFaces.append(name + '.f[' + str(i) +']')
listFaces = cmds.ls(listFaces, fl=True)
cmds.delete(listFaces)
cmds.delete(name + '.f[61]')
cmds.delete(name + '.f[0]')

#fill bottom hole
cmds.select( name + '.e[1]', r=True )
cmds.polyCloseBorder()

#    clean the history
cmds.delete(name, ch=1)