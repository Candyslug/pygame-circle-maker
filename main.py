import pygame as pg
from math import sin, cos, radians

def main():
    steps = int(input("Number of steps: "))

    pg.init()
    screen = pg.display.set_mode((500, 500))
    running = True

    while running:
        screen.fill((0, 0, 0, 255))

        # --------------------------- #

        center = screen.get_size()[0] / 2, screen.get_size()[1] / 2
        radius = screen.get_size()[0] * 0.4
        for i in range(steps):
            ang = (360 / steps) * i
            x = (cos(radians(ang)) * radius) + center[0]
            y = (sin(radians(ang)) * radius) + center[1]

            nang = (360 / steps) * (i + 1)
            nx = (cos(radians(nang)) * radius) + center[0]
            ny = (sin(radians(nang)) * radius) + center[1]

            pg.draw.line(screen, (100, 240, 100), (x, y), (nx, ny))

        dotSize = 10
        pg.draw.rect(screen, (240, 100, 100), ((center[0] - dotSize / 2, center[1] - dotSize / 2, dotSize, dotSize)))
        pg.display.flip()

        # --------------------------- #
        for event in pg.event.get():
            if event.type ==  pg.QUIT:
                running = False

    pg.quit()

if __name__ == '__main__':
    main()
