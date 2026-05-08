#!/bin/bash

source ~/mushr_ws/devel/setup.bash

# Find all YAML map files in the maps directory
map_dir="$(rospack find cse478)/maps"
map_files=("$map_dir"/*.yaml)

# Check if any maps were found
if [ ${#map_files[@]} -eq 0 ]; then
  echo "No map files found in $map_dir"
  exit 1
fi

# Display menu
echo "Available maps:"
for i in "${!map_files[@]}"; do
  filename=$(basename "${map_files[$i]}")
  echo "$((i+1))) $filename"
done

# User selection
read -p "Enter map number: " choice

# Validate input
if ! [[ "$choice" =~ ^[0-9]+$ ]] || \
   [ "$choice" -lt 1 ] || \
   [ "$choice" -gt "${#map_files[@]}" ]; then
  echo "Invalid selection."
  exit 1
fi

selected_map="${map_files[$((choice-1))]}"

echo "Launching with map: $(basename "$selected_map")"

roslaunch cse478 teleop.launch map:="$selected_map"