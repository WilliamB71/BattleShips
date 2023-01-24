from board import Board
import pygame
from pygame import Vector2

class User(Board):
    def __init__(self, x, y, pixels, border, main_window) -> None:
        super().__init__(x, y, pixels, border, main_window)
        self.user_ships = []
        self.user_hits = []
        self.temp_ship = []

    
    def ship_init(self, ship_len):
        if not self.temp_ship:
            self.temp_ship = [Vector2(0, i) for i in range(ship_len)]


    def ship_mover(self, event):
        self.move_ship(event)
        self.surface_init('Grey')
        self.draw(self.temp_ship, 'Red')
        self.update()
        


    
    def move_ship(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                for i, vector in enumerate(self.temp_ship):
                    self.temp_ship[i] = vector + Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                for i, vector in enumerate(self.temp_ship):
                    self.temp_ship[i] = vector + Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                for i, vector in enumerate(self.temp_ship):
                    self.temp_ship[i] = vector + Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                for i, vector in enumerate(self.temp_ship):
                    self.temp_ship[i] = vector + Vector2(1, 0)

        
    




            




    