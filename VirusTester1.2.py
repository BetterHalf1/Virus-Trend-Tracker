# -*- coding: utf-8 -*-
"""
Author: Kenneth Tang (Better Half)
Feb 27 2020

"""
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import math

class Virus:
    
    def __init__(self, name, R0, Lower0):
        self.n = name
        self.c = R0
        self.l = Lower0
        
    def __repr__(self):
        
        return "Virus name: " + self.n + "\nR0: " + str(self.c)

    
def infectedCycle(lst, initPop, cycles):
    '''Compares viruses of different R0 values based on number of infected
        at a given cycle.'''
    
    cycleCounter = -1
    vCounter = 0
    # Prints data on console
    print("\nInitial size of infected: " + str(initPop) +"\n")
    for i in range(len(lst)):
        print(str(lst[i]) + "\n")
        
    # Prints calculated data on console    
    for i in range(cycles + 1):  
        cycleCounter += 1
        print("Cycle " + str(cycleCounter) + ": ", end="", flush=True)
        
        for j in range(len(lst)):
            vCounter += 1
            pop = round(initPop * math.pow(lst[j].c, cycleCounter))
            
            if vCounter == len(lst):
                print(lst[j].n + " " + f"{pop:,d}" + "\n")
                vCounter = 0
                
            else: 
                print(lst[j].n + " " + f"{pop:,d}" + ", ", end="", flush=True)
                
             
    # Data for plotting
    c = np.arange(cycles - 2, cycles + .1, .1)
    fig, ax = plt.subplots()
    #plt.subplots(cycles, 1, sharex=True, figsize=(6, 6))
    ax.grid()
    ax.set(xlabel='Cycle (c)', ylabel='Infected (i)',
            title='Virus Infection (R0) Comparison')
    
    # Plots and initializes legend
    colCounter = 0
    colorList = ['blue', 'orange', 'green', 'red']
    legend = [None] * len(lst)
    
    for j in range(len(lst)):
        # Plot
        
        ub = initPop * lst[j].c**c
        #lb = initPop * lst[j].l**c
        ax.plot(c, ub)
        #ax.plot(c, lb)
        
        #ax.fill_between(c, lb, ub)
        plt.annotate('%0.2f (i)' % ub.max(), xy=(1, ub.max()), xytext=(8, 0), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points')
        # Legend
        x = mpatches.Patch(color=colorList[colCounter], label=lst[j].n + \
            " (" + str(lst[j].c) + ")")
        legend[colCounter] = x
        colCounter += 1
         
    plt.legend(handles=legend)
    fig.savefig("test.png")
    plt.show()       


x = Virus("COVID-19", 4.08, 2.4)    
y = Virus("SARS", 2.75, .70)
z = Virus("Smallpox", 7.00, 5.00)
test = Virus("Potion", .60, .5)

lst = [x, y, z]
infectedCycle(lst, 1.0, 5)
    
def rounder(x):
    if round(x) - int(x) + 1 == .5:
        return round(x) + 1
    else:
        return round(x)
    


