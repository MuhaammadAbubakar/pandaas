import pandas as pd

data = {
    "name":["raja","rani","ahmed","zia","hira","liaba"],
    "age":[10,20,30,40,23,21],
    "salary":[50000,60000,40000,45000,52000,70000],
    "performance":[72,75,68,89,92,78]


}
df = pd.DataFrame(data)
print(df.describe())