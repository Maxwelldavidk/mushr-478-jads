#!/bin/bash

# =========================
# CONNECTION SETTINGS
# =========================

HOST="mushr-2933.cs.washington.edu"
USER="mushr"
PASSWORD="prl_robot"

# =========================
# SSH LOGIN + COMMANDS
# =========================

sshpass -p "$PASSWORD" ssh -X -t "$USER@$HOST" "mushr_noetic"

source ~/catkin_ws/devel/setup.bash

EOF