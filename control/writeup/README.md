# Project 3: Control [![tests](../../../badges/submit-proj3/pipeline.svg)](../../../pipelines/submit-proj3/latest)

What tradeoffs did varying the Kp gain have on your PD controller’s performance?

1: Increasing Kp made the controller respond more aggressively to cross-track error. This helped the car correct back toward the path faster, but if Kp was too high it also made the controller more oscillatory and caused overshoot, especially on curved paths. Increasing Kd added damping, which reduced oscillation and helped smooth out the response, but if Kd was too large the controller became too sluggish and under-corrected. In general, the tradeoff was between responsiveness and stability with larger Kp improved correction speed, while larger Kd improved damping, but too much of either hurt the tracking quality in different ways.

Describe the tuning process for your PD controller. Justify your final gains Kp, Kd and include the controller plots for three reference paths on the default sandbox map (pid_circle.png, pid_left.png, pid_wave.png).

2: We tuned the PD controller by starting from the provided baseline values Kp = 0.5 and Kd = 0.5 and then observing the controller behavior on multiple reference paths. With the higher starting gains, the controller was too aggressive, especially on curved paths, and this showed up as oscillation and overshoot. We then reduced the gains and compared the tracking behavior again. Lowering both gains to Kp = 0.3 and Kd = 0.3 produced a smoother response and reduced the unwanted oscillation while still allowing the car to follow the required paths successfully. We chose these as the final gains because they gave the best overall compromise between stability and path tracking performance across the circle, left-turn, and wave paths. 

Describe the lookahead distance tuning process for your Pure Pursuit controller. Justify your final lookahead distance by including the controller plot for the wave reference path on the default sandbox map (pp_wave.png).

3: We tuned the Pure Pursuit controller by varying the lookahead distance and comparing the tracking behavior on the required paths. When the lookahead distance was too small, the controller became too reactive and produced oscillatory behavior because it chased points too close to the current vehicle position. As we increased the lookahead distance, the tracking became smoother and more stable, but if the lookahead became too large the controller began smoothing out the path too much and performed worse on tighter turns like left-turn. I found that a lookahead distance of 1.0 gave the best compromise across both the wave path and the left-turn path. It tracked the wave path smoothly while still handling turns better than larger lookahead values.

Include controller plots on the wave path for cases where the lookahead distance is too small/large (pp_small.png, pp_large.png). Explain the resulting Pure Pursuit behavior.

4:

How does varying the radius of the circle path affect the robustness of the Pure Pursuit controller?

5: Larger circle radius are easier for the Pure Pursuit controller to track because they correspond to softer curvature. With a large radius, the controller can follow the path more smoothly and with less tracking error. Smaller circle radius are less robust because they require sharper turning, and Pure Pursuit’s geometric lookahead can smooth out the turn if the lookahead distance is too large relative to the circle radius. In our case, this caused the controller to cut the corner and follow a larger-radius circle than the reference circle. A smaller lookahead can help Pure Pursuit handle tighter turns, but if it is too small the controller becomes more reactive and oscillatory. In other words, Pure Pursuit is generally more robust on wide, gradual curves than on very tight turns.