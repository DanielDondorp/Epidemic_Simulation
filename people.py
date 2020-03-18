#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:26:56 2020

@author: daniel
"""

import numpy as np
import pandas as pd
from diseases import Virus

class Person:
    def __init__(self, virus = Virus, world_size = 1000, ID = None):
        self.pos = np.random.uniform(0,1000,size = (2,))
        self.moving = False
        self.infected = False
        self.immune = False
        self.alive = True
        self.ID = ID
        self.world_size = world_size
        self.virus = virus()
    def start_moving(self):
        self.moving = True
        self.velocity = np.random.uniform(-5,5, size = (2,))
    
    def update(self, population):
        if self.moving:
            self.pos += self.velocity
            self.meet_people(population)
        if self.infected:
            self.be_sick()
            
    def meet_people(self, population):
        others = np.vstack([p.pos for p in population if p != self])
        dists = np.linalg.norm(others - self.pos, axis = 1)
        closest = population[np.argmin(dists)]
        closest_dist = dists.min()
        if closest_dist < 10:
            self.encounter(closest)
            self.velocity = np.random.uniform(-5,5, size = (2,))
        self.edges()
        
    def encounter(self, other):
        if self.infected and not other.infected:
            other.get_sick()
        elif not self.infected and other.infected:
            self.get_sick()
            
    def get_sick(self):
        if not self.immune:
            self.infected = True
            self.time_ill = 0
    
    def be_sick(self):
        self.time_ill += 1
        if self.time_ill >= self.virus.duration:
            self.heal()
        elif np.random.random() < self.virus.mortality_rate:
            self.die()
        
    def heal(self):
        self.virus = None
        self.infected = False
        self.immune = True
        
    def die(self):
        self.alive = False
        
    def edges(self):
        self.velocity[self.pos > self.world_size] *= -1
        self.velocity[self.pos < 0] *= -1