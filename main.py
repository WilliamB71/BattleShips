import pygame
from board import Board
from pygame import Vector2
from user import User
vect_list = [Vector2(0,0), Vector2(0, 1), Vector2(0, 3), Vector2(3, 3)]

border = 0.5
game_window_x = 16
game_window_y = 32
pixels = 30

pygame.init()
game_window = pygame.display.set_mode(((game_window_x+border)*pixels, (game_window_y+border)*pixels))

b = User(game_window_x, game_window_x, pixels=pixels, border=border, main_window=game_window)
b.surface_init(colour_key='Grey')
# b.draw(vect_list, 'Red')
# b.update(top=False)

# _surface_a = pygame.Surface((8*50,8*50))
# _surface_a.fill((255,0,0))

# _surface_b = pygame.Surface((8*50, 8*50))
# _surface_b.fill((0,255,0))

# game_window.blit(_surface_a, (12.5,418.75))
# game_window.blit(_surface_b, (12.5, 6.25))
# pygame.display.update()
# a = pygame.Surface(10, 20)

clock = pygame.time.Clock()

while True:
    
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    
        b.ship_init(7)
        b.ship_mover(event)
    
    clock.tick(10)
    

    