# Project 2: Localization [![tests](../../../badges/submit-proj2/pipeline.svg)](../../../pipelines/submit-proj2/latest)

In the motion model plot, why are there more particles within a 10cm radius of the noise-free model prediction in Figure 2 than Figure 3?

1: Figure 2 has more particles within 10 cm of the noise-free prediction because the given motion in example_cases is much smaller. The velocity and timestep are both lower, so the vehicle travels a shorter distance and accumulates less uncertainty. In Figure 3, the vehicle moves faster, for longer, and turns more, so both control noise and model noise spread the particles farther from the deterministic next state. As a result, fewer particles remain within 10 cm of the noise-free prediction.

Include mm1.png, mm2.png, and mm3.png, your three intermediate motion model plots for control 
. Use them to explain your motion model parameter tuning process. For each plot, explain how it differs from Figure 3, and how you changed the parameters in response to those differences. The last plot should reflect your final tuned parameters.

2: 
Initial motion paramaters-
![mm1 motion model](./mm1.png)
Loaded parameters: {'vel_std': 0.05, 'delta_std': 0.5, 'x_std': 0.05, 'y_std': 0.05, 'theta_std': 0.05}. 
Compared to Figure 3 in the spec, this plot was much too spread out, with only 2/100 particles within 10 cm of the mean. Since the particles were too spread out, I concluded that the parameters were too noisy, so I needed to lower their standard deviation values.


Second tuning attempt-
![mm2 motion model](./mm2.png)
Loaded parameters: {'vel_std': 0.03, 'delta_std': 0.2, 'x_std': 0.02, 'y_std': 0.02, 'theta_std': 0.02}
This produced a better result. The particles were still spread along the expected curved banana-shaped trajectory, but the distribution was more concentrated and looked closer to Figure 3, with 10/100 particles within 10 cm of the mean. This was an improvement, but it was still more dispersed than the reference plot, so I reduced the noise parameters further.



Final tuning attempt-
![mm3 motion model](./mm3.png)
Loaded parameters: {'vel_std': 0.03, 'delta_std': 0.1, 'x_std': 0.01, 'y_std': 0.01, 'theta_std': 0.01}
This plot matched Figure 3. The particle distribution had the same banana-shaped spread as the reference plot, and 21/100 particles were within 10 cm of the mean, matching the reference figure. Lowering the steering angle noise and the state noise made the particles cluster more tightly around the expected curved motion while still preserving the overall spread expected from the motion model.



