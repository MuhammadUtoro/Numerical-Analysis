#Using function to calculate x_pos and y_pos
def x(v0x,t):
    x = v0x*t
    return x

def y(v0y,t):
    g = 9.81
    y = v0y-0.5*g*t**2
    return y

#The output can also be combined
def xy(v0x,v0y,time):
    g = 9.81
    return v0x*time, v0y-0.5*g*time**2

inp_time = float(input("Enter a time value: "))
inp_v0x = float(input("Enter an inital velocity in x direction: "))
inp_v0y = float(input("Enter an intial velocity in y direction:  "))

xpos,ypos = xy(inp_v0x,inp_v0y,inp_time)

print(xpos,ypos)

# x_pos = x(inp_v0x, inp_time)
# y_pos = y(inp_v0y, inp_time)

# print(x_pos)
# print(y_pos)