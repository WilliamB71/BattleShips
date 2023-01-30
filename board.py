import pygame
from pygame import Vector2


class Board:
    def __init__(self, x, y, pixels, border, main_window) -> None:
        self.x = x
        self.y = y
        self.pixels = pixels
        self.border = border
        self.main_window = main_window
        self.colours = {'Blue': (0, 0, 255), 'Red': (
            255, 0, 0), 'Green': (0, 255, 0), 'Grey': (192, 192, 192), 'Yellow': (255, 191, 0)}
        self.board_window = pygame.Surface(
            (self.x*self.pixels, self.y*self.pixels))

    def surface_init(self, colour_key: str):
        self.board_window.fill(color=self.colours[colour_key])


    def draw(self, vector_list: list, colour_key: str):
        for vector in vector_list:
            pygame.draw.rect(self.board_window, color=self.colours[colour_key], rect=pygame.Rect(
                (vector.x*self.pixels, vector.y*self.pixels, self.pixels, self.pixels)))

    def update(self, top=True):
        _x = (self.border*self.pixels) / 2
        _y = (self.border*self.pixels) / 4

        if not top:
            _y += (self.y*self.pixels) + (2*_y)

        self.main_window.blit(self.board_window, (_x, _y))
        self.main_window
        pygame.display.update()
