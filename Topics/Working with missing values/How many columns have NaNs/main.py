#  write your code here 

import pandas as pd
path = "C:/Users/daile/PycharmProjects/Data Analysis for Hospitals/Topics/Working with missing values/How many columns have NaNs/data/dataset/input.txt"
df = pd.read_csv(path)
count = 0
print(df.isnull().any().sum())