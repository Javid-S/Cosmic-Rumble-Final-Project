# menu.py
# This file shows all the different screens before starting the actual game:
# title screen, world selection, and main menu

import pygame
from worlds import get_world_list

# Load background image once

# Helper function to draw glowing text
def draw_glowing_text(screen, text, font, color, glow_color, x, y, center=False):
    base = font.render(text, True, color)
    glow = font.render(text, True, glow_color)
    rect = base.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)

    # Slightly smaller glow
    for dx in [-1, 1]:
        for dy in [-1, 1]:
            screen.blit(glow, rect.move(dx, dy))

    screen.blit(base, rect)
    return rect

# Helper function to draw shadowed text
def draw_text_with_shadow(screen, text, font, text_color, shadow_color, x, y, center=False):
    text_surface = font.render(text, True, text_color)
    shadow_surface = font.render(text, True, shadow_color)
    rect = text_surface.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)

    screen.blit(shadow_surface, rect.move(2, 2))
    screen.blit(text_surface, rect)
    return rect

def title_screen(screen, font):
    # Load and draw background (after display is initialized)
    title_bg = pygame.image.load("assets/default/title_bg.png").convert()
    bg_scaled = pygame.transform.scale(title_bg, screen.get_size())
    screen.blit(bg_scaled, (0, 0))

    # Draw glowing SELECT WORLD in center of screen
    select_rect = draw_glowing_text(screen, "SELECT WORLD", font, (255, 215, 0), (255, 230, 100), 400, 300, center=True)

    draw_text_with_shadow(screen, "The worlds have shattered. Chaos has begun.", font,
                      (200, 100, 255), (20, 0, 40), 400, 560, center=True)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit", None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if select_rect.collidepoint(event.pos):
                    return "world_select", None

# World select screen
def world_select_screen(screen, font):
    select_world_bg = pygame.image.load("assets/default/select_world_bg.png").convert()

    screen.blit(pygame.transform.scale(select_world_bg, screen.get_size()), (0, 0))

    draw_glowing_text(screen, "CHOOSE YOUR WORLD", font, (255, 255, 255), (50, 50, 50), 400, 80, center=True)

    world_list = get_world_list()
    rects = []
    y = 180
    for world in world_list:
        label = world.replace('_', ' ').title()
        rect = draw_text_with_shadow(screen, label, font, (255, 215, 0), (0, 0, 0), 400, y, center=True)
        rects.append((rect, world))
        y += 60

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit", None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for rect, world in rects:
                    if rect.collidepoint(event.pos):
                        return "main_menu", world

# Main menu screen
def main_menu_screen(screen, font):
    screen.fill((0, 0, 0))
    draw_text_with_shadow(screen, "MAIN MENU", font, (255, 255, 255), (0, 0, 0), 400, 80, center=True)
    options = [
        ("New Game", "new"),
        ("Change World", "change"),
        ("Exit Game", "quit")
    ]

    rects = []
    y = 160
    for text, action in options:
        rect = draw_text_with_shadow(screen, text, font, (0, 255, 100), (0, 0, 0), 400, y, center=True)

        rects.append((rect, action))
        y += 60

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for rect, action in rects:
                    if rect.collidepoint(event.pos):
                        return action
