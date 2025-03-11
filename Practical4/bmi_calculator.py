# pseudocode：
# 1. Store a person's weight (kg) and height (m)
# 2. Calculate BMI: BMI = weight / (height ** 2)
# 3. Determine weight categories based on BMI values.：
#    - BMI < 18.5: Underweight
#    - 18.5 <= BMI <= 30: normal weight
#    - BMI > 30: Obesity
# 4. Output the BMI value and weight category.

weight= 60  #Store a person's weight (kg)
height= 1.65  #Store a person's height (m)
print(f"the weight is {weight}, and the height is {height}")

bmi=weight/(height**2) #Calculate BMI

#Determine weight categories
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 30:
    category = "normal weight"
else:
    category = "Obesity"

#Output the BMI value and weight category
print(f"The BMI value is {bmi}")
print(f"The weight category is: {category}")