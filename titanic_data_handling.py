import pandas as pd

# Exercises based on jpg-file

def read_file(filename):
    try:
        df=pd.read_csv(filename)
        df.rename(columns=lambda x:x.strip())
        df.loc[df['Age'] < 18, 'Sex' ] ='child'
        return df
    except:
        print("Error: Unable to read the file or the file does not exist.")

def average_fare_per_sex(dataframe):
    grouped_df=dataframe.groupby('Sex')[['Fare']].mean()
    return grouped_df

def average_fare_per_sex_and_pclass(dataframe):
    grouped_df=dataframe.groupby(['Sex','Pclass'])[['Fare']].mean()
    return grouped_df

def average_fare_per_survived(dataframe):
    grouped_df=dataframe.groupby(['Survived'])[['Fare']].mean()
    return grouped_df

def split_dataset(dataframe):
    df1=dataframe[dataframe['Sex']=='child']
    df2=dataframe[dataframe['Sex']=='female']
    df3=dataframe[dataframe['Sex']=='male']
    return df1, df2, df3

def splitted_records(*dfs):
    return [df.shape for df in dfs]

def get_certain_filtered_columns(dataframe):
    filtered_df=dataframe.loc[(dataframe['Siblings/Spouses Aboard']>0) | (dataframe['Parents/Children Aboard']>0),['Pclass', 'Name','Age','Siblings/Spouses Aboard','Parents/Children Aboard']]
    return filtered_df

def filter_records(dataframe):
    filtered_df=dataframe.loc[(dataframe['Siblings/Spouses Aboard']>0) | (dataframe['Parents/Children Aboard']>0),['Pclass', 'Name','Age','Siblings/Spouses Aboard','Parents/Children Aboard', 'Fare']]
    modified_df=filtered_df.loc[((filtered_df['Siblings/Spouses Aboard']==0) & (filtered_df['Parents/Children Aboard']>0)) | ((filtered_df['Siblings/Spouses Aboard']>0) & (filtered_df['Parents/Children Aboard']==0)) ,['Pclass', 'Name','Age','Siblings/Spouses Aboard','Parents/Children Aboard', 'Fare']]
    return modified_df

def average_fare_by_certain_columns(dataframe):
    grouped_df=dataframe.groupby('Pclass')[['Fare']].mean()
    return grouped_df


def main():
    dataframe=read_file('titanic.csv')
    # print when required
    average_fare_per_sex(dataframe)
    average_fare_per_sex_and_pclass(dataframe)
    average_fare_per_survived(dataframe)
    df1,df2,df3=split_dataset(dataframe)
    get_certain_filtered_columns(dataframe)
    filtered=filter_records(dataframe)
    print(average_fare_by_certain_columns(filtered))

if __name__ == "__main__":
    main()