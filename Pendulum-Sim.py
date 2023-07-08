# Pendulum Simulation
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
        return f'This is a pendulum. \nIts arm is {self.length}m long. \nIts weights mass is equal to {self.mass}kg. \nIts current distance to the floor is around {round(self.distanceToFloor, 4)}m. \
\nIts current angle relative to the position of balance is {self.angle} degrees. \nIts current gravitational potential energy is equal to {round(self.potentialEnergy, 4)}N'
        
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

object = pendulum(2, 30)
print(object)
