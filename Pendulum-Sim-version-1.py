# Pendulum Simulation - hardcoded edition
import turtle as t
from time import sleep as wait
from math import radians as rad, sin, pi as pi

t.bgcolor('grey')
t.pencolor('white')
t.speed(1000)
t.tracer(2)
t.ht()

'''
Units used for:
 - mass -> kilograms
 - length -> meters
 - force -> newtons
 - energy -> juls
 - angle -> degrees
 '''

## SPECIAL NOTES ##
#The bottom of the pendulums weight, while in position of balance, is located 0.3m above the floor
#The diameter of the pendulums weight is directly proportional to the weights mass

earthAcc = 9.8203

class pendulum:
    def __init__(self, lengthInMeters, mass, angle = 0):
        #Static properties
        self.length = lengthInMeters
        self.mass = mass
        self.forceOfGravity = self.mass * earthAcc
        self.distanceToFloorInPositionOfBalance = 0.3 + (mass/2)/100 #From the center of the weight, in meters
        self.distanceFromAnchorToFloor = self.length * 100 + self.distanceToFloorInPositionOfBalance * 100
        self.period = 2 * pi * (self.length / earthAcc)**(1/2)
        self.swingsPerMinute = round(60 / self.period)

        #Dynamic properties
        self.angle = angle
        self.distanceToFloor = self.calculateDistanceToFloor()
        self.potentialEnergy = self.mass * earthAcc * self.distanceToFloor

    def __str__(self):
        return f'This is a pendulum. \nIts arm is {self.length}m long. \nIts weights mass is equal to {self.mass}kg. {self.updateDynamic()}'

    def updateDynamic(self):
        self.distanceToFloor = self.calculateDistanceToFloor()
        self.potentialEnergy = self.mass * earthAcc * self.distanceToFloor
        return f'\nIts current distance to the floor is around {round(self.distanceToFloor, 4)}m. \
\nIts current angle relative to the position of balance is {self.angle} degrees. \nIts current gravitational potential energy is equal to {round(self.potentialEnergy, 4)}J \n'
        
    def calculateDistanceToFloor(self):
        #Angle naming explained on github
        alpha = self.angle
        beta = (180 - self.angle) / 2
        gamma = 90 - beta

        sinOfAlpha = sin(rad(alpha))
        sinOfBeta = sin(rad(beta))
        sinOfGamma = sin(rad(gamma))

        if sinOfBeta != 0:
            distanceFromPositionOfBalance = (self.length * sinOfAlpha) / sinOfBeta
        else:
            distanceFromPositionOfBalance = self.length * 2

        deltaHeightRelativeToPositionOfBalance = sinOfGamma * distanceFromPositionOfBalance
        distanceToFloor = deltaHeightRelativeToPositionOfBalance + self.distanceToFloorInPositionOfBalance

        return distanceToFloor

    def runPendulum(self, angle):
        self.angle = angle
        self.updateDynamic()
        
        oppositeDirection = -1 * (self.angle/abs(self.angle)) # -1 -> swing left; 1 -> swing right
        distanceDifferenceAfterSwing = round(-1 * oppositeDirection * abs(self.angle / self.swingsPerMinute))
        oppositeStopPoint = -self.angle

        print([oppositeDirection, distanceDifferenceAfterSwing, oppositeStopPoint])
        
        swinging = True

        while swinging:
            
            if oppositeDirection == 1 and self.angle >= oppositeStopPoint:
                oppositeDirection *= -1
                oppositeStopPoint = oppositeDirection * (abs(self.angle) - distanceDifferenceAfterSwing)
                print([oppositeDirection, distanceDifferenceAfterSwing, oppositeStopPoint])

            if oppositeDirection == -1 and self.angle <= oppositeStopPoint:
                oppositeDirection *= -1
                oppositeStopPoint = oppositeDirection * (abs(self.angle) - distanceDifferenceAfterSwing)
                print([oppositeDirection, distanceDifferenceAfterSwing, oppositeStopPoint])
            
            self.angle += oppositeDirection
            print(self.updateDynamic())

            self.drawSelf()
            wait(0.01)

            if oppositeStopPoint == 0 and self.angle == 0:
                swinging = False

    def drawSelf(self):
        t.clear()
        self.drawFloor()
        t.pu()
        t.setpos(0, 0)
        t.pd()
        t.setheading(self.angle - 90)
        t.fd(self.length * 100)
        t.dot(self.mass, 'white')

    def drawFloor(self):
        t.pu()
        t.setpos(0, -1 * self.distanceFromAnchorToFloor)
        t.pd()
        t.setheading(0)
        t.fd(self.length * 100)
        t.bk(self.length * 100 * 2)
        

object = pendulum(2, 30)
#object.drawSelf()
object.runPendulum(20)
