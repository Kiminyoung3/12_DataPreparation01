import pandas as pd

data = {
    "이름": ['Lily', 'Bob', "Robert"],
    "나이": [25, 30, 23],
    "성별": ['여', '남', '남']
}

df = pd.DataFrame(data)
print(df)