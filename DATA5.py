import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random


data = np.random.rand(10, 10)

plt.clf()
heatmap = plt.imshow(data, cmap="YlGnBu", aspect='auto')
plt.colorbar(heatmap)
plt.title("Heatmap Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
plt.savefig("./heatmap.png")