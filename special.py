import random as rd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'name': ['rabbit', 'lade', 'moti_sand'],
    'age': [100, 75, 0],
}

df = pd.DataFrame(data)
bars = plt.bar(df['name'], df['age'])

plt.bar_label(bars, fmt='%d')

plt.xlabel('overall parhai ki report')
plt.title('saal ki report')
plt.show()
