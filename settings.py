import pygame as pg

pg.init()
pg.font.init()

clock = pg.time.Clock()
font = pg.font.SysFont("rockwell", 32, bold=True)

SIZE = WIDTH, HEIGHT = 400, 500
SCREEN = pg.display.set_mode(SIZE)
FPS = 120
HALF_WIDTH = WIDTH / 2
HALF_HEIGHT = HEIGHT / 2
SCREEN_CENTER = HALF_WIDTH, HALF_HEIGHT

GRAVITY = 1

BLACK = (0, 0, 0)
YELLOW = (255, 200, 20)
GREEN = (0, 200, 0)
WHITE = (255, 255, 255)
