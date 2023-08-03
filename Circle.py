#Calculating the Area and Circumference of a Circle
import numpy as np

def circle_Area(r):
    circle_Area = np.pi*r**2
    return circle_Area

def circle_Circum(r):
    circle_Circum = 2*np.pi*r
    return circle_Circum

radius = float(input("Enter a value for the radius: "))

area = circle_Area(radius)
circum = circle_Circum(radius)

print("The area with a radius of " + str(radius) + " is: " + str(area))
print("The circumference with a radius of " + str(radius) + " is: " + str(circum))

