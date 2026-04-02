
import pandas as pd

data = {
    "name":["raja","rani","ahmed","zia","hira","liaba"],
    "age":[10,20,30,40,23,21],
    "salary":[50000,60000,40000,45000,52000,70000],
    "performance":[72,75,68,89,92,78]


}
df = pd.DataFrame(data)

#filter rows based on condition
filter_one_row = df[df["age"]>=20]
print("filter rows based on one condition")
print(filter_one_row)

#filter rows based on multiple conditions by using and operator(&)
filter_multiple_rows = df[(df["salary"]>55000) & (df["performance"]>70)]
print("filter rows based on multiple conditions")
print(filter_multiple_rows)

#filter rows based on multiple conditions by using or operator(|)
filter_or_rows = df[(df["age"]>22) | (df["salary"]>50000)]
print("filter rows based on multiple conditions")
print(filter_or_rows)