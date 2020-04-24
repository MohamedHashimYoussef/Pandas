import pandas as pd

poke = pd.read_csv('Pokemon.csv')  # To read  CSV Data
df = pd.read_excel('Pokemon.xlsx') # To read  Excel Data        # delimiter parameter to take control what is seperate

print(poke.head(5))  # To get First 5 records 
print(poke.tail(3))  # To get Last 3 records

print(poke.columns)  # To know the headers names

print(poke['Name'])  # To get data of name column 

print(poke['Name'][0:5]) # To get first 5 records in name column 

print(poke[['Name' , 'Type 1' , 'Type 2']]) # to get data of multiple columns

print(poke.iloc[0]) # To get first record row data

print(poke.iloc[0,0])   # To get specific location row , Column 

df['Total'] = df['HP'] + df['Attack'] + df['Speed']   # Create new column by summation of previous columns

df = df.drop(columns=['Total'] ) # To delete column from dataframe
df['Total'] = df.iloc[:,4:10].sum(axis=1) # Create new column by summation of previous columns

df.to_csv('modified.csv') # Save updated dataframe

df.to_csv('modified.csv' , index=False) # to unsave indexes

df.loc[df['Type 1'] == 'Grass'] # To filter rows with type Grass

df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')] # filter rows with type 1 grass and type 2 poison

df.groupby(['Type 1']) # Group data with type 1

df.sort_values(['Type 1' , 'Type 2'] , ascending=[False , True]) # To Sort data

# To read huge data
for df in pd.read_csv('Pokemon.csv' , chunksize=5):
    pass

#end
