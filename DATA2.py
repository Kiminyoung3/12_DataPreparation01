import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

x = [random.uniform(0,100) for _ in range(200)]

y = [2*val+1+random.uniform(-10,10) for val in x]

print(x, "\n", y)
plt.clf()
plt.scatter(x, y, label="Random Data Points", color="green", marker="x", s=30, alpha=0.5)
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.legend()
plt.savefig("./scatter2.png")
plt.show()

