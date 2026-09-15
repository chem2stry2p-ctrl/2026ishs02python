import numpy as np
import pandas as pd

df = pd.read_csv('smart_classroom.csv')
df = df.rename(columns={'timestamp':'Datetime'})
df = df.set_index('Datetime')

