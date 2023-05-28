import sys
import pygame as pg
from bird import Bird
from pipe import Pipe

from settings import *


class Game:
    def __init__(self):
        self.bird = Bird()
        self.pipe = Pipe()
        self.pipes = []

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            self.bird.handle_events(event)

    def update(self, dt):
        self.pipe.update()
        self.bird.update(dt)

    def draw(self):
        SCREEN.fill(BLACK)
        self.pipe.draw()
        self.bird.draw()
        pg.display.flip()
