
import numpy as np
import matplotlib.pyplot as plt
from simulation import Simulation
from multiprocessing import Pool

def run_sim(sim):
    sim.run_simulation()
    return sim

def plot_results(sims):
    fig, axes = plt.subplots(len(sims),1,figsize = (10,len(sims)*2), sharex= True, constrained_layout = True)
    for s, ax in zip(sims, axes):
        i = s.moving_fraction
        ax.fill_between(x = s.history[:,0], y1 = np.zeros_like(s.history[:,0]), y2 = s.history[:,1], label = "infected", alpha = 0.5)
        ax.fill_between(x = s.history[:,0], y1 = s.history[:,1], y2 = s.population_size - s.history[:,2], label = "healthy", alpha = 0.5)
        ax.fill_between(x = s.history[:,0], y1 = s.population_size - s.history[:,2], y2 = [s.population_size for x in range(len(s.history))], label = "cured", alpha = 0.5)
        ax.legend()
        ax.set_ylabel("Infected Individuals")
        ax.set_title(f"moving_fraction = {i}")
    ax.set_ylim(0,s.population_size)
    ax.set_xlabel("Time in frames")
    fig.suptitle(f"Population Size: {s.population_size}, World Size: {s.world_size}, Frames: {s.frames}")
    
    fig.savefig(f"Sim_p{s.population_size}_w{s.world_size}_f{s.frames}.png")


if __name__ == "__main__":
    population_size = 500
    frames = 1000
    world_size = 500
    fractions = [1/frac for frac in [1,2,4,8]]    
    sims = [Simulation(population_size = population_size, moving_fraction=frac, world_size=world_size) for frac in fractions]   
    p = Pool(4)
    results = p.map(run_sim, sims)
    plot_results(results)