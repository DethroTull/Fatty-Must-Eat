from kivy.core.image import Image
from map import RayMap
import math
import random

class RayPlayer:

    CIRCLE = math.pi * 2		
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.weapon = Image('./knife_hand.png')
        self.paces = 0

    def rotate(self, angle):
        self.direction = (self.direction + angle + CIRCLE) % (CIRCLE)

    def walk(self, distance, map):
        dx = math.cos(self.direction) * distance
        dy = math.sin(self.direction) * distance
        if map.get(self.x + dx, self.y) <= 0:
            self.x += dx

        if map.get(self.x, self.y + dy) <= 0:
            self.y += dy

        self.paces += distance

    def update(self, controls, map, seconds):
        if controls.left:
            self.rotate(-math.pi * seconds)
        if controls.right:
            self.rotate(math.pi * seconds)
        if controls.forward:
            self.walk(3 * seconds, map)
        if controls.backward:
            self.walk(-3 * seconds, map)
            
                        
