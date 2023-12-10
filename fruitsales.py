# add your code here
# importing pandas
import pandas as pd

# Creating a fruit sales dictionary

data = {
   'Apples': ['2017 Sales', '2018 Sales'],
   'Bananas': [35, 41]
}

# creating the dataframe
df = pd.DataFrame(data)

# writing the dataframe to a CSV file
df.to_csv('fruit.csv', index=False)
