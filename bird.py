import pygame as pg
from settings import *


class Bird:
    def __init__(self):
        self.x = 50
        self.y = HALF_HEIGHT
        self.alive = True
        self.score = 0
        self.vel = 0
        self.acc = 0
        self.max_vel = 100
        self.jump = 15
        self.image = pg.image.load("./images/bird.png").convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pg.Rect(self.x + 5, self.y + 5, self.width - 10, self.height - 10)

    def handle_events(self, event):
        if event.type == pg.KEYDOWN:
            if self.alive and event.key == pg.K_SPACE:
                self.acc = 0
                self.vel = 0
                self.apply_force(-self.jump)

    def apply_force(self, force, dt=1):
        self.acc += force
        self.vel += self.acc
        self.vel *= 0.9
        self.y += min(self.vel, self.max_vel) * dt

    def check_edges(self):
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > HEIGHT:
            self.y = HEIGHT - self.height
            self.vel = 0
            self.acc = 0

    def check_collision(self, pipes):
        return True if self.rect.collidelistall(pipes) else False

    def update(self, pipes, goal, dt):
        self.check_edges()
        if self.check_collision(pipes):
            self.alive = False
        if self.check_score(goal):
            self.update_score()
        self.apply_force(GRAVITY, dt)
        self.rect.y = self.y + 5

    def draw(self):
        SCREEN.blit(self.image, (self.x, self.y))
        self.display_score()

    def check_score(self, goal):
        return abs(self.x - goal) < 0.01

    def update_score(self):
        self.score += 1

    def display_score(self):
        text_render = font.render(str(self.score), True, WHITE)
        SCREEN.blit(text_render, (HALF_WIDTH - 16, 30))
