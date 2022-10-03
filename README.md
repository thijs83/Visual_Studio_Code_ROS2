# Automation in VS Code with ROS2

This repository contains two important python scripts that automate your ROS2 workflow in the Visual Studio Code IDE. Below is a step by step guide on how to setup the VS environment and work with this environment. 

Note: The assumption is made that you know how ROS2 works and that it is installed. Also Visual Studio Code should be installed.


## Contents:
* [1. Visual Studio Code Extensions](#1-visual-studio-code-extensions)
* [2. Setup of the VS workspace](#2-setup-of-the-vs-workspace)
* [3. Automation of the VS workspace](#3-automation-of-the-vs-workspace)

## 1) Visual Studio Code Extensions

The following extensions are recommended:
- C/C++ (C/C++ IntelliSense, debugging, and code browsing.)
- Python (IntelliSense (Pylance), Linting, Debugging (multi-threaded, remote), Jupyter Notebooks, code formatting, refactoring, unit tests, and more.)
- ROS (Develop Robot Operating System (ROS) with Visual Studio Code.)
- CMake (CMake langage support for Visual Studio Code)
- CMake Tools (Extended CMake support in Visual Studio Code)

## 2) Setup of the VS Workspace

First, a ROS workspace needs to be created, which eventually also will be the VS code workspace.
```bash
 mkdir ~/colcon_ws
 cd ~/colcon_ws
 mkdir src
 mkdir .vscode
 colcon build
```

Note: Using colcon build is essential to set up the ROS workspace for VS to know that it is a ROS2 workspace

Now we need the two files and too showcase the example, there are two beginner ROS packages included. These need to be moved to the src folder. If you have other packages then remove the ones included in this repository.
```bash
 git clone https://github.com/thijs83/Visual_Studio_Code_ROS2.git
 mv -v ~/colcon_ws/Visual_Studio_Code_ROS2/cpp_pubsub/ ~/colcon_ws/src
 mv -v ~/colcon_ws/Visual_Studio_Code_ROS2/py_pubsub/ ~/colcon_ws/src
 mv ~/colcon_ws/Visual_Studio_Code_ROS2/initialise_VSDebug.py ~/colcon_ws/
 mv ~/colcon_ws/Visual_Studio_Code_ROS2/update_VSDebug.py ~/colcon_ws/
```

Now we run the first python file to setup all the .json files in the .vscode folder. These are used by VS code to setup the environment and determine the debug settings. This script only has to run one time.
```bash
 python3 initialise_VSDebug.py
```

Next, we need to open Visual Studio Code and open the folder colcon_ws. Now go to File -> Save Workspace As and press save. The final structure of the ROS2 and VS workspace will look like:
```
~/colcon_ws/
    .vscode/
        c_cpp_properties.json
        extensions.json
        settings.json
        tasks.json
    build/
    install/
    log/
    src/
        cpp_pubsub/
        py_pubsub/
    initialise_VSDebug.py
    update_VSDebug.py
    colcon_ws.code-workspace
```

Below an image of how it will look like in Visual studio code.

TO DO: image

## 3) Automation of the VS workspace

Now everything is ready we can start automating using the second python script. To make it easy and not having to run the python script everytime, a task is made that can be run from the Command Palette. This task automatically runs colcon build (with debug settings to ON) and then runs the python script to include all ROS2 exutables to the debug section.
```
To do this: press Ctrl+Shift+P -->> Tasks: Run Task -->> ROS: update Build & Debug
```

TO DO: images next to eachother


Now in the folder .vscode another file will be included named launch.json automatically. Everytime you alter files or delete/add executables, you have to run the above command. (This command runs colcon build automatically and then updates the launch.json, so all executables are up to date with your code)

We can now go to the Run and Debug section (Ctrl+Shift+D) and all the ROS2 nodes are added to the drop-down menu visualized in the image below. 

TO DO: Image

The nodes are first described by if it is made as a python or c++ script, followed by the node name and then the package it originates from.
Lets start two nodes that talk to eachother, one publishes a counter and the other subscribes to the same counter. 

You could start a ROS2 system status that shows all connections. This is done by following the commands:
```
Press Ctrl+Shift+P -->> ROS: Start
```
Now start c++: cpp_listener_Node - PKG:cpp_pubsub by selecting this node from the drop down menu and then press the green play button to the left. This starts the subscriber node. Now do the same for the c++: cpp_talker_Node - PKG:cpp_pubsub. Now the two nodes are running and talking to eachother. The terminal of the talker is visualized but you can switch to the subscriber node terminal using the bottom-left pannel and press on the wanted terminal as shown below.




To stop the nodes, the terminals can be closed or the stop button can be pressed for the node. This is visualized in the image below.



Now you know how to start the nodes and stop them. The next section shows how to debug the code

## 5) Debugging your code in VS with ROS

The next step to debugging is very easy. Let's take the two nodes from previous section and open the scripts next to eachother and in both scripts set a Breakpoint as visualized in the image below.


Now run both scripts as done in previous section and see how the code stops at the break point set in the publisher. The debug player should be put on the talker node, as shown in the figure below. Now press a few times F5 or the continue button in the debug player to see what happens. After a few times pressing, a yellow bar should appear in the subscriber file and the breakpoint is hit (see the figure below). Now in the dropdown menu in the debug player, select the subscriber node and the corresponding variables are loaded. Again press F5 to let the code continue. 


## 4) Hints to increase development speed

TO DO: add shortcut to ROS: update Build & Debug

TO DO: Multiple windows and cloning the workspace


