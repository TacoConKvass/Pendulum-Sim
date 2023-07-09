# Pendulum Simulation
from time import sleep as wait

from math import radians as rad, sin

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
        distanceDifferenceAfterSwing = -1 * oppositeDirection * abs(self.angle/10)
        oppositeStopPoint = oppositeDirection * (abs(self.angle) - distanceDifferenceAfterSwing)

        while oppositeStopPoint != 0:
            self.angle += oppositeDirection * 1
            self.updateDynamic()
            print(self.updateDynamic())

            if self.angle == oppositeStopPoint:
                oppositeDirection *= -1
                oppositeStopPoint = oppositeDirection * (abs(self.angle) - distanceDifferenceAfterSwing)
                print([oppositeDirection, oppositeStopPoint])

            wait(0.2)
        

object = pendulum(2, 30)
object.runPendulum(20)
