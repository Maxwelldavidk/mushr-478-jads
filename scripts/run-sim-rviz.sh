#!/bin/bash

source ~/mushr_ws/devel/setup.bash

roslaunch localization particle_filter_teleop_sim.launch \
map:='$(find cse478)/maps/cse2_2.yaml'