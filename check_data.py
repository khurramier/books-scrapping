import pandas as pd
df = pd.read_csv("books.csv")
print(df.head())
print(df.shape)
#Missing data check
print(df.isnull().sum())
# cleaning price column
df['Price'] = pd.to_numeric(df['Price'].str.replace('\u00C2', '').str.replace('\u00A3', ''))
print(df['Price'].head())
#Saving cleaned data
df.to_csv('books_cleaned_data.csv', index=False)