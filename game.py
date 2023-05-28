import sys
import pygame as pg
from bird import Bird
from pipe import Pipe
from background import Background

from settings import *


class Game:
    def __init__(self):
        self.background = Background()
        self.bird = Bird()
        self.pipe = Pipe()
        self.pipes = []

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            self.bird.handle_events(event)
            if event.type == pg.KEYDOWN:
                if not self.bird.alive and event.key == pg.K_SPACE:
                    self.__init__()

    def update(self, dt):
        self.pipes = [self.pipe.bot_rect, self.pipe.top_rect]
        self.background.update(self.bird, dt)
        self.pipe.update(self.bird, dt)
        self.bird.update(self.pipes, self.pipe.goal, dt)

    def draw(self):
        self.background.draw()
        self.pipe.draw()
        self.bird.draw()
        pg.display.flip()
