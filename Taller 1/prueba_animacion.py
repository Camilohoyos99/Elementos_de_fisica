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
        self.vx0 = v0 * np.cos(np.radians(alpha0))
        self.vy0 = v0 * np.sin(np.radians(alpha0))
        
        # time interval to be simulated
        self.t =np.linspace(0,t_max,1000)
        # esto deberia ser un linspace?

    def kinematics(self, ax, ay):
        # kinematic equations: position and velocity    
        # line points se    
        # line points se
        self.x += self.x + self.vx0 * self.t
        self.y += self.y + self.vy0 * self.t - 5. * grav_ *(self.t **2)
         
        self.vx0 += self.vx0
        self.vy0 += self.vy0 - grav_ * self.t
    
    def get_trajectory(self):
        # returns values of x(t) and y(t)
        self.y = self.y[self.y>=0]
     
        #preguntar que hacer para llegar al 0, si forzarlo o que putas.
        self.x = self.x[:len(self.y)]
        
        return self.x, self.y
    










# physical constants (in arbitrary units)
grav_ = 1
drag_ = .0 * grav_
t_max = 10
params = [val for val in range(15, 91, 15)]

# initial position and velocity; acceleration
x0, y0 = 0., 0.
v0, alpha0 = 5, params
ax, ay = -drag_, -drag_ - grav_
print("parameters =", params)


# calculate simulation time and set time slices
sim_times = 2. * np.array(v0) * np.sin(np.radians(alpha0)) / grav_
print("sim times =", sim_times)

Projectile.time_slices = 160
print("time slices =", Projectile.time_slices)


# create all projectiles to animate
balls = Projectile(x0, y0, v0, alpha0[2])

# generate their respective trajectories
balls.kinematics(ax, ay) 

x,y = balls.get_trajectory()


plt.plot(x,y)


# print some relevant values to check correcteness
#print(balls.get_maxes()) 
#
#[print(ball.get_trajectory()) for ball in balls]


# create animator handle object for animation
framer = Animator(balls)

# set up animation
#framer.set_animation()

# carry out animation (default parameters)
#framer.run_animation(inval=1000*Projectile.sim_time/Projectile.time_slices)