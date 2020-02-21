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
        
        self.y = self.y[self.y>=0]
     
        self.x = self.x[:len(self.y)]
    
    def get_trajectory(self):
        # returns values of x(t) and y(t)
        #self.y = self.y[self.y>=0]
     
        #preguntar que hacer para llegar al 0, si forzarlo o que putas.
        #self.x = self.x[:len(self.y)]
        
        return self.x, self.y
    







class Animator:
    # choose your favorite colors!
    cls = ['green', 'red', 'blue', 'cyan', 'magenta', 'black']
    
    def __init__(self, objs):
        # objects to be animated and its total number
        self.artists = objs
        self.number = len(self.artists)
        
        # instance variables to None; properly set in set_animation
        self.fig = self.ax = self.line = self.point = None
        self.time_template = self.time_text = None
        self.xdata = self.ydata = None
    
    def set_animation(self):
        # plot setup: axis, labels, title, grid, etc.
        
        #ax = plt.axes(autoscale_on=False, xlim=(0, x_max), ylim=(0, y_max)) # use los 
        #limites que le estoy pasando
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], lw=2)
        
        self.xdata, self.ydata = [], []

        self.ax.set(xlabel='x [a.u.]', ylabel='y [a.u.]', title='Projectile motion')
        self.ax.grid()
        # line points setup, time template, points on top of axes

    def init(self,idx):
        # function used to draw a clear frame
        self.ax.set_ylim(0,max(self.artists[idx].y))
        self.ax.set_xlim(0,max(self.artists[idx].y))
        del self.xdata[:]
        del self.ydata[:]
        self.line.set_data(self.xdata, self.ydata)
            
        return self.line,
    
    def animate(self, idx):
        # function to call at each frame
        """t, y = idx
        self.xdata.append(t)
        self.ydata.append(y)
        xmin, xmax = ax.get_xlim()
        print("animate")
        if t >= xmax:
            self.ax.set_xlim(xmin, 2*xmax)
            self.ax.figure.canvas.draw()
            self.line.set_data(self.xdata, self.ydata)"""
        
       # print(type(self.artists))
            
        self.xdata=self.artists[idx].x
        
        self.ydata=self.artists[idx].y
        
        self.ax.set_xlim(0,max(self.xdata))
        
        self.ax.set_ylim(0,max(self.ydata))
        
        self.line.set_data(self.xdata,self.ydata)
        print("hola")
        return self.line,
       # return self.line, self.point, self.time_text
    
    
    def run_animation(self, inval=10, rep=True):
        # set up to perform animation
        for idx in range (self.number):
            
            ani = animation.FuncAnimation(self.fig, self.animate(idx),
                                      range(len(self.artists[idx].y)),
                                      repeat=rep, interval=inval,
                                      init_func=self.init(idx))

            name = "prueba" + str(idx)+".gif"
            ani.save(name)
        #plt.show()


"""ani = animation.FuncAnimation(self.fig, self.animate,
                                      range(len(self.artists.y)-1),
                                      repeat=rep, interval=inval,
                                      init_func=self.init)"""
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
balls = [Projectile(x0, y0, v0, val) for val in alpha0]

# generate their respective trajectories
[ball.kinematics(ax, ay) for ball in balls]

# print some relevant values to check correcteness
#[print(ball.get_maxes()) for ball in balls]
#[print(ball.get_trajectory()) for ball in balls]

# create animator handle object for animation
framer = Animator(balls)

# set up animation
framer.set_animation()


# carry out animation (default parameters)
#framer.run_animation(1000*Projectile.sim_time/Projectile.time_slices)

framer.run_animation()

#https://codingcompetitions.withgoogle.com/


