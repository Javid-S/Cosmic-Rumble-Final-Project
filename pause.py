# pause.py
# Shows a pause menu when the player presses 'P'

import pygame

def draw_pause_menu(screen, font):
    """
    Displays the pause menu with 3 options:
    ▶ Resume - to go back to the game
    ▶ Quit World - exit the current world/game
    ▶ Quit Game - closes the whole game
    """

    # Fill the screen with dark gray color
    screen.fill((30, 30, 30))

    # Menu options and what they do
    options = [
        ("▶ Resume", "resume"),
        ("▶ Quit World", "quit_world"),
        ("▶ Quit Game", "quit_game")
    ]

    # Draw all the menu options
    rects = []
    y = 200  # starting Y position
    for text, action in options:
        rendered = font.render(text, True, (255, 255, 255))  # white text
        rect = rendered.get_rect(center=(screen.get_width() // 2, y))  # center it
        screen.blit(rendered, rect)
        rects.append((rect, action))  # store button area + action
        y += 60  # move down for next option

    pygame.display.update()

    # Now wait for user input
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit_game"  # if window is closed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                return "resume"  # resume if 'P' is pressed again
            if event.type == pygame.MOUSEBUTTONDOWN:
                for rect, action in rects:
                    if rect.collidepoint(event.pos):
                        return action  # return the action for clicked button
