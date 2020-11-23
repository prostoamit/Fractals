import pygame
from math import sin, cos, pi


class Branch:
    def __init__(self, screen, color, begin, length, len_step, angle):

        # screen - pygame display
        # color - branch color
        #
        # begin - branch starting position
        # end - branch ending position
        #
        # length - branch length
        #
        # len_step - changing git branch length with every layer
        #
        # angle - angle between branches

        self.screen = screen
        self.color = color

        self.begin_x, self.begin_y = self.begin = begin

        self.angle = angle

        self.end_x = self.begin_x - int(length * cos(self.angle))
        self.end_y = self.begin_y - int(length * sin(self.angle))
        self.end = self.end_x, self.end_y

        self.length = length
        self.len_step = len_step

    def draw(self, min_l):
        pygame.draw.line(self.screen, self.color, self.begin, self.end, 3)
        if self.length - self.len_step >= min_l:
            branch_l = Branch(self.screen, self.color, self.end, self.length - self.len_step, self.len_step, self.angle + self.len_step / 100)
            branch_l.draw(min_l)

            branch_r = Branch(self.screen, self.color, self.end, self.length - self.len_step, self.len_step, pi - (self.angle + self.len_step / 100))
            branch_r.draw(min_l)