#Pendulum Sim - better edition (I hope)

### IMPORTANT NOTES ###
# The pendulums weight is a perfect sphere
# The weights diameter is directly proportional (1:1) to its mass
# While the pendulum is in the position of balance, the bottom of the weight is located 0.3m above ground

'''
Units used for:
 - mass -> kilograms
 - length -> meters
 - force -> newtons
 - angle -> degrees
'''

from math import cos, sin, pi, floor, radians as rad
from time import sleep as wait
import turtle as t

t.bgcolor('black')
t.ht()
t.speed(100)
t.tracer(2)

EARTH_ACC = 9.8203 #Value taken form wikipedia.org/wiki/Gravity_of_Earth
VECTOR_DRAW_MODIFIER = 0.4 #Value changing the length of the vectors drawn
AIR_DENSITY = 1.225 #approximate value at sea level
DRAG_COEFFICIENT = 0.47 #Approximate for a sphere

class Vector2:
    def __init__(self, x, y, color='red'):
        self.x = x
        self.y = y
        self.color = color

    def __add__(self, secondVector):
        self.x += secondVector.x
        self.y += secondVector.y
        return self

    def __sub__(self, secondVector):
        self.x -= secondVector.x
        self.y -= secondVector.y
        return self

    def __mul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        return self

    def __eql__(self, secondVector):
        if self.x == secondVector.x and self.y == secondVector.y:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.x}, {self.y}'

    def draw(self):
        t.pencolor(self.color)
        t.pensize(2)

        oldPos = (t.position()[0], t.position()[1])
        
        t.setpos(t.position()[0] + self.x, t.position()[1] + self.y)
        t.seth(t.towards(oldPos) + 180)
        t.stamp()

        t.pu()
        t.setpos(oldPos)
        t.pd()

        t.pencolor('white')
        
class Pendulum:
    def __init__(self, length, mass, angle = 0):
        #Static
        self.length = length
        self.lengthToDraw = self.length * 100
        self.mass = mass
        
        self.gravitationForceValue = self.mass * EARTH_ACC
        self.gravitationForceToDraw = Vector2(0, self.gravitationForceValue) * -1 * VECTOR_DRAW_MODIFIER

        self.distanceToFloorInPositionOfBalance = 0.3 + (mass/2)/100 #From the center of the weight, in meters
        self.distanceFromPivotToFloor = self.length * 100 + self.distanceToFloorInPositionOfBalance * 100

        #Dynamic
        self.angle = angle
        
        self.tensionForceValue = self.gravitationForceValue * cos(rad(self.angle))
        self.tensionForceToDraw = Vector2(self.tensionForceValue * cos(rad(90 + self.angle)), self.tensionForceValue * sin(rad(90 + self.angle)), 'green') * VECTOR_DRAW_MODIFIER

        self.accelerationValue = self.gravitationForceValue * sin(rad(self.angle))
        self.accelerationToDraw = Vector2(self.accelerationValue * cos(rad(self.angle)), self.accelerationValue * sin(rad(self.angle)), 'yellow') * -1 * VECTOR_DRAW_MODIFIER

        self.velocityValue = 0 * sin(rad(self.angle))
        self.velocityToDraw = Vector2(self.velocityValue * cos(rad(self.angle)), self.velocityValue * sin(rad(self.angle)), 'blue') * -1 * VECTOR_DRAW_MODIFIER
        
    def draw(self, drawForces=True):
        t.pencolor('white')
        t.pensize(1)
        self.drawFloor()
        
        t.pu()
        t.setpos(0, 0)
        t.dot(5, 'white')
        t.pd()

        t.seth(self.angle - 90)
        t.fd(self.lengthToDraw)
        t.dot(self.mass, 'white')

        if drawForces:     
            self.gravitationForceToDraw.draw()
            self.tensionForceToDraw.draw()

            if self.accelerationValue != 0:
                self.accelerationToDraw.draw()

            if self.velocityValue != 0:
                self.velocityToDraw.draw()

        #print(f'Gravitation: {self.gravitationForceToDraw},\tValue: {self.gravitationForceValue}')
        #print(f'Tension: {self.tensionForceToDraw},\tValue: {self.tensionForceValue}')
        print(f'Acceleration: {self.accelerationToDraw},\tValue: {self.accelerationValue}')
        print(f'Velocity: {self.velocityToDraw},\tValue: {self.velocityValue}')
        print(f'Angle: {self.angle}')
        print()

    def drawFloor(self):
        t.pu()
        t.setpos(0, -self.distanceFromPivotToFloor)
        t.seth(0)
        t.pd()


        t.fd(self.lengthToDraw)
        t.bk(self.lengthToDraw * 2)

    def updateDynamic(self):
        self.tensionForceValue = self.gravitationForceValue * cos(rad(self.angle))
        self.tensionForceToDraw = Vector2(self.tensionForceValue * cos(rad(90 + self.angle)), self.tensionForceValue * sin(rad(90 + self.angle)), 'green') * VECTOR_DRAW_MODIFIER

        self.accelerationValue = self.gravitationForceValue * sin(rad(self.angle))
        self.accelerationToDraw = Vector2(self.accelerationValue * cos(rad(self.angle)), self.accelerationValue * sin(rad(self.angle)), 'yellow') * -1 * VECTOR_DRAW_MODIFIER

        if self.accelerationValue > 0:
            if self.velocityValue < 0:
                self.velocityValue = (self.velocityValue + self.accelerationValue * (floor(AIR_DENSITY / DRAG_COEFFICIENT)) * 0.7)
            else:
                self.velocityValue = (self.velocityValue + self.accelerationValue)

        else:
            if self.velocityValue > 0:
                self.velocityValue = (self.velocityValue + self.accelerationValue * (floor(AIR_DENSITY / DRAG_COEFFICIENT)) * 0.7)
            else:
                self.velocityValue = (self.velocityValue + self.accelerationValue)

        self.velocityToDraw = Vector2(self.velocityValue * cos(rad(self.angle)), self.velocityValue * sin(rad(self.angle)), 'blue') * -1 * VECTOR_DRAW_MODIFIER

    def updateFrame(self):
        swinging = True
        
        while swinging:
            
            t.clear()
            self.angle += self.velocityToDraw.x / 100
            self.updateDynamic()
            self.draw(False)
            wait(0.01)

            if abs(self.velocityValue) < 0.1 and abs(self.accelerationValue) < 0.8:
                swinging = False

        t.clear()
        self.draw(False)

object1 = Pendulum(2, 30, 40)
object1.draw()
object1.updateFrame()
