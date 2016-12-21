# importing Python Maya commands
import maya.cmds as cmds

# creating a sphere and storing its name
cmds.polySphere(name='dome_right', radius=1, subdivisionsX=10, subdivisionsY=10)
name = 'dome_right'

# get the selection of the object
listFaces = []
# loop for each face...

for i in xrange(89, 80, -1):
    listFaces.append(name + '.f[' + str(i) + ']')

for i in xrange(19, 0, -1):
    listFaces.append(name + '.f[' + str(i) + ']')
listFaces = cmds.ls(listFaces, fl=True)
cmds.delete(listFaces)
cmds.delete(name + '.f[61]')
cmds.delete(name + '.f[0]')

# fill bottom hole
cmds.select(name + '.e[1]', r=True)
cmds.polyCloseBorder()

# rotate edgeloop
for i in range(1, 7):
    angle = 36 * i
    edgeLoop = name + '.e[' + str(i) + '0:' + str(i) + '9]'
    cmds.rotate(0, str(angle) + 'deg', 0, str(edgeLoop))

# scaling edgeloops
scaleValue = 1
step = 0.2
for i in range(4, 7):
    edgeLoop = name + '.e[' + str(i) + '0:' + str(i) + '9]'
    scaleValue -= step
    # scale only x, z value so that they remain on the same height
    cmds.scale(scaleValue, 1, scaleValue, str(edgeLoop))
    step += 0.1

# moving tip of the dome
cmds.polyMoveVertex(name + '.vtx[70]', ty=0.2)

# scaling whole dome to fit the tower
scale = 0.52
cmds.scale(scale, scale, scale, str(name))

# retrieving position of top of the left tower
towerName = 'turret_wall'
leftTop = cmds.pointPosition(towerName + '.pt[214]', w=True)

# moving dome pivot to one of its bottom points
newPivotPos = cmds.pointPosition(name + '.pt[6]', w=True)
cmds.move(newPivotPos[0], newPivotPos[1], newPivotPos[2], name + '.translatePivot', a=True)
#print str(cmds.pointPosition(name + '.pt[214]', w=True))
cmds.move(leftTop[0], leftTop[1], leftTop[2], name)
# clean the history
cmds.delete(name, ch=1)
