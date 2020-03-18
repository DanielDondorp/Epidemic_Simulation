#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:30:09 2020

@author: daniel
"""
import tqdm
from people import Person
from diseases import Virus
import numpy as np

class Simulation:
    def __init__(self, population_size = 500, moving_fraction = 1, time_p0 = 100, frames = 1000, world_size = 2000):
        self.population_size = population_size
        self.world_size = world_size
        self.population = [Person(virus = Virus, world_size=self.world_size, ID = i) for i in range(self.population_size)]
        self.moving_fraction = moving_fraction
        self.movers = np.random.random(self.population_size) < moving_fraction
        self.movers_index = np.where(self.movers)[0]
        for mover in self.movers_index:
            p = self.population[mover]
            p.start_moving()
        self.time_p0 = time_p0
        self.frames = frames
            
    def run_simulation(self):
        t = 0
        self.history = np.zeros(shape=(4,))
        for t in tqdm.tqdm(range(self.frames)):
            if t == self.time_p0:
                p0 = np.random.choice(self.population)
                p0.get_sick()
                p0.start_moving()
            infected = 0
            cured = 0
            dead = 0
            for p in self.population:
                p.update(self.population)
                if p.infected:
                    infected += 1
                if p.immune:
                    cured +=1
                if not p.alive:
                    dead += 1
                    self.population.remove(p)
            self.history = np.vstack([self.history, np.array([t,infected,cured, dead])])  
        
