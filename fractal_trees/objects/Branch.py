import pygame
from math import sin, cos, pi


class Branch:
    def __init__(self, screen, color, begin, len, len_step, angle):
        self.screen = screen
        self.color = color

        self.b_x, self.b_y = self.begin = begin

        self.angle = angle

        self.e_x = self.b_x - int(len * cos(self.angle))
        self.e_y = self.b_y - int(len * sin(self.angle))
        self.end = self.e_x, self.e_y

        self.len = len
        self.len_step = len_step

    def draw(self, min_l):
        pygame.draw.line(self.screen, self.color, self.begin, self.end, 3)
        if self.len - self.len_step >= min_l:
            branch_l = Branch(self.screen, self.color, self.end, self.len - self.len_step, self.len_step, self.angle + self.len_step/100)
            branch_l.draw(min_l)

            branch_r = Branch(self.screen, self.color, self.end, self.len - self.len_step, self.len_step, pi - (self.angle + self.len_step/100))
            branch_r.draw(min_l)
