import pygame
from game_master import GameMaster

border = 0.5
game_window_x = 12
game_window_y = 24
pixels = 30

pygame.init()
game_window = pygame.display.set_mode(
    ((game_window_x+border)*pixels, (game_window_y+border)*pixels))

b = GameMaster(game_window_x, game_window_x, pixels=pixels,
               border=border, main_window=game_window)
b.surface_init(colour_key='Grey')
b.ai_place_ships()

clock = pygame.time.Clock()
game_started = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

            if not game_started:
                b.move_ship(event)
                b.ship_placement(event)

    if not game_started:
        b.temp_ship_control()
        b.intro_draw()
        game_started = b.intro_completed()

    game_started = b.intro_completed()

    if game_started:
        b.gameplay_draw_bottom()
        b.gameplay_draw_top()

    b.play(game_started)

    clock.tick(30)
