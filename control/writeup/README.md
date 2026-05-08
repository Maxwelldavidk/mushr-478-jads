# Project 3: Control [![tests](../../../badges/submit-proj3/pipeline.svg)](../../../pipelines/submit-proj3/latest)

For the controller plots, you may submit either an image of PlotJuggler or a screenshot of RViz after the path has completed.

## 1

What tradeoffs did varying the \(K_p\) gain have on your PD controller's performance?

Increasing Kp made the controller respond more aggressively to cross-track error. This helped the car correct back toward the path faster, but if Kp was too high it also made the controller more oscillatory and caused overshoot, especially on curved paths. Increasing Kd added damping, which reduced oscillation and helped smooth out the response, but if Kd was too large the controller became too sluggish and under-corrected. In general, the tradeoff was between responsiveness and stability with larger Kp improved correction speed, while larger Kd improved damping, but too much of either hurt the tracking quality in different ways.

## 2

Describe the tuning process for your PD controller. Justify your final gains \(K_p, K_d\) and include the controller plots for three reference paths on the default sandbox map (pid_circle.png, pid_left.png, pid_wave.png).

We tuned the PD controller by starting from the provided baseline values Kp = 0.5 and Kd = 0.5 and then observing the controller behavior on multiple reference paths. With the higher starting gains, the controller was too aggressive, especially on curved paths, and this showed up as oscillation and overshoot. We then reduced the gains and compared the tracking behavior again. Lowering both gains to Kp = 0.3 and Kd = 0.3 produced a smoother response and reduced the unwanted oscillation while still allowing the car to follow the required paths successfully. We chose these as the final gains because they gave the best overall compromise between stability and path tracking performance across the circle, left-turn, and wave paths.

![pid_circle.png](pid_circle.png)
![pid_left.png](pid_left.png)
![pid_wave.png](pid_wave.png)

## 3

Describe the lookahead distance tuning process for your Pure Pursuit controller. Justify your final lookahead distance by including the controller plot for the wave reference path on the default sandbox map (pp_wave.png).

We tuned the Pure Pursuit controller by varying the lookahead distance and comparing the tracking behavior on the required paths. When the lookahead distance was too small, the controller became too reactive and produced oscillatory behavior because it chased points too close to the current vehicle position. As we increased the lookahead distance, the tracking became smoother and more stable, but if the lookahead became too large the controller began smoothing out the path too much and performed worse on tighter turns like left-turn. I found that a lookahead distance of 1.0 gave the best compromise across both the wave path and the left-turn path. It tracked the wave path smoothly while still handling turns better than larger lookahead values.

![pp_wave.png](pp_wave.png)

## 4

Include controller plots on the wave path for cases where the lookahead distance is too small/large (pp_small.png, pp_large.png). Explain the resulting Pure Pursuit behavior.

TODO

![pp_small.png](pp_small.png)
![pp_large.png](pp_large.png)

## 5

How does varying the radius of the circle path affect the robustness of the Pure Pursuit controller?

Larger circle radius are easier for the Pure Pursuit controller to track because they correspond to softer curvature. With a large radius, the controller can follow the path more smoothly and with less tracking error. Smaller circle radius are less robust because they require sharper turning, and Pure Pursuit's geometric lookahead can smooth out the turn if the lookahead distance is too large relative to the circle radius. In our case, this caused the controller to cut the corner and follow a larger-radius circle than the reference circle. A smaller lookahead can help Pure Pursuit handle tighter turns, but if it is too small the controller becomes more reactive and oscillatory. In other words, Pure Pursuit is generally more robust on wide, gradual curves than on very tight turns.

## 6

Describe the tuning process for the MPC optimization parameters. Justify your final parameters \(K, T\) by including the controller plots for the circle, wave, and saw reference paths on the default sandbox map. What makes the saw path so difficult to track?

We tuned the MPC parameters by starting with the initial values (K = 5, T = 10) and incrementally increasing each parameter. We found that increasing K gave the controller more steering angle candidates to choose from, which improved its ability to find a good control action, while increasing T gave the controller a longer planning horizon, which helped it anticipate upcoming turns. We first turned K to make sure our paths were directionally correct then we tuned T to make our paths of acceptable granularity. Through this iterative process, we settled on K = 8 and T = 15. K = 8 provided enough steering sample coverage for good path tracking without excessive computation, and T = 15 gave the controller enough lookahead to anticipate curves while keeping the control frequency high enough for stable operation. The combination of K = 8 and T = 15 produced smooth tracking on the circle and wave paths with good error margins.

The saw path is very difficult for MPC to track because it has sharp, sudden changes in direction (vertices of the sawtooth). Unlike the smooth curves of the circle and wave paths, the saw path's sharp corners require the controller to quickly switch steering direction, which is challenging for a sample-based MPC with a discrete set of steering angle candidates and a fixed horizon. The controller tends to cut the sharp corners because none of the K sampled steering sequences perfectly capture the aggressive steering reversal needed, resulting in larger tracking errors at the vertices.

![mpc_circle.png](mpc_circle.png)
![mpc_wave.png](mpc_wave.png)
![mpc_saw.png](mpc_saw.png)

## 7

Include controller plots for two reference paths and slaloms of your choice in the slalom_world map.

![slalom1.png](slalom1.png)
![slalom2.png](slalom2.png)

## 8

In this project, we asked you to implement a very specific MPC cost function that only includes distance and collision terms (and specific weights for the two terms). What other terms might you include, if you were to customize your cost function? (You don't have to implement this, just describe some ideas.)

TODO

## 9

Include a bag file and a screenshot of rviz for the MPC running on the real car with
`rosrun control path_sender circle --tf_prefix "car/" --speed 1.0 --radius 1`
and
`rosrun control path_sender wave --tf_prefix "car/" --speed 0.5`

DONE

## 10

Include a bag file and a screenshot of rviz for each controller (pid, pp and mpc) running on the real car. See above for the detailed instructions.

DONE
