import numpy as np


class MatrixMultGenerator:

    vmin = -2
    vmax = 3

    def generate(self, w, h, s, restrictToIntegers):
        m1 = np.random.randint(self.vmin, self.vmax, size=(w, s))
        m2 = np.random.randint(self.vmin, self.vmax, size=(s, h))
        sol = m1@m2
        return (m1, m2, sol)
        # TODO: create rational version
