import pygame


class Line:
    def __init__(self, screen, color, begin_position, end_position, width):
        self.screen = screen
        self.color = color

        self.begin_position = self.b_x, self.b_y = begin_position
        self.end_position = self.e_x, self.e_y = end_position

        self.vector = pygame.math.Vector2((self.e_x - self.b_x, self.e_y - self.b_y))

        self.width = width

    def rotate(self, angle):
        self.vector.rotate(angle)

    def sclae(self, length):
        self.vector.scale_to_length(length)

    def render(self):
        pygame.draw.line(self.screen, self.color, self.begin_position, self.end_position, self.width)