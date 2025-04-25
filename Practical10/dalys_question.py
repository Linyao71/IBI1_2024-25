import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

#question 1
daly1990 = dalys_data[dalys_data.Year == 1990] # Filter data for the year 1990
Q1 = daly1990['DALYs'].quantile(0.25) # calculate Q1
Q3 = daly1990['DALYs'].quantile(0.75) # calculate Q3
IQR = Q3 - Q1 # calculate IQR (Interquartile Range)
upper = Q3 + 1.5 * IQR # calculate upper bound for outliers
lower = Q1 - 1.5 * IQR # calculate lower bound for outliers

# identify outlier countries
upperoutlier = daly1990[daly1990.DALYs > upper]
upperline = upperoutlier[["Entity", "DALYs"]].sort_values('DALYs', ascending=False)
if not upperline.empty:
    print(" The upper outliers are as follows:")
    print(upperline)
else:
    print(" No upper outliers were found.")

loweroutlier = daly1990[daly1990.DALYs < lower]
lowerline = loweroutlier[["Entity", "DALYs"]].sort_values('DALYs', ascending=True)
if not lowerline.empty:
    print(" The lower outliers are as follows:")
    print(lowerline)
else:
    print(" No lower outliers were found.")

# question 2
plt.boxplot(daly1990.DALYs, 
             vert=False, 
             patch_artist=True,
             boxprops=dict(facecolor='lightpink'),
             flierprops=dict(marker='o', markersize=8))

# enhance the plot
plt.title('Global distribution of DALYs in 1990', pad=20, fontsize=14)
plt.xlabel('DALYs', fontsize=12)
plt.yticks([])  # remove y-axis ticks
plt.grid(axis='x', linestyle='--', alpha=0.6)

# add statistical explanations
stats_text = f"Q1: {Q1:,.0f}\nQ3: {Q3:,.0f}\nIQR: {IQR:,.0f}\nOutlier threshold: {upper:,.0f} & {lower:,.0f}"
plt.text(0.98, 0.75, stats_text, 
         transform=plt.gca().transAxes, ha='right', va='top',
         bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.savefig("boxplot.png", dpi=300, bbox_inches='tight')
plt.show()

# question 3
country = ['China', 'United Kingdom']
mask = dalys_data['Entity'].isin(country)
subset = dalys_data[mask]

for cou in country:
    countrydata = subset[subset.Entity == cou]
    plt.plot(countrydata['Year'], countrydata['DALYs'], label=cou)

plt.title('DALYs Trend: China vs UK (1990-2019)')
plt.xlabel('Years')
plt.ylabel('DALYs')
plt.legend()
plt.grid(True)
plt.savefig("trend.png", dpi=300, bbox_inches='tight')
plt.show()
