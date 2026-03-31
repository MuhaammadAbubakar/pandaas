import pandas as pd

#load the data and how to read
df = pd.read_csv(r"C:\Users\rajas\Desktop\pandas practice\pandaas\PIA_2026_Advanced_Kaggle_Dataset.csv")
print(df)
print(df.shape)

#print atleast first 5 rows
print("Print first 5 rows")
print(df.head(5))

#print atleast last 5 rows
print("Print last 5 rows")
print(df.tail(5))

#use info() method to check how mny rows and hw many columns and 
# data type of each column and also tell how many null values and 
# also how many memory consumed.
print(df.info())

#use describe function to get the statistical summary of the data
print(df.describe())
