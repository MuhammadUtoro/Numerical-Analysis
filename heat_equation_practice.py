import numpy as np
import math
import matplotlib
from matplotlib import pyplot as mplot

# Practicing the 1D heat equation with fourth-order approximation for the spatial derivative
# using the same input with the previous example

def fourth_order_app(deltaT, numX, alpha, tMax, temp1, temp2):
    deltaX = 1.0/(numX-1)

    #The constants of proportionality
    C = alpha*deltaT/(12*(deltaX*deltaX))

    #Initial Condition
    x = np.linspace(0,1,numX)
    y = temp1*np.ones(x.shape)

    #Boundary Condition
    y[-2:] = temp2
    mplot.plot(x,y,'-', label='Initial Condition',linewidth=3)  
    time = 0
    count = 0
    numTimeSteps = (np.rint(tMax/deltaT)).astype(int)
    pausePercentages = np.array([1,4,10,20,100])

    pauseTimeSteps = np.rint(numTimeSteps*0.01*pausePercentages).astype(int)

    while time < tMax:
        yOld = np.copy(y)
        y[2:-2] = yOld[2:-2] + C*(-yOld[4:]+16*yOld[3:-1]-30*yOld[2:-2]+16*yOld[1:-3]-yOld[:-4])

        time = time + deltaT
        count = count + 1
        if count in pauseTimeSteps:
            index = np.where(pauseTimeSteps == count)
            mplot.plot(x,y,'-', label='%s%% of tMax' %pausePercentages[index][0],linewidth=3)
    mplot.plot(x,y,'-', label='Initial Condition',linewidth=3)
    mplot.title('Temperature Distribution across Time', fontsize=24)
    mplot.xlim(0,1)
    mplot.xticks(fontsize=14)
    mplot.ylim(temp1,temp2)
    mplot.yticks(fontsize=14)
    mplot.grid()
    mplot.ylabel('Temperature ($^{o}C$)', fontsize=18, loc='center',rotation=90)
    mplot.xlabel('X (m)', fontsize=18)
    mplot.legend(prop={'size': 14})
    mplot.show(block=True)

if __name__ == '__main__':

    numX = 101
    tMax = 10
    alpha = 0.2 #Plexiglass

    # Boundary Conditions
    temp1 = 20
    temp2 = 100
    deltaT = 0.0001
    
    fourth_order_app(deltaT,numX,alpha,tMax,temp1,temp2)