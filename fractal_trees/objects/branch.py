import pygame
from math import sin, cos, pi, radians


class Branch:
    def __init__(self, screen, color, begin, length, length_fraction, angle):

        # screen - pygame display
        # color - branch color
        #
        # begin - branch starting position
        # end - branch ending position
        #
        # length - branch length
        #
        # len_fraction - changing branch length with every layer
        #
        # angle - angle between branches

        self.screen = screen
        self.color = color

        self.begin = self.begin_x, self.begin_y = begin

        self.length = length
        self.length_fraction = length_fraction

        self.angle = angle

        self.vector = pygame.math.Vector2()  # creating a 2D vector to calculate points with rotation
        self.vector.x, self.vector.y = 0, self.length

        # creating ending position
        self.end = self.end_x, self.end_y = int(self.begin_x - self.vector.x), int(self.begin_y - self.vector.y)

    def rotate_branch(self, angle):
        self.vector = self.vector.rotate(angle)  # rotates vector counterclockwise by the given angle

        # changing ending point values
        self.end = self.end_x, self.end_y = int(self.begin_x - self.vector.x), int(self.begin_y - self.vector.y)

    def draw(self, recursion, angle):
        pygame.draw.line(self.screen, self.color, self.begin, self.end, 1)  # draws a branch
        self.angle = angle

        if recursion > 1:

            # creating right branch object
            right_branch = Branch(self.screen, self.color, self.end, self.length / self.length_fraction, self.length_fraction, self.angle)
            right_branch.vector = self.vector
            right_branch.vector.scale_to_length(right_branch.length)

            # rotating the branch vector to get coordinates
            right_branch.rotate_branch(right_branch.angle)

            # recursive method calling
            right_branch.draw(recursion - 1, self.angle)

            # same
            left_branch = Branch(self.screen, self.color, self.end, self.length / self.length_fraction, self.length_fraction, self.angle)
            left_branch.vector = self.vector
            left_branch.rotate_branch(-left_branch.angle)
            left_branch.vector.scale_to_length(left_branch.length)

            left_branch.draw(recursion - 1, self.angle)
