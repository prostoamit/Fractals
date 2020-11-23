import pygame
import sys
from math import pi, sin, cos, sqrt
from objects.Branch import Branch

SIZE = WIDTH, HEIGHT = 800, 600
CENTRE = CENTRE_X, CENTRE_Y = WIDTH // 2, HEIGHT // 2

black = 0, 0, 0
white = 255, 255, 255

start_len = 200

angle = pi / 3


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    working = True

    branch = Branch(screen, white, (CENTRE_X, HEIGHT), start_len, 40, angle)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False

        screen.fill(black)

        branch.draw(1)

        pygame.display.flip()

    sys.exit()


if __name__ == '__main__':
    main()