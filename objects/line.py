import pygame


class Line:
    def __init__(self, screen, color, begin_position, end_position, width):
        self.screen = screen
        self.color = color

        self.begin_position = begin_position
        self.end_position = end_position

        self.width = width

    def render(self):
        pygame.draw.line(self.screen, self.color, self.begin_position, self.end_position, self.width)