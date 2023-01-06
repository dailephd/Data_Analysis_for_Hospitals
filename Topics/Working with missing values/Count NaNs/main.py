#  write your code here 
import pandas as pd
path ="C:/Users/daile/PycharmProjects/Data Analysis for Hospitals/Topics/Working with missing values/Count NaNs/data/dataset/input.txt"
df = pd.read_csv(path)

print(df.isnull().sum())