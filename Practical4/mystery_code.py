# What does this piece of code do?
# Answer:
#Roll a number between 1 and 6 twice.
#If the two numbers are the same, stop and say the number of attempts. 
#If not, try again. The number of attempts add 1.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
while progress>=0: #run a loop when the progress is exist and no be broken
	progress+=1 #count the progress times
	first_n = randint(1,6) #roll first number between 1 and 6, store in first_n
	second_n = randint(1,6) #roll second number between 1 and 6, store in second_n
	if first_n == second_n: #check whether first_n equal to second_n 
		print(progress) #print the number of attempts
		break # if first_n equal to second_n, break this loop

