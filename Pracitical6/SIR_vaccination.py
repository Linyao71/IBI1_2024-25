# pseudocode：
# 1.import necessary libraries
# 2.define the basic variables of the model
# 3.set initial conditions
# 4.record time course simulation
# 5.plot results
# 6.save results

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def sirv(N, beta, gamma, vaccination_rate, time_points):
    v=int(vaccination_rate*N)
    s=N-v-1
    i=1
    r=0
    sus=[s]  # susceptible (start with all but one)
    inf=[i]       # infected (start with 1)
    re=[r]       # recovered (start with 0)

    for t in range(0, time_points):
        # current state
        presus=sus[-1]
        preinf=inf[-1]
        prereco=re[-1]
    
        # calculate infection probability (beta * proportion infected)
        probinf=float(beta * preinf/N)
        probinf=max(0, min(1, probinf))
    
        # simulate new infections
        presus=max(0, presus)
        newinf=int(np.random.choice(range(2), int(presus), p=[1-probinf, probinf]).sum())
    
        # simulate recoveries
        newreco=int(np.random.choice(range(2), int(preinf), p=[1-gamma, gamma]).sum())
    
        # update compartments
        sus.append(presus-newinf)
        inf.append(preinf+newinf-newreco)
        re.append(prereco+newreco)
    
    return inf

N=10000  # Total population
beta=0.3  # Infection rate
gamma=0.05  # Recovery rate
time_points=1000  # Number of time steps
vaccinated_rate=np.arange(0, 1.1, 0.1) # vaccinated rate
varate=[]

plt.figure(figsize=(6,4), dpi=150) # set up plot's dimensions and resolution
colors = cm.jet(np.linspace(0, 1, len(vaccinated_rate)))  # color map

for rate, color in zip(vaccinated_rate, colors):
    inf_curve = sirv(N, beta, gamma, rate, time_points)
    plt.plot(inf_curve, label=f"{int(rate*100)}%", color=color)

plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR model with different vaccination rates')
plt.legend(title="Vaccination rate") # show legends
plt.grid(True, linestyle='--', color='gray', alpha=0.5) #show grid lines in the background
plt.savefig("Practicals2.png")
plt.show()