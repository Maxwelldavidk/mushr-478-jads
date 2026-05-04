from __future__ import division
import numpy as np

from control.controller import BaseController
from control.controller import compute_position_in_frame


class PIDController(BaseController):
    def __init__(self, **kwargs):
        self.kp = kwargs.pop("kp")
        self.kd = kwargs.pop("kd")

        # Get the keyword args that we didn't consume with the above initialization
        super(PIDController, self).__init__(**kwargs)


    def get_error(self, pose, reference_xytv):
        """Compute the PD error.

        Args:
            pose: current state of the vehicle [x, y, heading]
            reference_xytv: reference state and speed

        Returns:
            error: across-track and cross-track error
        """
        return compute_position_in_frame(pose, reference_xytv[:3])

    def get_control(self, pose, reference_xytv, error):
        """Compute the PD control law.

        Args:
            pose: current state of the vehicle [x, y, heading]
            reference_xytv: reference state and speed
            error: error vector from get_error

        Returns:
            control: np.array of velocity and steering angle
                (velocity should be copied from reference velocity)
        """
        # BEGIN QUESTION 2.1
        "*** REPLACE THIS LINE ***"
        # copy velocity from the reference state and speed.
        velocity = reference_xytv[3]
        # take the cross track error from the error vector [e_at, e_ct]
        e_ct = error[1]
        # the derivative of e_ct take the argument heading - reference heading.
        heading_error = pose[2] - reference_xytv[2]
        # the derivative of e_ct is velocity * -sin(heading_error)
        e_ct_dot = velocity * np.sin(heading_error)
        # delta is the u(t) in the control law for PID control, we are using PD control.
        delta = -(self.kp * e_ct + self.kd * e_ct_dot)
        # return np.array of velocity and delta as a two element array.
        return np.array([velocity, delta])
        # END QUESTION 2.1
