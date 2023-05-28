import sys
import pygame as pg
from bird import Bird
from pipe import Pipe
from background import Background
from qlearn import QLearn

from settings import *


class Game:
    def __init__(self):
        self.qlearn = QLearn(650, 2)
        self.background = Background()
        self.bird = Bird(self.qlearn)
        self.pipe = Pipe()
        self.high_score = 0
        self.generation = 0
        self.pipes = []

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            self.bird.handle_events(event)

    def update(self, dt):
        self.pipes = [self.pipe.bot_rect, self.pipe.top_rect]
        self.background.update(self.bird, dt)
        self.pipe.update(self.bird, dt)
        self.bird.update(self.pipes, self.pipe.goal, dt)
        if not self.bird.alive:
            self.generation += 1
            if self.bird.score > self.high_score:
                self.high_score = self.bird.score
            self.new_game()

    def draw(self):
        self.background.draw()
        self.pipe.draw()
        self.bird.draw()
        self.display_text()
        pg.display.flip()

    def new_game(self):
        # self.background = Background()
        self.bird = Bird(self.qlearn)
        self.pipe = Pipe()
        # self.pipes = []

    def display_text(self):
        gen_text = f"Generation: {self.generation}"
        hs_text = f"Highscore: {self.high_score}"
        text_render = font.render(gen_text, True, WHITE)
        SCREEN.blit(text_render, (15, 15))
        text_render = font.render(hs_text, True, WHITE)
        SCREEN.blit(text_render, (15, 40))
