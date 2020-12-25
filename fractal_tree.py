import pygame
import sys

from objects import FractalTree

# from objects.fractal_tree import FractalTree

SIZE = WIDTH, HEIGHT = 1080, 720
CENTRE = CENTRE_X, CENTRE_Y = WIDTH // 2, HEIGHT // 2

black = 0, 0, 0
white = 255, 255, 255

# Starting length
start_len = HEIGHT // 5

# Length change ratio
length_fraction = 1.3


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Fractal tree")
    working = True

    tree = FractalTree(screen, white, (CENTRE_X, HEIGHT), start_len, length_fraction, start_len, SIZE)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
            tree.process_logic(event)

        screen.fill(black)

        tree.render()

        pygame.display.flip()

    sys.exit()


if __name__ == '__main__':
    main()
