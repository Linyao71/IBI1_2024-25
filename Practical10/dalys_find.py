import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("C:/Users/asus/Desktop/IBI/IBI1_2024-25/Practical10")

print(os.getcwd())
print(os.listdir())
print()

# output: 
# C:/Users/asus/Desktop/IBI/IBI1_2024-25/Practical10
# ['dalys-rate-from-all-causes.csv', 'dalys_find.py']'''

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

print(dalys_data.head(3)) # first 3 rows
print(dalys_data.info()) # first 3 rows with column names and data types
print()
describe = dalys_data.describe()

maxdaly = describe.loc['max', 'DALYs']
mindaly = describe.loc['min', 'DALYs']

print(f"max DALY: {maxdaly}")
print(f"min DALY: {mindaly}")
print()
#out put：
#max DALY: 693367.49
#min DALY: 15045.11

year = dalys_data['Year'].describe()
first = year['min']
latest = year['max']
    
print(f"first year: {int(first)}")
print(f"latest year: {int(latest)}")
print()
# output:
# first year: 1990
# latest year: 2019

print(dalys_data.iloc[0,3]) # 1st row, 4th column
print(dalys_data.iloc[2,0:5]) # first 5 columns of the 3rd row
print(dalys_data.iloc[0:2,:]) # first 2 rows, all columns
print(dalys_data.iloc[0:10:2,0:5]) # first 10 rows, every 2nd row, first 5 columns
print()

print(dalys_data.iloc[0:10,2]) # 1st 10 rows, 3rd column
print()
# output: 
# 0    1990
# 1    1991
# 2    1992
# 3    1993
# 4    1994
# 5    1995
# 6    1996
# 7    1997
# 8    1998
# 9    1999

afghanistan = dalys_data[dalys_data["Entity"] == "Afghanistan"] # filter rows where Entity is Afghanistan
tenthyear = afghanistan.iloc[9,2]  # 10th row, 3rd column (year)
print(f"the 10th year for which DALYs were recorded in Afghanistan: {tenthyear}")  
print()
# output: 1999

# same as "print(dalys_data.iloc[0:3,[0,1,3]])"
my_columns = [True, True, False, True]
print(dalys_data.iloc[0:3,my_columns]) # first 3 rows, 1st, 2nd and 4th columns
print()
# output:
# Entity	Code	DALYs
# 0	Afghanistan	AFG	86375.17
# 1	Afghanistan	AFG	83381.07
# 2	Afghanistan	AFG	79890.55

# like print(dalys_data.loc[2:4,"Year"])
year = dalys_data["Year"]
specificyear = dalys_data["Year"] == 1990
daly1990 = dalys_data.loc[specificyear, ["Entity", "DALYs"]]
print(daly1990) # DALYs in 1990 in all countries as a list
print()
# output:
#                               Entity     DALYs
# 0                        Afghanistan  86375.17
# 30              African Region (WHO)  81293.92
# 60                           Albania  32964.61
# 90                           Algeria  44481.53
# 120                   American Samoa  35230.49
# ...                              ...       ...
# 6690  World Bank Lower Middle Income  61774.10
# 6720  World Bank Upper Middle Income  41087.86
# 6750                           Yemen  67015.90
# 6780                          Zambia  90310.81
# 6810                        Zimbabwe  55804.06

# [228 rows x 2 columns]

# print the DALYs in 1990 one by one
for index, row in daly1990.iterrows():
    print(f"{row['Entity']} {row['DALYs']}")
