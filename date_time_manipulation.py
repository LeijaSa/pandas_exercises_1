import pandas as pd

data={
    'Date':['2019.9.24', '2015.7.14', '2025.1.3', '2008-8-31'],
}

df=pd.DataFrame(data)

# Passing `format='mixed'`, and the format will be inferred for each element individually
df['Date']=pd.to_datetime(df['Date'],format='mixed')

# Display the DataFrame after using to_datetime()
print("\nDataFrame after using to_datetime():")
print(df)