#  write your code here 
import pandas as pd
path = "C:/Users/daile/PycharmProjects/Data Analysis for Hospitals/Topics/Handling missing values/Replace with the mode/data/dataset/input.txt"
df = pd.read_csv(path)
mode_loc = df['location'].mode()[0]
df['location'].fillna(mode_loc, inplace=True)
print(df.head(5))