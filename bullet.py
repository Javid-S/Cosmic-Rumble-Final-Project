# bullet.py
# This file handles firing bullets, moving them, drawing them,
# and checking if they hit any enemies.

import pygame
import random

def fire_bullets(bullet_timer, bullets, player, enemies, enemy_speeds, score, bullet_img):
    """
    Fires bullets using an image. Bullets move right and hit enemies.
    """
    bullet_timer += 1

    # Fire a bullet every few frames
    if bullet_timer > 7:
        bullet_rect = pygame.Rect(player.right, player.centery - 6, 20, 12)
        bullets.append({'rect': bullet_rect, 'img': bullet_img})
        bullet_timer = 0

    # Move bullets and check collisions
    for bullet in bullets[:]:
        bullet['rect'].x += 10  # Move right

        # Check for collision with enemies
        for i, enemy in enumerate(enemies):
            if bullet['rect'].colliderect(enemy):
                if bullet in bullets:
                    bullets.remove(bullet)
                # Reset enemy position and speed
                enemy.x = 800 + random.randint(0, 500)
                enemy.y = random.randint(50, 550)
                enemy_speeds[i] = random.uniform(1.5, 2.5)
                score += 1
                break

    return bullet_timer, bullets, score


def draw_bullets(screen, bullets):
    """
    Draws all bullets using their images.
    """
    for bullet in bullets:
        screen.blit(bullet['img'], bullet['rect'])
