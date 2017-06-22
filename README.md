# Dome.py

Run `dome.py` to create the dome shape procedurally and to place the object in the correct position within the scene.

The script is located in the `script` folder of the project.

The script does the following:

* it produces two domes inside the scene in a run.
* it places them in the right position.
* it performs a final cleanup of the manipulations that occurred in order to keep the outline and maya history clean and readable.

## Motivation

Since the dome shape presents a spiral pattern on its surface, a script can easily produce that effect and can avoid tedious work of having to manipulate by hand each horizontal edge loop.

## Requirements

Tested on: Maya 2016 (python engine 2.7).

## Execute

* on the top of the window, go to `Windows -> General Editors -> Script Editor`
* click on the `+` button at the middle right side of the Script Editor window
* select Python as scripting language
* on the top left of the Script Editor window, click on `File -> Load Script...`
* choose dome.py from the `script` folder of the project

The code for the script will appear in the script Python tab that you created.

* `Ctrl + a` to highlight all the code
* `Shift + Enter` to run the script

_WARNING_

If you want to run the script again, please make sure to remove the existing domes geometry.

## Examples

![alt text](https://github.com/demiaster/CGITools_maya_assignment/blob/master/images/final_dome.png "Final Shape Dome, perspective")
![alt text](https://github.com/demiaster/CGITools_maya_assignment/blob/master/images/front_view_texture.png "Dome, front view and texture")
![alt text](https://github.com/demiaster/CGITools_maya_assignment/blob/master/images/front_view_wireframe.png "Dome, front view and wireframe")
![alt text](https://github.com/demiaster/CGITools_maya_assignment/blob/master/images/top_view_texture.png "Dome, top view and texture")
![alt text](https://github.com/demiaster/CGITools_maya_assignment/blob/master/images/top_view_wireframe.png "Dome, top view and wireframe")
![alt text](https://github.com/demiaster/CGITools_maya_assignment/blob/master/images/final_scene.png "Final scene, perspective and texture")


