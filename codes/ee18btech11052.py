
import numpy as np
from matplotlib import pyplot as plt 
import control
from matplotlib.pyplot import style

# style.use('seaborn')

G = control.TransferFunction((25.05, 100.2), (1, 8, 16.05, 28.2))

rlist, klist = control.rlocus(G)


plt.annotate("Pole, P1", (-6.13, -2))
plt.annotate("Pole, P2", (-1, 3))
plt.annotate("Pole, P3", (-1, -3))
plt.annotate("Zero, Z1", (-4, 1))
plt.legend()
plt.show()