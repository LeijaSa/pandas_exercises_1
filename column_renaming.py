import pandas as pd

data={
    'Date':['2019.9.24', '2015.7.14', '2025.1.3', '2008-8-31'],
    'Value':['sports', 'library', 'sports', 'theater']
}

df=pd.DataFrame(data)
print(df)

# Renaming the column 'Date' to 'EventDate' and 'Value' to 'EventValue'
df_renamed=df.rename(columns={'Date':'EventDate', 'Value':'EventValue'})

# Display the DataFrame after renaming the column
print("\nDataFrame after renaming the column:")
print(df_renamed)