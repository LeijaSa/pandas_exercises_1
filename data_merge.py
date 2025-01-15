import pandas as pd

data={
    'ID': [1,2,3,4,5,6],
    'Name': ['Tina','Elma','Giron','Lione','Zahray','Juli'],
    'Age':[41,13,25,6,30,65]
}

second_data={
    'ID': [1,2,3,4,5,7],
    'Occupation': ['Engineer', 'Data Scientist','Teacher', 'Student', 'Manager','Unemployed'],
    'Salary':[4100,3100,2500,1600,5000,0],
}
df_one=pd.DataFrame(data)
df_two=pd.DataFrame(second_data)

# Outer Join (how='outer'): Keeps all rows from both DataFrames, filling non-matching rows with NaN
# 'inner' or 'left' or 'right' could be used to
merged_df=pd.merge(df_one,df_two, on='ID',how='outer')

# Display the DataFrame after using merge()
print("\nDataFrame after using merge():")
print(merged_df)