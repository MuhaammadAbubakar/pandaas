#handle missing values
import pandas as pd

data = {
    "name":["raja","rani",None,"zia","hira","liaba"],
    "age":[10,None,30,40,23,21],
    "salary":[50000,60000,40000,45000,52000,70000],
    "performance":[72,75,None,89,92,78]
}
df = pd.DataFrame(data)

print(df.isnull())
print(df.isnull().sum())