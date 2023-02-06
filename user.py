from board import Board
import pygame
from pygame import Vector2
from direction import Direction
import itertools


class User(Board):

    def __init__(self, x, y, pixels, border, main_window) -> None:
        super().__init__(x, y, pixels, border, main_window)
        self.user_shots = []
        self.user_ships = []
        self.user_hits = []
        self.user_temp_ship = []
        self.user_ships_len = [2, 4, 6, 8, 8]
        self.user_temp_orientation = Direction.SOUTH

    def intro_completed(self):
        if not self.user_temp_ship:
            return True

    def temp_ship_control(self):
        if self.user_ships_len:
            if not self.user_temp_ship:
                selected_ship = self.user_ships_len.pop()
                self.ship_creation(selected_ship)
        if not self.user_ships_len and not self.user_temp_ship:
            return False

    def ship_creation(self, ship_len):
        if not self.user_temp_ship:
            self.user_temp_ship = [Vector2(7, 7+i) for i in range(ship_len)]

    def intro_draw(self):
        overlapping_vectors = self.temp_ship_over_plaved_ship()
        self.surface_init('Grey')
        for ship in self.user_ships:
            self.draw(ship, 'Blue')
        if not self.whole_on_board():
            self.draw(self.user_temp_ship, 'Red')
        else:
            self.draw(self.user_temp_ship, 'Green')

        if overlapping_vectors:
            self.draw(overlapping_vectors, 'Yellow')
        self.update()

    def move_ship(self, event):
        if self.user_temp_ship:
            return_ship = []

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    for vector in self.user_temp_ship:
                        return_ship.append(vector + Vector2(0, -1))
                if event.key == pygame.K_DOWN:
                    for vector in (self.user_temp_ship):
                        return_ship.append(vector + Vector2(0, 1))
                if event.key == pygame.K_LEFT:
                    for vector in self.user_temp_ship:
                        return_ship.append(vector + Vector2(-1, 0))
                if event.key == pygame.K_RIGHT:
                    for vector in self.user_temp_ship:
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

                self.user_temp_ship = return_ship

    def rotate(self):
        self.user_temp_orientation = self.user_temp_orientation.next
        snake_head_x, snake_head_y = self.user_temp_ship[0]

        if self.user_temp_orientation == Direction.NORTH:
            self.user_temp_ship = [Vector2(snake_head_x, snake_head_y-i)
                                   for i in range(len(self.user_temp_ship))]
        if self.user_temp_orientation == Direction.EAST:
            self.user_temp_ship = [Vector2(snake_head_x + i, snake_head_y)
                                   for i in range(len(self.user_temp_ship))]
        if self.user_temp_orientation == Direction.SOUTH:
            self.user_temp_ship = [Vector2(snake_head_x, snake_head_y+i)
                                   for i in range(len(self.user_temp_ship))]
        if self.user_temp_orientation == Direction.WEST:
            self.user_temp_ship = [Vector2(snake_head_x-i, snake_head_y)
                                   for i in range(len(self.user_temp_ship))]

    def whole_on_board(self):
        if self.user_temp_ship:
            ship_head_x, ship_head_y = self.user_temp_ship[0]
            ship_tail_x, ship_tail_y = self.user_temp_ship[-1]

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

    def temp_ship_over_plaved_ship(self):
        overlapped_vectors = []
        placed_vectors = None
        if len(self.user_ships) >= 1:
            placed_vectors = itertools.chain.from_iterable(self.user_ships)
        if placed_vectors:
            for vec in placed_vectors:
                if vec in self.user_temp_ship:
                    overlapped_vectors.append(vec)
        return overlapped_vectors

    def ship_placement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                ship = self.user_temp_ship
                if self.whole_on_board():
                    if not self.temp_ship_over_plaved_ship():
                        self.user_ships.append(ship)
                        self.user_temp_ship = []
                        self.user_temp_orientation = Direction.SOUTH
