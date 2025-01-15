import pandas as pd

data={
    'Occupation': ['Engineer', 'Data Scientist','Teacher', 'Student', 'Manager','Teacher','Data Scientist','Teacher', 'Student', 'Manager'],
    'Value':[41,13,25,6,30,7,23,90,58,2],
}
df=pd.DataFrame(data)
print(df)

unique_occupation=df['Occupation'].unique()
# Display the unique values in the 'Occupation' column
print("\nUnique Values in the 'Occupation' Column:")
print(unique_occupation)

# Use nunique() to count the number of unique values in the 'Category' column
num_unique_occupations = df['Occupation'].nunique()

# Display the number of unique values in the 'Category' column
print("\nNumber of Unique Values in the 'Occupation' Column:")
print(num_unique_occupations)