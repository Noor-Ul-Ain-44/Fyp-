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
