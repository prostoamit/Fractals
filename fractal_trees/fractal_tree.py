import pygame
import sys
from math import pi, sin, cos, sqrt
from objects.branch import Branch
from objects.slider import Slider

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

# Angle between branches


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Fractal tree")
    working = True

    recursion_count = 15
    angle = 25

    recursion_slider = Slider(screen, white, (100, HEIGHT - 20), 100, (1, 17))
    angle_slider = Slider(screen, white, (100, HEIGHT - 40), 100, (10, 180))

    branch = Branch(screen, white, (CENTRE_X, HEIGHT), start_len, length_fraction, angle)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
            recursion_count = recursion_slider.move(event)
            angle = angle_slider.move(event)

        screen.fill(black)

        recursion_slider.render()
        angle_slider.render()

        branch.draw(recursion_count, angle)

        pygame.display.flip()

    sys.exit()


if __name__ == '__main__':
    main()
