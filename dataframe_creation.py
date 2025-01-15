import pandas as pd

data={
    'Name': ['cat','dog','giraffe','lion','mouse'],
    'Age':[11,13,15,16,18],
    'Score':[6,2,8,4,5]
}
df=pd.DataFrame(data)
print(df)