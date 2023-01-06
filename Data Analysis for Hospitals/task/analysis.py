import pandas as pd
import matplotlib.pyplot as plt
# Set max columns to display
pd.set_option('display.max_columns', 8)
# Get links to data files
general = "C:/Users/daile/OneDrive/pythonProject/general.csv"
prenatal = "C:/Users/daile/OneDrive/pythonProject/prenatal.csv"
sports = "C:/Users/daile/OneDrive/pythonProject/sports.csv"
# Read data files from links into dataframes
general_df = pd.read_csv(general,header=0)
prenatal_df = pd.read_csv(prenatal, header=0)
sports_df = pd.read_csv(sports, header=0)
# Rename columns to unified names
prenatal_df = prenatal_df.rename(columns={"HOSPITAL": "hospital",
                                          "Sex": "gender"})
sports_df = sports_df.rename(columns={"Hospital": "hospital",
                                      "Male/female": "gender"})
# Concat all 3 three dataframes
df = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)
# Drop unncessary columns
df = df.drop(["Unnamed: 0"], axis=1)
# Drop empty rows
df = df.dropna(how="all")
# Replace female and woman with f, male and man with m
df["gender"].replace({"female": "f",
                      "woman": "f",
                      "male": "m",
                      "man": "m"},
                     inplace=True)
# Replace NaN in gender column of prenatal hospital with f
df['gender'][df["hospital"]=="prenatal"] = df['gender'][df["hospital"]=="prenatal"].fillna("f")


# Fill NaNs in other columns with 0
df = df.fillna(value={"bmi": 0,
                 "diagnosis": 0,
                 "blood_test": 0,
                 "ecg": 0,
                 "ultrasound": 0,
                 "mri": 0,
                 "xray": 0,
                 "children": 0,
                 "months": 0})


# Name of hospital with the most patients
maxpatient =  df['hospital'].value_counts().idxmax()
# Number of patients in general hospital
ngeneral = df['hospital'][df['hospital']=='general'].count()
# Number of patients in sports hospital
nsports = df['hospital'][df['hospital']=='sports'].count()
# Number of patients in prenatal hospital
nprenatal = df['hospital'][df['hospital']=='prenatal'].count()
# Number of patients in general hospital diagnosed with stomach issue
nstomachgen = df['diagnosis'][df["diagnosis"]=="stomach"][df['hospital']=='general'].count()
# Number of patients in sports hospital diagnosed with dislocation issue
ndislocationsports = df['diagnosis'][df["diagnosis"]=="dislocation"][df['hospital']=='sports'].count()
# Name of hospital with the most patients who took blood tests
tmaxhospital = df["hospital"][df['blood_test']=='t'].value_counts().idxmax()
# Number of blood tests in hospital with the most patients who took blood tests
tmax = df["hospital"][df['blood_test']=='t'].value_counts().max()
# Median age of patients in general hospital
med_general = df['age'][df['hospital'] == 'general'].median()
# Median age of patients in sports hospital
med_sports = df['age'][df['hospital'] == 'sports'].median()
# Different in median ages between patients in general and sports hospital
med_diff = med_general - med_sports
# Pct of patients with stomach issue in general hospital
sharestomach = (nstomachgen/ngeneral).round(3)
# Pct of patients with dislocation issue in sports hospital
sharesdislocation = (ndislocationsports/nsports).round(3)
# Histogram of age range of all patients among all hospitals
fig1, axes1 = plt.subplots()
plt.hist(df['age'])
plt.show()
# Diagnoses among patients in all hospitals
diag = df['diagnosis'].value_counts()
# Pie chart to show most common diagnosis
diaglabels = diag.index
fig2, axes2 = plt.subplots()
plt.pie(diag, labels=diaglabels)
plt.show()
# Violin plot of height distribution by hospitals
heightgen = df["height"][df["hospital"] == "general"]
heightpre = df["height"][df["hospital"] == "prenatal"]
heightsports = df["height"][df["hospital"] == "sports"]
heightdata = [heightgen, heightpre, heightsports]
fig3, axes3 = plt.subplots()
axes3.set_xticks((1,2,3))
axes3.set_xticklabels(("general", "prenatal", "sports"))
axes3.set_ylabel("Height")
plt.violinplot(heightdata)
plt.show()
# What is the most common age of a patient among all hospitals?
# Plot a histogram and choose one of the following age ranges:
# 0-15, 15-35, 35-55, 55-70, or 70-80
print("The answer to the 1st question: 15-35")
# What is the most common diagnosis among patients in all hospitals?
# Create a pie chart
print("The answer to the 2nd question: pregnancy")
# Build a violin plot of height distribution by hospitals.
# What is the main reason for the gap in values?
# Why there are two peaks, which correspond to the relatively small and big values?
print("The answer to the 3rd question: It's because there are 2 metric systems used: International System of Units and U.S customary units")