#  write your code here 
import pandas as pd
path = "C:/Users/daile/PycharmProjects/Data Analysis for Hospitals/Topics/Summarizing categorical columns/Rock it/data/dataset/input.txt"
df = pd.read_csv(path)
print(df['labels'][df['labels']=="R"].count())