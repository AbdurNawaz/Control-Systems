
import numpy as np
from matplotlib import pyplot as plt 
import control
from matplotlib.pyplot import style

# style.use('seaborn')

G = control.TransferFunction((25.05, 100.2), (1, 8, 16.05, 28.2))

rlist, klist = control.rlocus(G, grid=0)

plt.grid()
plt.show()