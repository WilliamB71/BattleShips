import random
import itertools
import pygame
from pygame import Vector2
from ai import Ai
from user import User
from board import Board


class GameMaster(Ai, User, Board):
    def __init__(self, x, y, pixels, border, main_window) -> None:
        super().__init__(x, y, pixels, border, main_window)

    def user_shoot(self):
        x_border, y_border = (self.border*self.pixels) / \
            2, (self.border*self.pixels)/4
        mouse_position_x, mouse_position_y = pygame.mouse.get_pos()
        x_block = (mouse_position_x + x_border - self.pixels) / self.pixels
        y_block = (mouse_position_y + y_border - self.pixels) / self.pixels

        vector = Vector2(round(x_block, 0), round(y_block, 0))

        ai_ships = list(itertools.chain.from_iterable(self.ai_ships))

        if vector in self.user_shots:
            return False
        else:
            self.user_shots.append(vector)
            if vector in ai_ships:
                self.user_hits.append(vector)
            return True

    def game_over_check(self):
        ai_ships = list(itertools.chain.from_iterable(self.ai_ships))
        user_ships = list(itertools.chain.from_iterable(self.user_ships))

        if len(ai_ships) == len(self.user_hits):
            return True
        if len(user_ships) == len(self.ai_hits):
            return True
        else:
            return False

    def ai_take_shot(self):
        while True:
            vector = Vector2(random.randint(0, self.x-1),
                             random.randint(0, self.y-1))

            if vector not in self.ai_shots:
                self.ai_shots.append(vector)
                if vector in itertools.chain.from_iterable(self.user_ships):
                    self.ai_hits.append(vector)
                    print('Hit - One of your ships has been struck.')
                else:
                    print('your opponent takes a shot but misses')
                break

    def play(self, game_started):
        if game_started:
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > 486 or mouse_pos[-1] > 482:
                    pygame.event.wait()
                else:
                    if self.user_shoot():
                        self.gameplay_draw_top()
                        if self.game_over_check():
                            print('GAME OVER - YOU WIN!')
                            pygame.time.wait(900)
                            pygame.quit()
                        pygame.time.wait(300)
                        self.ai_take_shot()
                        self.gameplay_draw_bottom()
                        if self.game_over_check():
                            print('GAME OVER AI WINS')
                            pygame.time.wait(900)
                            pygame.quit()

    def gameplay_draw_top(self):
        self.surface_init('Grey')
        self.draw(self.user_shots, 'Dark Grey')
        self.draw(self.user_hits, 'Green')
        self.update()

    def gameplay_draw_bottom(self):
        self.surface_init('Grey')
        self.draw(itertools.chain.from_iterable(self.user_ships), 'Blue')
        self.draw(self.ai_shots, 'Dark Grey')
        self.draw(self.ai_hits, 'Red')
        self.update(False)
