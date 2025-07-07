import math
def triangle(b,h):
	return b*h/2
def rectangle(b,h):
	return b*h
def circle(r):
	return math.pi*(r**2)
def donut(outerR,innerR):
    return circle(outerR)-circle(innerR)
#print("Hello")
