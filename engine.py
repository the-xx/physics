

import numpy as np
from body import Body
import logging
logging.basicConfig(level=logging.INFO)

# https://www.cs.cmu.edu/~baraff/sigcourse/notesc.pdf

class Engine:
    bodies: list[Body]
    time: float

    def __init__(self, options={}):
        defaults = {
            'bodies': [],
            'time': 0,
        }
        defaults.update(options)
        self.bodies = defaults['bodies']
        self.time = defaults['time']

    def add_body(self, body):
        self.bodies.append(body)

    def clear_forces(self):
        for body in self.bodies:
            body.force = np.zeros(3)
            body.torque = np.zeros(3)

    def get_derivates(self):
        self.clear_forces()
        self.compute_forces()
        derivatives = []
        for body in self.bodies:
            # [x1,x2,x3, v1,v2,v3] =  [v1,v2,v3, f1,f2,f3]
            # ...
            # n bodies
            derivatives.append(np.concatenate(
                (body.velocity, body.force / body.mass), axis=None))
        logging.debug('derivatives %r', derivatives)
        return derivatives

    def get_states(self):
        states = []
        # [x1,x2,x3, v1,v2,v3]
        # ...
        # n bodies
        logging.debug('bodies: %r', self.bodies)
        for body in self.bodies:
            states.append(np.concatenate(
                (body.position, body.velocity), axis=None))
        logging.debug('state: %r', states)
        return states

    def set_states(self, states):
        for i, body in enumerate(self.bodies):
            body.position = states[i][0:3]
            body.velocity = states[i][3:6]

    def integrate_euler(self, dt):
        derivatives = self.get_derivates()
        current_states = self.get_states()
        new_states = []
        logging.debug('current_states %r', current_states)
        for i, body in enumerate(self.bodies):
            scaler = dt * derivatives[i]
            new_state = current_states[i] + scaler
            new_states.append(new_state)
        self.set_states(new_states)

    def apply_gravity(self):
        for body in self.bodies:
            body.force += np.array([0, -9.8, 0]) * body.mass

    def compute_forces(self):
        self.apply_gravity()

    def simulate(self, dt):
        self.integrate_euler(dt)
        self.time = self.time + dt
