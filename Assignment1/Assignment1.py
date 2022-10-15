import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv(r'C:/Users/natha/OneDrive/Desktop/Coding/RSM338/RSM338-Assignment-1/data/AAPL.csv')
df = pd.DataFrame(data)
get_rows_100 = df.head(100)

print(get_rows_100)