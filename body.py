import numpy as np


class Body:
    BASE_DELTA = 1000 / 60

    def __init__(self, options={}):
        defaults = {
            'position': [0, 0, 0],
            'velocity': [0, 0, 0],
            'mass': 1,
            'inertia': [1, 1, 1],
            'force': [0, 0, 0],
            'torque': [0, 0, 0],
            'orientation': [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            'angular_velocity': [0, 0, 0],
            'deltaTime': Body.BASE_DELTA,
        }
        defaults.update(options)
        self.position = np.array(defaults['position'])
        self.velocity = np.array(defaults['velocity'])
        self.mass = defaults['mass']
        self.inertia = np.array(defaults['inertia'])
        self.force = np.array(defaults['force'])
        self.torque = np.array(defaults['torque'])
        self.orientation = np.array(defaults['orientation'])
        self.angular_velocity = np.array(defaults['angular_velocity'])
        self.deltaTime = defaults['deltaTime']
