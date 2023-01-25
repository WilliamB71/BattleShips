from board import Board
import pygame
from pygame import Vector2
from direction import Direction


class User(Board):

    def __init__(self, x, y, pixels, border, main_window) -> None:
        super().__init__(x, y, pixels, border, main_window)
        self.user_ships = []
        self.user_hits = []
        self.temp_ship = []
        self.orientation = Direction.SOUTH

    def ship_init(self, ship_len):
        if not self.temp_ship:
            self.temp_ship = [Vector2(0, i) for i in range(ship_len)]

    def ship_mover(self, event):
        self.move_ship(event)
        self.surface_init('Grey')
        if not self.whole_on_board():
            self.draw(self.temp_ship, 'Red')
        else:
            self.draw(self.temp_ship, 'Green')
        self.update()

    def move_ship(self, event):
        return_ship = []

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                for vector in self.temp_ship:
                    return_ship.append(vector + Vector2(0, -1))
            if event.key == pygame.K_DOWN:
                for vector in (self.temp_ship):
                    return_ship.append(vector + Vector2(0, 1))
            if event.key == pygame.K_LEFT:
                for vector in self.temp_ship:
                    return_ship.append(vector + Vector2(-1, 0))
            if event.key == pygame.K_RIGHT:
                for vector in self.temp_ship:
                    return_ship.append(vector + Vector2(1, 0))
            
            if event.key == pygame.K_r:
                self.rotate()

        if return_ship:
            ship_head_x, ship_head_y = return_ship[0]
            ship_tail_x, ship_tail_y = return_ship[-1]

            if ship_head_x >= self.x or ship_head_x < 0:
                if ship_tail_x >= self.x or ship_tail_x < 0:
                    return

            if ship_head_y >= self.y or ship_head_y < 0:
                if ship_tail_y >= self.y or ship_tail_y < 0:
                    return

            self.temp_ship = return_ship

    def rotate(self):
        self.orientation = self.orientation.next
        snake_head_x, snake_head_y = self.temp_ship[0]

        if self.orientation == Direction.NORTH:
            self.temp_ship = [Vector2(snake_head_x, snake_head_y-i)
                              for i in range(len(self.temp_ship))]
        if self.orientation == Direction.EAST:
            self.temp_ship = [Vector2(snake_head_x + i, snake_head_y)
                              for i in range(len(self.temp_ship))]
        if self.orientation == Direction.SOUTH:
            self.temp_ship = [Vector2(snake_head_x, snake_head_y+i)
                              for i in range(len(self.temp_ship))]
        if self.orientation == Direction.WEST:
            self.temp_ship = [Vector2(snake_head_x-i, snake_head_y)
                              for i in range(len(self.temp_ship))]

    def whole_on_board(self):
        ship_head_x, ship_head_y = self.temp_ship[0]
        ship_tail_x, ship_tail_y = self.temp_ship[-1]

        if ship_head_x >= self.x or ship_head_x < 0:
            return False
        if ship_head_y >= self.y or ship_head_y < 0:
            return False
        if ship_tail_x >= self.x or ship_tail_x < 0:
            return False
        if ship_tail_y >= self.y or ship_tail_y < 0:
            return False
        else:
            return True
