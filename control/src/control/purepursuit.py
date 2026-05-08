from __future__ import division
import numpy as np

from control.controller import BaseController
from control.controller import compute_position_in_frame


class PurePursuitController(BaseController):
    def __init__(self, **kwargs):
        self.car_length = kwargs.pop("car_length")

        # Get the keyword args that we didn't consume with the above initialization
        super(PurePursuitController, self).__init__(**kwargs)


    def get_error(self, pose, reference_xytv):
        """Compute the Pure Pursuit error.

        Args:
            pose: current state of the vehicle [x, y, heading]
            reference_xytv: reference state and speed

        Returns:
            error: Pure Pursuit error
        """
        return compute_position_in_frame(reference_xytv[:3], pose)

    def get_control(self, pose, reference_xytv, error):
        """Compute the Pure Pursuit control law.

        Args:
            pose: current state of the vehicle [x, y, heading]
            reference_xytv: reference state and speed
            error: error vector from get_error

        Returns:
            control: np.array of velocity and steering angle
        """
        # BEGIN QUESTION 3.1
        "*** REPLACE THIS LINE ***"

        # velovity is from the reference velocity
        velocity = reference_xytv[3]
        # e_x is the first element of the error vector, e_y is the second element of the error vector.
        e_x = error[0]
        e_y = error[1]
        # numerator is 2 * car_length * e_y, denominator is e_x^2 + e_y^2, delta is arctan(numerator / denominator).
        numerator = 2 * self.car_length * e_y
        denominator = e_x**2 + e_y**2
        if denominator == 0.0:
            delta = 0.0
        else: 
            delta = np.arctan(numerator / denominator)
        # return np.array of velocity and delta as a two element array.
        return np.array([velocity, delta])
        # END QUESTION 3.1
