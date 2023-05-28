import pygame as pg
from game import Game
from settings import *

game = Game()


def main():
    while True:
        clock.tick(FPS)
        dt = clock.tick_busy_loop(FPS) / FPS
        fps = str(int(clock.get_fps()))
        pg.display.set_caption("Flappy Bird | FPS: " + fps)
        game.handle_events()
        game.update(dt)
        game.draw()


if __name__ == "__main__":
    main()
else:
    pass
