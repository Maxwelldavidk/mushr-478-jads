#!/bin/bash

# Interactive loop for running RRT with custom eta and bias values

while true
do
    echo ""
    read -p "Enter iterations (-x) value: " ITERS
    read -p "Enter eta (-e) value: " ETA
    read -p "Enter bias (-b) value: " BIAS    

    echo ""
    echo "Running search with:"
    echo "  eta  = $ETA"
    echo "  bias = $BIAS"
    echo "  iter = $ITERS"
    echo ""
    
    cd ~/mushr_ws/src/mushr478/planning
    python3 scripts/run_search \
        -m test/share/map1.txt \
        --algorithm rrt \
        -x "$ITERS" \
        -e "$ETA" \
        -b "$BIAS" \
        --show-edges r2 \
        -s 1 1 \
        -g 8 7

    echo ""
    read -p "Run again? (y/n): " AGAIN

    if [[ "$AGAIN" != "y" && "$AGAIN" != "Y" ]]; then
        break
    fi
done

