import pygame as pg

pg.init()
pg.font.init()

clock = pg.time.Clock()
font = pg.font.SysFont("rockwell", 24, bold=True)

SIZE = WIDTH, HEIGHT = 400, 500
SCREEN = pg.display.set_mode(SIZE)
FPS = 60
HALF_WIDTH = WIDTH / 2
HALF_HEIGHT = HEIGHT / 2
SCREEN_CENTER = HALF_WIDTH, HALF_HEIGHT

GRAVITY = 1

WHITE = (255, 255, 255)
