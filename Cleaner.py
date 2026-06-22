import pandas as pd

# 1. Load dirty CSV file
df = pd.read_csv('trx-10k.csv')

# 2. check the total number of rows and columns 
print("---Data Size (Rows, Column)---")
print(df.shape)

# 3. View the first 5 rows to see how data looks 
print("\n--- First 5 rows of Data ---")
print(df.head())

# 4. Count the missing (null) values in each column 
print("\n--- Missing Values Count --- ")
print(df.isnull().sum()) 

# 5. Drop duplicate rows
df = df.fillna("Unknown")

# 6. verify if all missing values are cleaned 
print("\n--- After Cleaning : Missing Values Count ---")
print(df.isnull().sum())

# 7. Save the perfectly cleaned data into a new CSV file 
df.to_csv('cleaned_trx.csv', index=False)
print("\nSuccess!! Cleaned data saved as 'cleaned_trx.csv'")