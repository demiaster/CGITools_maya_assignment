# importing Python Maya commands
import maya.cmds as cmds


def get_center(face, polygon):
    """ Calculate center coordinates of the given face

    - **parameters**, **types**, **return** and **return types**::

         :param face: is the name of the Maya face object
         :type face: string
         :param polygon: is the name of the Maya object the given face belongs to
         :type polygon: string
         :return: return list with coordinates of the center of the given face
         :rtype: list of float

    """
    # selecting given face
    cmds.select(face)

    # storing all the vertexes surrounding the face
    raw_vertexes = cmds.polyInfo(faceToVertex=True)
    # parsing horrible polyInfo output to have a normal array
    list_vertexes = map(lambda x: int(x), "".join(raw_vertexes).split(':')[1].split())

    # initialising accumulators
    x_tot = 0.0
    z_tot = 0.0

    # calculate the total x, z sum for neighbour vertexes
    for j in range(0, len(list_vertexes)):
        # storing coordinates of current point
        current_point = str(polygon) + '.vtx[' + str(list_vertexes[j]) + ']'
        point_coordinates = cmds.pointPosition(current_point, w=True)
        # sum all the x coordinates
        x_tot += point_coordinates[0]
        # sum all the z coordinates
        z_tot += point_coordinates[2]

    # calculate the weighted average for x, z coordinates
    x_center = x_tot / float(len(list_vertexes))
    y_center = cmds.pointPosition(str(polygon) + '.vtx[' + str(list_vertexes[0]) + ']', w=True)[1]
    z_center = z_tot / float(len(list_vertexes))

    return [x_center, y_center, z_center]


# creating a sphere and storing its name
cmds.polySphere(name='dome_right', radius=1, subdivisionsX=10, subdivisionsY=10)
dome = 'dome_right'

# get the selection of the object
listFaces = []

# loop for each face...
for i in xrange(89, 80, -1):
    listFaces.append(dome + '.f[' + str(i) + ']')

for i in xrange(19, 0, -1):
    listFaces.append(dome + '.f[' + str(i) + ']')
listFaces = cmds.ls(listFaces, fl=True)
cmds.delete(listFaces)
cmds.delete(dome + '.f[61]')
cmds.delete(dome + '.f[0]')

# fill bottom hole
cmds.select(dome + '.e[1]', r=True)
cmds.polyCloseBorder()

# rotate edge loop
for i in range(1, 7):
    angle = 36 * i
    edgeLoop = dome + '.e[' + str(i) + '0:' + str(i) + '9]'
    cmds.rotate(0, str(angle) + 'deg', 0, str(edgeLoop))

# scaling edge loops
scaleValue = 1
step = 0.2
for i in range(4, 7):
    edgeLoop = dome + '.e[' + str(i) + '0:' + str(i) + '9]'
    scaleValue -= step
    # scale only x, z value so that they remain on the same height
    cmds.scale(scaleValue, 1, scaleValue, str(edgeLoop))
    step += 0.1

# moving tip of the dome
cmds.polyMoveVertex(dome + '.vtx[70]', ty=0.2)

# scaling whole dome to fit the tower
scale = 0.52
cmds.scale(scale, scale, scale, str(dome))

# storing name of the tower we are working on
towerName = 'turret_wall'

# moving dome pivot to center of bottom face
newPivotPos = get_center(dome + '.f[70]', dome)
cmds.move(newPivotPos[0], newPivotPos[1], newPivotPos[2], dome + '.rotatePivot', a=True)

# storing center for top tower face
targetPosition = get_center(towerName + '.f[7]', towerName)

cmds.move(targetPosition[0], targetPosition[1], targetPosition[2], dome, rpr=True, a=True)
print "final pivot position : " + str(cmds.pointPosition(dome + '.rotatePivot'))
# TODO: create copy
# TODO: move copy to its right position
# TODO: group right_dome
# TODO: group left_dome

# clean the history
cmds.delete(dome, ch=1)
# TODO: clean history for both of them
