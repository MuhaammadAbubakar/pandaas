#Selecting coulmns one by one and multiple columns
import pandas as pd
data = {
    "name":["raja","rani","ahmed","zia","hira","liaba"],
    "age":[10,20,30,40,23,21],
    "salary":[50000,60000,40000,45000,52000,70000],
    "performance":[72,75,68,89,92,78]
}
df = pd.DataFrame(data)
print(df)
#select one column only by this method

select_columns = df["name"]
print(select_columns)

#select multiple columns by this method
select_multiple = df[["name","age","salary"]]
print(select_multiple)