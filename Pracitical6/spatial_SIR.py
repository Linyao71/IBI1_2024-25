# pseudocode：
# 1.import necessary libraries
# 2.set basic parameters
# 3.set variables
# 4.plot results
# 5.save results

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

size=100  # Total population
beta=0.3  # Infection rate
gamma=0.05  # Recovery rate
time_points=100  # Number of time steps

# make array of allsusceptible population
population=np.zeros((size,size)) # 0 = susceptible, 1 = infected, 2 = recovered
population[4,12]

# random initial outbreak
outbreak = np.random.choice(range(size), 2)
population[outbreak[0], outbreak[1]] = 1

# create figure for plotting
fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
img = ax.imshow(population, cmap='viridis',vmin=0, vmax=2, interpolation='nearest')
plt.colorbar(img, label='State (0=Susceptible, 1=Infected, 2=Recovered)')

def update(time_points):
    global population
    # make a copy of the current state
    new_population=population.copy()
    
    # find all infected points
    infected_indices=np.where(population == 1)
    infected_points=list(zip(infected_indices[0], infected_indices[1]))
    
    # pocess each infected point
    for i, j in infected_points:
        # try to infect neighbors
        for x in range(max(0, i-1), min(size, i+2)):
            for y in range(max(0, j-1), min(size, j+2)):
                # ckip the center point itself
                if x == i and y == j:
                    continue
                # Only infect susceptible neighbors
                elif population[x, y] == 0 and np.random.random() < beta:
                    new_population[x, y] = 1
        
        # try to recover
        if np.random.random() < gamma:
            new_population[i, j] = 2
    
    # update the population
    population=new_population
    
    # update the plot
    img.set_array(population)
    ax.set_title(f'Time Step: {time_points}')
    return img,

# create animation
ani = FuncAnimation(fig, update, frames=time_points, interval=200, blit=False)
plt.show()