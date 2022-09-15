import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/91997/Desktop/Shruthi/breast cancer/data.csv")
df.head()
df.shape
df.columns
df.info()
df.isna ().sum()
df=df.drop ('Unnamed: 32',axis=1)
df['diagnosis'].unique()





