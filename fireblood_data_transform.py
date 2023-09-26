import pandas as pd

file_path = r"C:\Users\P\Downloads\archive\artists.csv"

df = pd.read_csv(file_path)

#print(df.head())

# checking the shape of the dataset(no. of rows, columns)
#print(df.shape)

# checking for data types and missing values
print(df.info())

#dropping null rows from the Daily column
df.dropna(subset=['Daily'], inplace=True)

# converting the Streams to only numeric
df['Streams'] = pd.to_numeric(df['Streams'], errors='coerce')

print(df.info())

# fill missing rows with the mean of the As lead
df['Daily'].fillna(df['Daily'].mean(), inplace=True)

#drop duplicates
df = df.drop_duplicates()

# removing trailing whites and lowercasing.
df['Artist'] = df['Artist'].str.strip()
df['Artist'] = df['Artist'].str.lower()

#check for missing values
null_values = df.isnull().sum()
print(null_values)

#exporting the file
export_file = r"C:\Users\P\Downloads\cleansed_artists.csv"
df.to_csv(export_file, index=False)
