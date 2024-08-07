import numpy
import pandas as pd

my_index= [1, 2, 3]
my_columns = ['이름', '나이', '성별']
my_data = numpy.array([['Alice', 'Bob', 'Robert'],
                      [25, 30, 26],
                       ['남', '여', '남']]).transpose()

df = pd.DataFrame(my_data, index=my_index, columns=my_columns)
print(df, df.shape)
print("-"*30)
print(df['이름'])
print("-"*30)
print(df, "\n", df.loc["A"])
print("-"*30)