import pandas as pd

data={
    'Name': ['tiger','elephant','giraffe','lion','zebra'],
    'Age':[41,13,25,6,30],
    'Score':[None,2,38,None,45]
}
df=pd.DataFrame(data)
print(df)

# Use fillna() to fill missing values with specified values
df_filled_data=df.fillna({'Score':'Nan'})

# Display the DataFrame after filling missing values
print("\nDataFrame after Filling Missing Values:")
print(df_filled_data)
