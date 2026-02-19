# Fyp-
Configured a ROS 2 Humble environment on Ubuntu (WSL2) 
Implemented an SQLite3 backend to ensure data persistence for visitor logs
Developed a Python-based telemetry_node.py that aggregates robot data (Battery, Navigation, and Perception) into a unified JSON Master Object
# Communication part 
Deployed rosbridge_suite to create a communication gateway between the Linux ROS 2 environment and the Windows-based Web Dashboard
Created a responsive HTML/CSS dashboard featuring a Visitor Check-in system and a Real-time Status monitor
For Dynamic Data Binding Used roslibjs to subscribe to the JSON telemetry stream, enabling the UI to update status without page refreshes
For User Feedback Loop Implemented JavaScript logic to provide instant UI confirmation upon database entry
# Cross Platform integration 
Bridged the gap between Linux and Windows file systems using explorer.exe integration to serve web assets and audit database files via DB Browser for SQLite
# Prerequisites
To run this project you need to have the following installed and configured:
Operating System Ubuntu 22.04 LTS (running via WSL2).
ROS 2 Distribution: ROS 2 Humble
Build Tool: colcon (to build the robot packages).
GWSL (Windows Utility): Used to bridge the graphical interface between Linux and Windows, allowing ROS-based GUIs (like Rviz or Gazebo) to appear as Windows apps
ROS Bridge Suite: Essential for connecting the Humble backend to the Web Frontend.
Install command: sudo apt install ros-humble-rosbridge-server
roslibjs Integrated via CDN to handle the WebSocket communication in the browser
DB Browser for SQLite Windows-side tool to inspect the visitor tables
Python 3.10  For running the telemetry and logging logic
# To run the system
Launch the WebSocket Bridge through this command : ros2 launch rosbridge_server rosbridge_websocket_launch.xml
Start telemetry node by this command: cd ~/fyp_ws
source install/setup.bash
ros2 run robot_control_pkg telemetry_node
Locate dashboard folder for index.html
