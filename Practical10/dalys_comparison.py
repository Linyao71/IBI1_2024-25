import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["DALYs", "Year"]]
france = dalys_data.loc[dalys_data.Entity == "France", ['DALYs', 'Year']]

ukmean = uk['DALYs'].mean()
francemean = france['DALYs'].mean()

if ukmean > francemean:
    print("The mean DALYs for the UK is larger than that of France.")
elif ukmean < francemean:
    print("The mean DALYs for the France is larger than that of UK.")
else:
    print("the mean DALYs for the UK and France are equal.")

# output:
# The mean DALYs for the UK is larger than that of France.

plt.plot(uk.Year, uk.DALYs, 
         markersize=4,       # Kky tick size
         markerfacecolor='Lavender', # fill color
         markeredgecolor='#BA55D3', # border color
         markeredgewidth=1, # border width
         color='Purple', # line color
         linestyle=':',         # line style
         marker='p',          # marker type
         label="DALYs in the UK") 

plt.xticks(uk.Year,rotation=-60)
plt.show()