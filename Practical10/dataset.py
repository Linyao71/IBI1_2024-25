import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("C:/Users/asus/Desktop/IBI/IBI1_2024-25/Practical10")

'''print(os.getcwd())
print(os.listdir())'''

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

'''print(data.head(3))
print(data.info())'''

'''describe = dalys_data.describe()

maxdaly = describe.loc['max', 'DALYs']
mindaly = describe.loc['min', 'DALYs']

print(f"max DALY: {maxdaly}")
print(f"min DALY: {mindaly}")

year = dalys_data['Year'].describe()
first = year['min']
latest = year['max']
    
print(f"first year: {int(first)}")
print(f"latest year: {int(latest)}")'''

'''print(dalys_data.iloc[0,3])'''

'''print(dalys_data.iloc[2,0:5])
print(dalys_data.iloc[0:2,:])
print(dalys_data.iloc[0:10:2,0:5])'''

'''print(dalys_data.iloc[0:10,2])
tenthyear = dalys_data.iloc[9,2]
print(f"the 10th year for which DALYs were recorded in Afghanistan: {tenthyear}")'''

'''# same as "print(dalys_data.iloc[0:3,[0,1,3]])""
my_columns = [True, True, False, True]
print(dalys_data.iloc[0:3,my_columns])'''

# like "print(dalys_data.loc[2:4,"Year"])
year = dalys_data["Year"]
specificyear = dalys_data["Year"] == 1990
daly1990 = dalys_data.loc[specificyear, "DALYs"]
print(daly1990)