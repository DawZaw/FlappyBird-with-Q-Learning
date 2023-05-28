import pygame as pg
from settings import *

class Bird:
    def __init__(self):
        self.x = 150
        self.y = half_height
        self.r = 20
        self.vel = 0
        self.acc = 0
        self.max_vel = 10
        self.jump = 150

    def handle_events(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                self.apply_force(-self.jump)
                self.acc = 0
                self.vel = 0

    def apply_force(self, force):
        self.acc += force
        self.vel += self.acc
        self.y += min(self.vel, self.max_vel)

    def update(self, dt):
        self.apply_force(gravity)

    def draw(self):
        return pg.draw.circle(SCREEN, YELLOW, (self.x, self.y), self.r)