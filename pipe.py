import pygame as pg
from random import randint
from settings import *


class Pipe:
    def __init__(self) -> None:
        self.top_img = pg.image.load("./images/top_pipe.png").convert_alpha()
        self.bot_img = pg.image.load("./images/bottom_pipe.png").convert_alpha()
        self.width = self.top_img.get_width()
        self.height = self.top_img.get_height()
        self.spacing = 150
        self.y = randint(50, 300)
        self.x = WIDTH
        self.speed = 50
        self.goal = self.x + self.width / 2
        self.top_rect = pg.Rect(self.x, self.y - self.height, self.width, self.height)
        self.bot_rect = pg.Rect(self.x, self.y + self.spacing, self.width, self.height)

    def update(self, bird, dt):
        if bird.alive:
            self.x -= self.speed * dt
            if self.x + self.width < 0:
                self.reset()
            self.goal = self.x + self.width / 2
            self.top_rect.x = self.x
            self.bot_rect.x = self.x

    def reset(self):
        self.y = randint(50, 300)
        self.top_rect.y = self.y - self.height
        self.bot_rect.y = self.y + self.spacing
        self.x = WIDTH

    def draw(self):
        SCREEN.blit(
            self.top_img, (self.x, self.y - self.height, self.width, self.height)
        )
        SCREEN.blit(
            self.bot_img, (self.x, self.y + self.spacing, self.width, self.height)
        )
