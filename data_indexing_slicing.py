import pandas as pd

data={
    'Name': ['cat','dog','giraffe','lion','mouse'],
    'Age':[21,43,15,26,28],
    'Score':[6,2,8,4,5,]
}
df=pd.DataFrame(data)
# Use set_index() to set the 'Name' column as the index
df_indexed = df.set_index('Name')
print(df_indexed)

# Use boolean indexing to filter rows where Age is greater than 25
df_filtered=df_indexed[df_indexed['Age']>25]
print(df_filtered)