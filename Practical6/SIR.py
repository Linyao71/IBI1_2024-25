# pseudocode：
# 1.import necessary libraries
# 2.define the basic variables of the model
# 3.set initial conditions
# 4.make and record time course simulation
# 5.plot results

import numpy as np
import matplotlib.pyplot as plt

N=10000  # Total population
beta=0.3  # Infection rate
gamma=0.05  # Recovery rate
time_points=1000  # Number of time steps

sus=[N-1]  # susceptible (start with all but one)
inf=[1]       # infected (start with 1)
re= [0]       # recovered (start with 0)

for t in range(0, time_points):
    # current state
    presus=sus[-1]
    preinf=inf[-1]
    prereco=re[-1]
    
    # calculate infection probability (beta * proportion infected)
    probinf=beta * preinf/N
    
    # simulate new infections
    newinf=np.random.choice(range(2), presus, p=[1-probinf, probinf]).sum()
    
    # simulate recoveries
    newreco=np.random.choice(range(2), preinf, p=[1-gamma, gamma]).sum()
    
    # update compartments
    sus.append(presus-newinf)
    inf.append(preinf+newinf-newreco)
    re.append(prereco+newreco)

plt.figure(figsize=(6,4), dpi=150) # set up plot's dimensions and resolution
plt.plot(sus, label='Susceptible')
plt.plot(inf, label='Infected')
plt.plot(re, label='Recovered')
plt.xlabel('Time (/days)')
plt.ylabel('Number of People')
plt.title('SIR Model Simulation (β=0.3, γ=0.05)')
plt.legend() # show legends
plt.grid(True, linestyle='--', color='gray', alpha=0.5) #show grid lines in the background
plt.savefig("Practicals1.png")
plt.show()