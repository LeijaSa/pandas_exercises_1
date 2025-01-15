import pandas as pd

data={
    'Name': ['tiger','elephant','giraffe','lion','zebra'],
    'Age':[41,13,6,6,30],
    'Score':[16,2,38,24,45]
}
df=pd.DataFrame(data)
print(df)

# Use groupby() to group the DataFrame by 'Age' and calculate the mean for each group
grouped_data= df.groupby('Age')[['Score']].mean()

# Display the DataFrame after using groupby() and mean()
print("\nDataFrame after using groupby() and mean():")
print(grouped_data)