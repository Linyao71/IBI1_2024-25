a=15
b=75
c=a+b

d=90
e=5
f=d+e

if c>f:
    print("The car is faster than the bus. The bus takes longer time than the car.")
elif c<f:
    print("The bus is faster than the car. The car takes longer time than the bus.")
else:
    print("The bus is as fast as the car. They takes same time to go to the office.")
#The bus is faster than the car. The ar takes longer time than the bus.

X=True
Y=True
W= X and Y
print (W)
#	truth	table	for	W
# X     Y     W
# True  False False
# False True  False
# False False False
# True  True  True