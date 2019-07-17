import matplotlib.pyplot as plt  
import pandas as pd

df = pd.read_csv('result_csv.csv')

df.plot(x='timestamp', y='count')
plt.show()
