#!/usr/bin/env python3

import json
from pathlib import Path
import os
import sys
import glob

# Retrieve the workspace folder
workspace_folder = str(Path().absolute())

# Find all packages and check if there exists atleast one
package_names = [f for f in os.listdir(workspace_folder+"/src") if os.path.isdir(os.path.join(workspace_folder+"/src",f))]

if not package_names:
    print("There are no packages and thus nothing is build")
    sys.exit(1)

# Check if initial build is done
try:
    test = os.listdir(workspace_folder+"/install")

    if not test:
        print("First build the envirnment, before calling this script")
        sys.exit(1)
except:
    print("First build the envirnment, before calling this script")
    sys.exit(1)

########################################################################################
## Creation of the launch.json file
########################################################################################
launch_data_array = []
for i in package_names:
    # Path to build folder of the package
    path_build = workspace_folder+"/build/"+str(i)

    # Find c++ executables
    files = [f for f in os.listdir(path_build) if os.path.isfile(os.path.join(path_build,f))]
    cpp_executable_names = [name for name in files if not name.endswith((".last",".txt",".cmake",".json",".env",".rc",".sh","ini","Makefile","log"))]

    try:
        #python_folder = os.listdir(workspace_folder+"/build/"+str(i)+"/build")
        python_folder = workspace_folder+"/build/"+str(i)+"/build/lib/"+str(i)
        python_executable_names = [f for f in os.listdir(python_folder) if os.path.isfile(os.path.join(python_folder,f))]

        if"__init__.py" in python_executable_names:
            python_executable_names.remove("__init__.py")
    except:
        python_executable_names = []

    print(i)
    print(python_executable_names)
    print(cpp_executable_names)


    # Add the CPP files to the launch file
    for j in cpp_executable_names:     
        launch_data_array.append({
                        "name": "c++: "+str(j)+"_Node - PKG:"+str(i),
                        "type": "cppdbg",
                        "request": "launch",
                        "program": "${workspaceFolder}/install/"+str(i)+"/lib/"+str(i)+"/"+str(j),
                        "args": [],
                        "stopAtEntry": False,
                        "cwd": "${workspaceFolder}/../../",
                        "environment": [],
                        "externalConsole": False,
                        "MIMode": "gdb",
                        "setupCommands": [
                            {
                                "description": "Enable pretty-printing for gdb",
                                "text": "-enable-pretty-printing",
                                "ignoreFailures": True
                            }
                        ]
                    })

    # Find the python files and also add them to the launch file
    for j in python_executable_names:
        path_package = "./src/"+str(i)
        path_file = glob.glob(path_package + "/**/"+str(j), recursive = True)
        
        path = path_file[0]

        launch_data_array.append({
                        "name": "py: "+str(j)+"_Node - PKG:"+str(i),
                        "type": "python",
                        "request": "launch",
                        "program": "${workspaceFolder}"+path[1:]
        })

# Give the correct form to the launch file     
launch_data = {}
launch_data["configurations"] = launch_data_array

# Store the data in the json file
with open('.vscode/launch.json', 'w') as jsonFile_launch:
    json.dump(launch_data, jsonFile_launch, indent=4)
    jsonFile_launch.close()

