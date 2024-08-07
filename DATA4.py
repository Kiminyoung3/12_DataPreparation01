import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random


data = [random.gauss(0, 1) for _ in range(100)]
outliers = [-10, 10]

plt.clf()
plt.boxplot(data+outliers, vert=False, patch_artist=True)
plt.title("Boxplot example with outliers")
plt.xlabel("Values")
plt.xticks(range(-15, 6, 5))
plt.show()
plt.savefig("./boxplot.png")