#!/bin/bash

CAR_IP="mushr"

# Source ROS
source /opt/ros/noetic/setup.bash

# Source your workspace
source ~/mushr_ws/devel/setup.bash

# Connect to car ROS master
export ROS_MASTER_URI=http://mushr-2933.cs.washington.edu:11311

# Optional: set your local IP
export ROS_IP=$(hostname -I | awk '{print $1}')

# Launch RViz with default config
rosrun rviz rviz -d ~/mushr_ws/src/mushr478/cse478/config/default.rviz