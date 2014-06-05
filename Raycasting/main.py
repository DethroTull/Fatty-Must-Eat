from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, DictProperty, ListProperty
from kivy.core.window import WindowBase
from map import RayMap
from player import RayPlayer

import math


#g_player = Player(15.3, -1.2, math.pi * 0.3)
resolution = 320
fov = math.pi * 0.4
CIRCLE = math.pi * 2



class RayControls(Widget):
    def __init__(self):
        pass

class RayCamera(Widget):
    def __init__(self, game, resolution, fov):
        self.width = game.width
        self.height = game.height
        self.resolution = resolution
        self.spacing = self.width / resolution
        self.fov = fov
        self.range = 8
        self.lightRange = 5
        self.scale = (self.width + self.height) / 1200

    def render(self, player, map):
        player = ObjectProperty(None)
        map = ObjectProperty(None)
        self.drawSky(player.direction, map.skybox, map.light)
        #self.drawColumns(player, map)
        #self.drawWeapon(player.weapon, player.paces)

    def drawSky(self, direction, sky, ambient):
        width = self.width * (CIRCLE / self.fov)
        

class RayGame(Widget):
  
    def update(self, dt):
       pass
        
class RayApp(App):
    def build(self):
        game = RayGame()
        
        self.g_player = RayPlayer(15.3, -1.2, math.pi * 0.3)
        self.g_map = RayMap()
        self.g_controls = RayControls()      
        self.g_camera = RayCamera(game, resolution, fov)

        self.g_map.randomize()
        
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        
        return game

    def update(self, dt):
        self.g_map.update(dt)
        self.g_player.update(self.g_controls.states, self.g_map, dt)       
        self.g_camera.render(self.g_player, self.g_map)       

if __name__ == '__main__':
    RayApp().run()
