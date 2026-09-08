import pandas as pd
import numpy as np

array = np.array(
    [
        [100, 100, 100],
        [52.3, 99, 91],
        [99, 97, 82]
    ]
)
df = pd.DataFrame(array, columns=['Kor', 'Eng', 'Math'], index =['이시우', '구ㅈ모', '정지훈'])
print(df)