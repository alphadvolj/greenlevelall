import pandas as pd

data = {
    'numbers': [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)

df['cumulative_sum'] = df['numbers'].cumsum()

print(df)