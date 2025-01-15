import pandas as pd

data={
    'Name': ['tiger','elephant','giraffe','lion','zebra'],
    'Age':[41,13,25,6,30],
    'Score':[16,2,38,24,45]
}
df=pd.DataFrame(data)
print(df)

def convert_to_float(score:int):
    return float(score)

# Use apply() to apply the custom function to the 'Score' column
df['Score'] = df['Score'].apply(convert_to_float)
print("\nDataFrame after using apply():")
print(df)

# Another way to do this
# Use astype() to convert the 'Age' column from int to float
#df['Age'] = df['Age'].astype(float)