# player.py
# Handles the player’s movement and keeps them inside the screen

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

# Speed at which player moves
PLAYER_SPEED = 5

def handle_player_movement(keys, player_rect):
    """
    This function checks which arrow keys are pressed and moves the player accordingly.
    """
    if keys[pygame.K_UP]:        # Move up
        player_rect.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:      # Move down
        player_rect.y += PLAYER_SPEED
    if keys[pygame.K_LEFT]:      # Move left
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:     # Move right
        player_rect.x += PLAYER_SPEED

def clamp_player(player_rect):
    """
    This function makes sure the player doesn’t move outside the screen.
    """
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > SCREEN_HEIGHT:
        player_rect.bottom = SCREEN_HEIGHT
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > SCREEN_WIDTH:
        player_rect.right = SCREEN_WIDTH
