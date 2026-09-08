import pandas as pd
import numpy as np

array = np.array([[4, 7, 8], [5,8,11], [6, 9, 12]])
df = pd.DataFrame(array, columns=['a', 'b', 'c'], index=[1,2,3])
print(df)
print(df.melt().rename(columns={'variable':'var', 'valuable': 'val'}))