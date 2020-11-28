import pygame


class Slider:
    def __init__(self, screen, color, position, length, interval):

        # ---------|-----
        #  ^       ^
        # base   slider
        #
        # screen - pygame surface
        # color - slider color
        #
        # position - sliders base CENTRE
        # length - sliders base length
        #
        # interval - tuple of beginning and ending of values

        self.screen = screen
        self.color = color

        self.base_length = length

        # makes center coordinates the coordinates of the left corner
        self.base_begin_position = self.b_x, self.b_y = position[0] - self.base_length // 2, position[1]

        self.base_end_position = self.e_x, self.e_y = self.b_x + self.base_length, self.b_y

        # slider position
        self.slider_pos = self.slider_x, self.slider_y = position

        # to locate mouse position
        self.mouse_click = False

        self.interval = interval

    def move(self, event):

        # getting mouse position event
        if event.type == pygame.MOUSEMOTION:
            # moves the slider while holding down the left mouse button
            if self.mouse_click:
                # checks if the slider is out of range
                if self.b_x <= event.pos[0] <= self.e_x:
                    # moves slider
                    self.slider_x = event.pos[0]

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_click = True
        if event.type == pygame.MOUSEBUTTONUP:
            self.mouse_click = False

        # returns a value depending on the slider position
        return int(((self.interval[1] - self.interval[0]) * (self.slider_x - self.b_x)) / self.base_length)

    def render(self):
        pygame.draw.line(self.screen, self.color, self.base_begin_position, self.base_end_position, 2)
        pygame.draw.line(self.screen, self.color, (self.slider_x, self.slider_y + 5), (self.slider_x, self.slider_y - 5), 2)
