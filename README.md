#Dome.py

##The Purpose

The script is intented to create the dome shape procedurally and to place the object in the correct position within the scene. It also performs a final cleanup of the manipulations that occurred in order to keep the outline and maya history clean and readable.

Since the dome shape present a spiral pattern on its surface, a script can easily produce that effect and can avoid tedious work of having to manipulate by hand each horizontal edge loop.

The script is only run once to produce the two dome in the scene. On top of that other operation has been manually added to the domes, such as applying texture and colours.

The script is located in the `script` folder of the project.

##Main Tasks

* Create initial geometry for the dome

* Manipulate initial geometry to get the final dome shape

* Evaluate goal position for dome to be moved to

* Move dome to goal position

###Modules

In order to accomplish the aforementioned tasks, two main modules have been created.

####Get Center

`get_center(face, polygon)` calculate the center of a given polygon shape using the weighted average formula.
This module is used both to evaluate the new position for the dome rotation and scale pivot as well as for the final position for the dome to be placed to.

* retrieve name of vertexes that compose the polygon using the `polyInfo` maya command

* parse polyInfo output using a lambda function and store the vertexes name in a list

* calculate the sum of all the x and z vertexes coordinates using a simple for loop

* evaluate the the center applying the weighted average formula for both x and z coordinate.

* return the center coordinate as a list of three value (x, y, z)


####Model Dome

`model_dome(_dome)` is concerned with the manipulation of a simple polySphere to get the dome shape. It mainly works on faces and edge loops.

* create sphere with a given name, 10 subdivisions in the x (parallels) and 10 subdivisions in the y (meridians).

* remove the bottom three rows of faces

* create a new face to fill the bottom hole

* rotate one parallel at the time by selecting its relative edge loopto produce the spiral pattern of the dome surface. This step heavily relies on string manipulation to select the correct edge loop and is achieved though a simple for loop.

* scale edge loops to achieve the external silhouette. Each of them is scaled only in the xz plane, so that the y coordinate remains the same. Each parallel is incrementally shrunk compared to the previous one.

* `get_center(face, polygon)` is invoked to calculate the center of the bottom face. The pivot of the dome is then moved to the center of the bottom face.

## Information Flow

The name of the dome is first chosen. `model_dome` is then invoked to create the dome shape. `get_center` is then used to calculate the center of the top of the tower that is used as final position for the dome. The dome is moved to the top of the tower, added to the correct group in the outline of the scene. As final task, the script deletes all the manipulation history. These operation are run twice, once for each of the two domes in the scene.