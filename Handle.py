#how to drop value and fill values
import pandas as pd

data = {
    "name":["raja","rani","ahmed","zia","hira","liaba"],
    "age":[10,None,30,40,23,21],
    "salary":[50000,60000,40000,45000,52000,70000],
    "performance":[72,75,None,89,92,78]
}
df = pd.DataFrame(data)
#print(df)

#drop values if we remove specific rows and columns by using axis =0,1
#df.dropna(inplace=True)
#print(df)

#fill value by using fillna() method
df.fillna(5,inplace=True)
print(df)

#df["performance"].fillna(df["performance"].mean(), inplace=True)   
#print(df)
