import pygame as pg

pg.init()
pg.font.init()

clock = pg.time.Clock()
font = pg.font.SysFont("Arial", 12)

SIZE = WIDTH, HEIGHT = 1440, 900
SCREEN = pg.display.set_mode(SIZE)
FPS = 144
half_width = WIDTH / 2
half_height = HEIGHT / 2
screen_center = half_width, half_height

gravity = 0.1

BLACK = (0, 0, 0)
YELLOW = (255, 200, 20)
GREEN = (0, 200, 0)