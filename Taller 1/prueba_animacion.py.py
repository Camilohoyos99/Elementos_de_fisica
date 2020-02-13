#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:31:19 2020

@author: tesla
"""


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


class Projectile:
    # class variables for simulation time and number of time slices
    sim_time, time_slices = None, None
    
    def __init__(self, x0, y0, v0, alpha0):
        # projectile initial position and velocity
        self.x, self.y = x0, y0
        self.vx0 = v0 * np.cos(alpha0)
        self.vy0 = v0 * np.sin(alpha0)
        
        # time interval to be simulated
        self.t =np.linespace(0,t_max)
        # esto deberia ser un linspace?

    def kinematics(self, ax, ay):
        # kinematic equations: position and velocity    
        # line points se    
        # line points se
        self.x += self.x + self.vx0 * self.t
        self.y += self.y + self.vy0 * self.t - 5. * grav_ *(self.t **2)
         
        self.vx += self.vx0
        self.vy += self.voy - grav_ * self.t
    
    def get_trajectory(self):
        # returns values of x(t) and y(t)
        kinematics(0,0)
        
        return self.x, self.y