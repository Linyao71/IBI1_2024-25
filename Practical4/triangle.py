# Pseudocode:
# 1. Compute the Nth triangle number
# 2. Use a loop to count the dot of first 10 triangles
# 3. Print the first 10 triangles


a=0 #the variable to store the number of dots required to form the trigngle
for n in range (1,11): #the nth triangle 
    a+=n #compute the dots
    print (f"T{n} = {a}") #print the answer