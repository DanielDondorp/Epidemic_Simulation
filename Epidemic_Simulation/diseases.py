#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:28:52 2020

@author: daniel
"""


class Virus:
    def __init__(self, duration = 200, mortality_rate = 0.0):
        self.duration = duration
        self.mortality_rate = mortality_rate