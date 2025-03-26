# pseudocode：
# 1.import necessary libraries
# 2.set basic variables of the SIRV model
# 2.set basic parameters
# 3.set variables
# 4.plot results
# 5.save results

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches

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
main,sub=plt.subplots(figsize=(6, 4), dpi=150)
color=mcolors.ListedColormap(['green', 'red', 'gray'])  # choose 3 colors: green，1=red，2=gray
confine=mcolors.BoundaryNorm([0, 1, 2, 3], color.N)  # define the confine：0-1=0, 1-2=1, 2-3=2
img=sub.imshow(population, cmap=color,norm=confine) # set the figure ligand

legend_label=['Susceptible', 'Infected', 'Recovered']
legend_color=['green', 'red', 'gray']
patches = [mpatches.Patch(color=legend_color[i], label=legend_label[i]) for i in range(3)]
sub.legend(handles=patches, loc='center left', bbox_to_anchor=(1, 0.5), frameon=False) # show the figure ligand

# undergo time course simulation with showing each day polt
def new(time_points):
    global population
    new_population=population.copy() # make a copy of the current state
    
    findinf=np.where(population == 1)  # find all infected points
    recordinf=list(zip(findinf[0], findinf[1]))  # record all infected points
    
    # pocess each infected point
    for a, b in recordinf:
        # try to infect neighbors
        for x in range(max(0, a-1), min(size, a+2)):
            for y in range(max(0, b-1), min(size, b+2)):
                # Only infect susceptible neighbors, skip infected point and recovered point
                if (x!=a or y!=b) and population[x, y] == 0 and np.random.random() < beta:
                    new_population[x, y] = 1
        
        # try to recover
        if np.random.random() < gamma:
            new_population[a, b] = 2
    
    # update the population
    population=new_population
    
    # update the plot
    img.set_array(population)
    sub.set_title(f'Time: the {time_points} days')
    return img,

# create animation
ani=FuncAnimation(main, new, frames=time_points, interval=200, blit=False)
plt.show()