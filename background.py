import pygame as pg

from settings import *


class Background:
    def __init__(self):
        self.img = pg.image.load("./images/background.png")
        self.width = self.img.get_width()
        self.rect = self.img.get_rect()
        self.speed = 15
        self.scroll = 0
        self.panels = 2

    def draw(self):
        for i in range(self.panels):
            SCREEN.blit(self.img, (i * self.width + self.scroll - self.width, 0))

    def update(self, bird, dt):
        if bird.alive:
            self.scroll = (self.scroll - self.speed * dt) % self.width
