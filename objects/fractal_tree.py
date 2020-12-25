import pygame

from .branch import Branch
from .slider import Slider


class FractalTree:
    def __init__(self, screen, color, begin, length, length_fraction, start_len, SIZE):

        self.start_len = start_len

        self.color = color

        self.SIZE = self.WIDTH, self.HEIGHT = SIZE

        self.recursion_count = 10
        self.angle = 30

        self.branch = Branch(screen, self.color, (self.WIDTH // 2, self.HEIGHT), start_len, length_fraction, self.angle)

        self.recursion_slider = Slider(screen, self.color, (100, self.HEIGHT - 20), 100, (1, 17))
        self.angle_slider = Slider(screen, self.color, (100, self.HEIGHT - 40), 100, (10, 180), 30)

    def process_logic(self, event):
        self.recursion_count = recursion_count = self.recursion_slider.move(event)
        self.angle = angle = self.angle_slider.move(event)

    def render(self):
        self.recursion_slider.render()
        self.angle_slider.render()
        self.branch.render(self.recursion_count, self.angle)