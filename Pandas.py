import pandas as pd
import numpy as np

my_index = np.array([1, 2, 3])
data= ["홍길동", "김길동", "박길동"]
series = pd.Series(data)

print(series)

data_2 = [10, 20, 30, 40, 50]
series_2 = pd.Series(data_2)

print(series_2)