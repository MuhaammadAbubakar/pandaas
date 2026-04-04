#updating values in a dataframe
import pandas as pd 

data = {
    "name":["raja","rani","ahmed","zia","hira","liaba"],
    "age":[10,20,30,40,23,21],
    "salary":[50000,60000,40000,45000,52000,70000],
    "performance":[72,75,68,89,92,78]
}
df = pd.DataFrame(data)

#update the value at any row and column by using loc function
df.loc[0,"age"] = 25
print("update the value of age")
print(df)

#update the value of full column by using column function
df["salary"] = df["salary"] *1.05
print("update the value of salaryby 5%")
print(df)
