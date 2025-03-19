import matplotlib.pyplot as plt

# 1. form a dictionary
## first line is "language name", second line is "percentage"
language_percentage = {
    "JavaScript": 62.3,
    "HTML": 52.9,
    "Python": 51,
    "SQL": 51,
    "TypeScript": 38.5
}
print (language_percentage)

# 2. construct a bar plot
languages = list(language_percentage.keys()) # input "language name" into languages
percentages = list(language_percentage.values()) # input "percentage" into percentages

plt.bar(languages, percentages, color='lavender') 
# languages are X-axis. percentages are Y-axis. color is purple
plt.xlabel('Programming Languages') 
# label X-axis as "Programming Languages"
plt.ylabel('Users (percentage)') 
# label Y-axis as "Users (percentage)"
plt.title('Programming Language Popularity (February 2024)') 
# name the bar plot as "Programming Language Popularity (February 2024)"
plt.ylim(0, 70)  
# limit the Y-axis range as 0-70%
plt.show() 
# print the bar plot

# 3. get the percentage of a specific language
requested_language = "JavaScript" 
# the specific language
## if want to get the percentage of other languages, modify this variable.
percentage = language_percentage.get(requested_language, "Language not found") 
# get the percentage. 
# If the language is not in the dictionary, return "Language not found".

print(f"The percentage of developers who use {requested_language} is {percentage}%.")
# print the percentage