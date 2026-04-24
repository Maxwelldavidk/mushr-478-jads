#!/usr/bin/env python3
from __future__ import division

from threading import Lock

import numpy as np


class LowVarianceSampler:
    """Low-variance particle sampler."""

    def __init__(self, particles, weights, state_lock=None):
        """Initialize the particle sampler.

        Args:
            particles: the particles to update
            weights: the weights to update
            state_lock: guarding access to the particles and weights during update,
                since both are shared variables with other processes
        """
        self.particles = particles
        self.weights = weights
        self.state_lock = state_lock or Lock()
        self.n_particles = particles.shape[0]

        # You may want to cache some intermediate variables here for efficiency

    def resample(self):
        """Resample particles using the low-variance sampling scheme.

        Both self.particles and self.weights should be modified in-place.
        """
        # Acquire the lock that synchronizes access to the particles. This is
        # necessary because self.particles is shared by the other particle
        # filter classes.
        #
        # The with statement automatically acquires and releases the lock.
        # See the Python documentation for more information:
        # https://docs.python.org/3/library/threading.html#using-locks-conditions-and-semaphores-in-the-with-statement
        with self.state_lock:
            # BEGIN QUESTION 3.2
            # total num of particles. 
            M = self.n_particles
            # Make a new partilce array as same shape and fill with 0
            new_particles = np.zeros(self.particles.shape)
            # Pick a random starting point uniformly.
            r = np.random.uniform(0, 1 / M)
            # start the weights at the first particle
            weight = self.weights[0]
            # Loop through all particles. The next r + n/M step. While not in the correct weight interval, advance i, add the next particles weight to the sum, ounce in the 
            # correct interval copy particle i into row m of the new particel. 
            i = 0
            for m in range (M):
                next_r = r + m / M
                while next_r > weight:
                    i += 1
                    weight += self.weights[i]

                new_particles[m] = self.particles[i]
            # Overwrite the old particle array inplace with the re sampled particle
            self.particles[:] = new_particles
            # reset all weights
            self.weights[:] = 1.0 / M
            # END QUESTION 3.2
