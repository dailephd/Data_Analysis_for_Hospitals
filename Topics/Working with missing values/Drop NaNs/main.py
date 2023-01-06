#  write your code here 
import pandas as pd
path = "C:/Users/daile/PycharmProjects/Data Analysis for Hospitals/Topics/Working with missing values/Drop NaNs/data/dataset/input.txt"
df = pd.read_csv(path)
df2 = df.dropna()
print(df.shape[0],df2.shape[0])