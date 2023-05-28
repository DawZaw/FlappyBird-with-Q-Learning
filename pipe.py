import pygame as pg
from random import randint
from settings import *


class Pipe:
    def __init__(self) -> None:
        self.width = 150
        self.spacing = 150
        self.y = randint(250, HEIGHT - 250)
        self.x = WIDTH

    def update(self):
        self.x -= 4

    def draw(self):
        pg.draw.rect(
            SCREEN,
            GREEN,
            (
                self.x,
                0,
                self.width,
                self.y - self.spacing,
            ),
        )
        pg.draw.rect(
            SCREEN,
            GREEN,
            (
                self.x,
                self.y + self.spacing,
                self.width,
                HEIGHT - self.y,
            ),
        )
