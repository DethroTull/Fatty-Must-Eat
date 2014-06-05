from kivy.core.image import Image
from kivy.graphics.texture import Texture
from kivy.properties import ListProperty, BoundedNumericProperty, VariableListProperty
from kivy.uix.widget import Widget

import math
import random
import array

class RayMap(Widget):
    def __init__(self):
        self.mapSize = 32
        self.wallGrid = [] #VariableListProperty(self.mapSize * self.mapSize)
        self.skybox = Image.load('./deathvalley_panorama.jpg')
        self.wallTexture = Image.load('./wall_texture.jpg')
        self.light = 0

    def get(self, x, y):
        x = math.floor(x)
        y = math.floor(y)
        if x < 0 or x > (self.mapSize - 1) or y < 0 or y > (self.mapSize -1):
            return -1

        return self.wallGrid[y * self.mapSize + x]

    def randomize(self):
        for i in range(0, self.mapSize * self.mapSize):
            self.wallGrid.append(random.randrange(0,1))

    def cast(self, point, angle, range):
        this = self
        sin = math.sin(angle)
        cos = math.cos(angle)
        noWall.length2 = 'Infinity'

    def ray(self, angle, origin):
        stepX = step(sin, cos, origin.x, origin.y)
        stepY = step(cos, sin, origin.y, origin.x, True)
        if stepX.length2 <  stepY.length:
            nextStep = self.inspect(stepX, 1, 0, origin.distance, stepX.y)
        else:
            nextStep = self.inspect(stepY, 0, 1, origin.distance, stepY.x)

        if nextStep.distance > self.range:
            return [origin]

        return 
    
    def update(self, seconds):
        if self.light > 0:
            self.light = math.ceil(self.light - 10 * seconds)
        elif random.random() * 5 < seconds:
            self.light = 2

          
            
    
class RayRay(Widget):
    def __init__(self, origin, angle):
        
        stepX = step(sin, cos, origin.x, origin.y)
        stepY = step(cos, sin, origin.y, origin.x, True)
        if stepX.length2 <  stepY.length:
            nextStep = self.inspect(stepX, 1, 0, origin.distance, stepX.y)
        else:
            nextStep = self.inspect(stepY, 0, 1, origin.distance, stepY.x)

        if nextStep.distance > self.range:
            return ListProperty(origin)

        return -1

    def step(rise, run, x, y, inverted):
        if run == 0: return self.noWall
        if run > 0:
            dx = math.floor(x + 1) - x
        else:
            dx = math.ceil(x - 1) - x

        dy = dx * (rise / run)

        if inverted:
            x = y + dy
            y = x + dx
        else:
            x = x + dx
            y = y + dy

        length2 = dx * dx + dy * dy

        return { 'x': x, 'y': y, 'length2': length2 }

    def inspect(step, shiftX, shiftY, distance, offset):
        if self.cos < 0:
            dx = shiftX
        else:
            dx = 0

        if self.sin < 0:
            dy = shiftY
        else:
            dy = 0

        step.height = self.this.get(step.x - dx, step.y - dy)
        step.distance = distance + math.sqrt(step.length2)
        if shiftX:
            if self.cos < 0:
                step.shading = 2
            else:
                step.shading = 0

        else:
            if self.sin < 0:
                step.shading = 2
            else:
                step.shading = 1
        step.offset = offset - math.floor(offset)
        return step

    
