
import pandas as pd

import pandas as pd

data = {
    "Firstname":["raja","rani","ahmed","zia","hira","liaba"],
    "age":[10,20,30,40,23,21],
    "salary":[50000,60000,40000,45000,52000,70000],
    "performance":[72,75,68,89,92,78]


}
df = pd.DataFrame(data)
print(df)

#adding a column by direct method
df["bonus"] = df["salary"] * 0.1
print(df)

#adding a column by using the insert method
df.insert(1,"Lastname",["sb","sahiba","jutt","khan","mani","rajput"])
print(df)