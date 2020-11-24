import pygame
import sys
from math import pi, sin, cos, sqrt
from objects.Branch import Branch

SIZE = WIDTH, HEIGHT = 1080, 720
CENTRE = CENTRE_X, CENTRE_Y = WIDTH // 2, HEIGHT // 2

black = 0, 0, 0
white = 255, 255, 255

# Tree characteristics

# Starting length
start_len = HEIGHT // 5

# Length change ratio
length_fraction = 1.3

# Count of layers
recursion_count = 15

# Angle between branches
angle = 25


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    working = True

    branch = Branch(screen, white, (CENTRE_X, HEIGHT), start_len, length_fraction, angle)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False

        screen.fill(black)

        branch.draw(recursion_count)

        pygame.display.flip()

    sys.exit()


if __name__ == '__main__':
    main()
