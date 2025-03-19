import matplotlib.pyplot as plt

# 1. Create and sort 2 lists
# population in 2022 of countries in the United Kingdom	
uk_countries = [57.11, 3.13, 1.91, 5.45] # store the population in list	"uk_countries"
uk_countries_sorted = sorted(uk_countries) # in order of smallest to largest

# population in	2022 of the	provinces in China which border Zhejiang province	
china_provinces = [65.77, 41.88, 45.28, 61.27, 85.15] # store the population in list "china_provinces"
china_provinces_sorted = sorted(china_provinces) # in order of smallest to largest

# print the sorted lists
print("UK countries population (millions):", uk_countries_sorted) #Print "uk_countries_sorted"
print("Provinces border Zhejiang province population (millions):", china_provinces_sorted) #Print "china_provinces_sorted"

# 2. Draw 2 pie charts
# the pie chart for countries in the United Kingdom
uk_country = ['England', 'Wales', 'Northern Ireland', 'Scotland'] # set country name
plt.figure(figsize=(12, 7)) # create a new graphics window, set the width and height
plt.subplot(1, 2, 1) # create a subplot in the graphics window, select the first subplot
plt.pie(uk_countries_sorted, labels=uk_country, autopct='%1.1f%%', startangle=90, 
        colors=['mistyrose', 'powderblue', 'teal', 'lightcoral'],
        pctdistance=0.8,  # the percentage label is 0.8 away from the center of the circle
        labeldistance=1.1)  # the distance between the text label and the center of the circle is 1.1
plt.title('Population percentages in UK Countries') # set title

# the pie chart for provinces border Zhejiang
china_province = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu'] # set provinece name
plt.subplot(1, 2, 2) # create a subplot in the graphics window, select the second subplot
plt.pie(china_provinces_sorted, labels=china_province, autopct='%1.1f%%', startangle=90, 
        colors=['lightyellow', 'lightcyan', 'thistle', 'khaki', 'powderblue'])
plt.title('Population Distribution in Zhejiang-neighbouring Provinces') # set title

plt.tight_layout() # adjust the layout of subplots to avoid overlapping.
plt.show() #show the window