#!/bin/bash

# Function to wait for the prompt cursor
wait_for_prompt() {
  tmux send-keys -t "$1" C-m  # Ensure the prompt is fully loaded
  while true; do
    if tmux capture-pane -t "$1" -p | grep -q -E '[$#]'; then
      break
    fi
    sleep 0.5
  done
}

# Create a new tmux session in detached mode
tmux new-session -d -s ros_sessions

# Window 1: Teleop
tmux new-window -t ros_sessions:1 -n "teleop"
wait_for_prompt "ros_sessions:1"
tmux send-keys -t ros_sessions:1 "roslaunch mushr_base teleop.launch" C-m

# Window 2: Map Server
tmux new-window -t ros_sessions:2 -n "map_server"
wait_for_prompt "ros_sessions:2"
tmux send-keys -t ros_sessions:2 "rosrun map_server map_server \$(rospack find cse478)/maps/002.yaml" C-m

# Window 3: Localization
tmux new-window -t ros_sessions:3 -n "localization"
wait_for_prompt "ros_sessions:3"
tmux send-keys -t ros_sessions:3 "roslaunch localization particle_filter_sim.launch use_namespace:=true publish_tf:=true tf_prefix:=\"car/\"" C-m

# Window 4: Costmap (after localization)
tmux new-window -t ros_sessions:4 -n "costmap"
wait_for_prompt "ros_sessions:4"
tmux send-keys -t ros_sessions:4 "rosparam load \$(rospack find control)/config/costmap_params.yaml /costmap_node/costmap && rosrun costmap_2d costmap_2d_node _name:=costmap_node" C-m

# Window 5: Controller
tmux new-window -t ros_sessions:5 -n "controller"
wait_for_prompt "ros_sessions:5"
tmux send-keys -t ros_sessions:5 "roslaunch control controller.launch type:=mpc tf_prefix:=\"car/\"" C-m

# Window 6: Planner
tmux new-window -t ros_sessions:6 -n "planner"
wait_for_prompt "ros_sessions:6"
tmux send-keys -t ros_sessions:6 "roslaunch planning planner_car.launch num_vertices:=1000 connection_radius:=20 curvature:=1 num_goals:=8" C-m

# Attach to the session
tmux attach-session -t ros_sessions
