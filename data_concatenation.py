import pandas as pd

data={
    'Name': ['Tina','Elma','Giron','Lione','Zahray','Juli'],
    'Age':[41,13,25,6,30,65],
    'Score':[16,2,38,24,45,65]
}

second_data={
    'Name': ['Keira','Elmon','Hjalmar','Urg','Pietrus','Dier'],
    'Age':[19,55,35,13,34,29],
    'Occupation': ['Engineer', 'Data Scientist','Teacher', 'Student', 'Manager','Unemployed'],
}

df1=pd.DataFrame(data)
df2=pd.DataFrame(second_data)

#The ignore_index=True parameter is used to reindex the resulting DataFrame.
concatenated_dataframe=pd.concat([df1,df2], ignore_index=True)

# Display the DataFrame after using concat()
print("\nDataFrame after using concat():")
print(concatenated_dataframe)