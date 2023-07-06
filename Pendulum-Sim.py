import turtle as t
from time import sleep as wait
from math import sin, radians

#Assumption 1: While the pendulum is in rest, the bottom of the weigth
#is located 30 units above the floor

t.ht()
t.tracer(5)
t.bgcolor('grey')
t.pencolor('white')

class pendulum:

    def __init__(self, length, mass, angle):
        #Static properties
        self.length = length
        self.mass = mass
        self.distanceToFloorFromAnchor = self.length + self.mass/2 + 30 
        self.distanceToFloorInRest = self.mass/2 + 30 #This represent the distance of the center of mass from the floor

        #Dynamic properties
        self.angle = angle

    def drawSelf(self):
        t.setheading(0)
        t.pu()
        t.setpos(0, 0)
        t.pd()

        t.dot(10, 'white')
        t.rt(90)
        t.lt(self.angle)
        t.fd(self.length)
        t.dot(self.mass, 'white')
        t.bk(self.length)

    def drawFloor(self):
        t.pu()
        t.setpos(0, -1 * self.distanceToFloorFromAnchor)
        t.setheading(0)
        t.pd()
        t.fd(self.length * 2)
        t.bk(self.length * 4)
        t.fd(self.length * 2)

def calculateDistanceToFloor(current, **draw : bool):
    if draw:
        test = pendulum(current.length, current.mass, 0)
        test.drawSelf()
    
    alpha = current.angle
    if alpha < 0:
        alpha *= -1
        
    beta = (180 - alpha)/2
    gamma = 90 - beta
    
    sineOfAlpha = round(sin(radians(alpha)), 4)
    sineOfBeta = round(sin(radians(beta)), 4)
    sineOfGamma = round(sin(radians(gamma)), 4)

    if sineOfBeta != 0:
        distanceBetweenWeights = (current.length * sineOfAlpha)/sineOfBeta
    else:
        distanceBetweenWeights = current.length * 2

    deltaHeightRelativeToWeightInRest = sineOfGamma * distanceBetweenWeights
    currentDistanceToFloor = current.distanceToFloorInRest + deltaHeightRelativeToWeightInRest
    print(currentDistanceToFloor)

def updateFrame(target):
    target.drawFloor()
    target.drawSelf()
    if target.angle != 0:
        target.angle -= 1

    
    wait(0.2)
    t.clear()

def run():
    main = pendulum(200, 30, 20)

    calculateDistanceToFloor(main)

    while True:
        updateFrame(main)

run()
