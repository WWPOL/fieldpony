#!/usr/bin/env python2.7
import pyglet
from pyglet.window import key
from pyglet.window import mouse
import sys

# Internal imports.
from objects import Stage
from objects import Paddle
from physics import Vector
from meta import Player
from graphics import graphics_render
from graphics import graphics_resize
from hand import HandJob
from client import Connection, ClientSession 

window = pyglet.window.Window(width=1280, height=720)
hand = HandJob()
stage = Stage()

def start_match():
    player1 = Player()
    player2 = Player()

def render(self):
    graphics_render(hand, stage)

@window.event
def on_draw():
    pass

@window.event
def on_resize(width, height):
    return graphics_resize(width, height)

@window.event
def on_key_press(symbol, modifier):
    if symbol == key.ESCAPE:
        pyglet.app.exit()

@window.event
def on_mouse_motion(x,y,dx,dy):
	global mouseX, mouseY
	mouseX = x - window.width/2
	mouseY = y - window.height/2

pyglet.clock.schedule_interval(render, 1/120.0)
connection = Connection(stage, sys.argv[1])
client_session = ClientSession(connection)
client_session.start()
pyglet.clock.schedule_interval(client_session.send_coordinates, 1/20.0)
client_session.send_coordinates()
pyglet.app.run()
