import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from settings import ENEMY_WIDTH, ENEMY_HEIGHT

def create_enemies(count=5):
    enemies = []
    enemy_speeds = []
    for _ in range(count):
        x = random.randint(SCREEN_WIDTH + 100, SCREEN_WIDTH + 400)
        y = random.randint(50, SCREEN_HEIGHT - 50)
        speed = random.randint(2, 4)  # ⚠️ Still above 1.2 bg scroll
        enemy = pygame.Rect(x, y, 50, 50)
        enemies.append(enemy)
        enemy_speeds.append(speed)
    return enemies, enemy_speeds



def move_enemies(enemies, speeds):
    # Ensure enemies and speeds lists are always the same length
    if len(enemies) != len(speeds):
        print("⚠️ Mismatch in enemy/speed list length")
        return

    for i in range(len(enemies)):
        enemies[i].x -= speeds[i]

        # Respawn enemy to the right if it moves off screen
        if enemies[i].right < 0:
            enemies[i].x = random.randint(SCREEN_WIDTH + 100, SCREEN_WIDTH + 300)
            enemies[i].y = random.randint(50, SCREEN_HEIGHT - 50)
            speeds[i] = random.randint(9,12)  # Still faster than background scroll

    # Debug output (can comment out after testing)
    # print([enemy.x for enemy in enemies]) 



def check_enemy_collisions(player, enemies, speeds, lives):
    i = 0
    while i < len(enemies):
        if player.colliderect(enemies[i]):
            del enemies[i]
            del speeds[i]  # Remove corresponding speed!
            lives -= 1
        else:
            i += 1
    return lives

def draw_enemies(screen, enemies, enemy_sprite):
    for enemy in enemies:
        screen.blit(enemy_sprite, enemy)
