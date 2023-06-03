import math
import pygame as pg
from settings import *


class Bird:
    def __init__(self, brain):
        self.image = pg.image.load("./images/bird.png").convert_alpha()
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.x = 50
        self.y = HALF_HEIGHT
        self.alive = True
        self.vel = 0
        self.acc = 0
        self.max_vel = 80
        self.jump = 10
        self.rect = pg.Rect(self.x + 5, self.y + 5, self.width - 10, self.height - 10)

        self.score = 0
        self.state = (12, 13, 0)
        self.brain = brain

    def flap(self):
        self.acc = 0
        self.vel = 0
        self.apply_force(-self.jump)

    def apply_force(self, force, dt=1):
        self.acc += force
        self.vel += self.acc
        self.vel *= 0.9
        self.y += min(self.vel, self.max_vel) * dt

    def check_edges(self):
        if self.y < 10:
            self.y = 10
        elif self.y + self.height > HEIGHT:
            return True
        return False

    def check_collision(self, pipes):
        return True if self.rect.collidelistall(pipes) else False

    def update(self, pipe, dt):
        failed = False
        if self.check_edges() or self.check_collision(pipe.pipes):
            failed = True
            self.alive = False
        if self.check_score(pipe.goal):
            self.update_score()
        self.apply_force(GRAVITY, dt)
        self.rect.y = self.y + 5
        if failed:
            self.update_brain(self.brain.punish, pipe.pipes)
        else:
            self.update_brain(self.brain.reward, pipe.pipes)

    def update_brain(self, reward, pipes):
        prv_state = self.state
        x_state = min(WIDTH, pipes[0].x)
        x_state = math.floor(x_state / 40) + 2
        y_delta = pipes[0].y - self.y
        if y_delta < 0:
            y_delta = int(abs(y_delta) + HEIGHT * 0.8)
        y_state = math.floor(y_delta / 40)
        action = self.brain.select_action(self.state)
        self.state = (x_state, y_state, action)
        self.brain.updateQ(prv_state, self.state, reward)
        if action == 1:
            self.flap()

    def draw(self):
        SCREEN.blit(self.image, (self.x, self.y))
        self.display_score()

    def check_score(self, goal):
        return abs(self.x - goal) < 1

    def update_score(self):
        self.score += 1

    def display_score(self):
        score_text = f"Score: {self.score}"
        text_render = font.render(score_text, True, WHITE)
        SCREEN.blit(text_render, (WIDTH - 110, 15))
