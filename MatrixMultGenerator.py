import numpy as np


class MatrixMultGenerator:

    vmin = -5
    vmax = 5

    def generate(self, w, h, s, restrictToIntegers):
        m1 = np.random.randint(self.vmin, self.vmax, size=(w, s))
        print(m1)
        m2 = np.random.randint(self.vmin, self.vmax, size=(s, h))
        print(m2)
        sol = m1@m2
        print(sol)
