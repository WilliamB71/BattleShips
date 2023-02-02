from board import Board
from direction import Direction
from pygame import Vector2
import pygame
import random
import itertools


class Ai(Board):
    def __init__(self, x, y, pixels, border, main_window) -> None:
        super().__init__(x, y, pixels, border, main_window)
        self.ai_shots = []
        self.ai_ships = []
        self.ai_hits = []
        self.ai_temp_ship = []
        self.ai_ships_len = [5, 4, 3, 2, 1]
        self.ai_temp_orientation = Direction.NORTH

    def ai_place_ships(self):
        for ship_len in self.ai_ships_len:
            placed = False
            while not placed:
                position = []
                direction = Direction(random.randint(0, 3))
                start_vector = Vector2(random.randint(
                    0, self.x-1), random.randint(0, self.y-1))

                if direction == Direction.NORTH:
                    position = [Vector2(start_vector.x, start_vector.y-i)
                                for i in range(ship_len)]
                if direction == Direction.EAST:
                    position = [Vector2(start_vector.x + i, start_vector.y)
                                for i in range(ship_len)]
                if direction == Direction.SOUTH:
                    position = [Vector2(start_vector.x, start_vector.y+i)
                                for i in range(ship_len)]
                if direction == Direction.WEST:
                    position = [Vector2(start_vector.x-i, start_vector.y)
                                for i in range(ship_len)]
                
                if position:
                    ship_head_x, ship_head_y = position[0]
                    ship_tail_x, ship_tail_y = position[-1]

                    if ship_head_x >= self.x or ship_head_x < 0:
                        continue
                    if ship_head_y >= self.y or ship_head_y < 0:
                        continue
                    if ship_tail_x >= self.x or ship_tail_x < 0:
                        continue
                    if ship_tail_y >= self.y or ship_tail_y < 0:
                        continue
                    else:
                        if self.ai_ships:
                            placed_vectors = itertools.chain.from_iterable(self.ai_ships)
                            for vector in placed_vectors:
                                if vector in position:
                                    continue
                    self.ai_ships.append(position)
                    placed = True





border = 0.5
game_window_x = 16
game_window_y = 32
pixels = 30

pygame.init()
game_window = pygame.display.set_mode(((game_window_x+border)*pixels, (game_window_y+border)*pixels))


test = Ai(game_window_x, game_window_x, pixels, border, game_window)
pygame.init()
test.ai_place_ships()


