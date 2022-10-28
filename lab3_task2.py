import numpy as np
from lab_3_task_1 import g, k, e

h = 100
A = np.pi / 3
B = np.pi / 6



v = (g * h * (np.tan(B)) ** 2 / (2 * (np.cos(A)) ** 2 * (1 - np.tan(B) * np.tan(A)))) ** 0.5

print(v)