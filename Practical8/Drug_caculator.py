'''
1.define the caculating function to caculate 
2.if the strength is our of range, say wrong
3.require the chidren's weight and required strength
4.use the function and return the result
'''

def dosage (weight, strength):
    volume = weight*15/strength
    return volume

while True:
    W = float(input("please input the childern's weight (in kg): "))
    if 10 <= W <= 100:
        break
    print("The weight provided is out of the specification, please re-enter")

option = [120, 250]

print("possible strengths of paracetamol: 120mg/5ml or 250mg/5ml)")
while True:
    M = int(input("please input the required mass of niacinamide corresponding to 5ml of solution (120 or 250): "))
    if M in option:
        break
    print("Meaningless input. Please choose beteen 120mg/5ml and 250mg/5ml.")

V = dosage(W,M)
print (f"the required volume of paracetamol is {V}ml")

'''running example:
>please input the childern's weight (in kg): 
>9

>The weight provided is out of the specification, please re-enter
>please input the childern's weight (in kg): 
>10

>possible strengths of paracetamol: 120mg/5ml or 250mg/5ml)
>please input the required mass of niacinamide corresponding to 5ml of solution (120 or 250): 
>270

>Meaningless input. Please choose beteen 120mg/5ml and 250mg/5ml.
>please input the required mass of niacinamide corresponding to 5ml of solution (120 or 250): 
>120
>the required volume of paracetamol is 1.25
'''