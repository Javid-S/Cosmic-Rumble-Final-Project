# boss.py
# Handles the boss character: creating it, moving it, firing bullets, updating bullets, and health bar.

import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

def create_boss(boss_image):
    # Make the boss image bigger
    boss_image = pygame.transform.scale(boss_image, (boss_image.get_width() * 2, boss_image.get_height() * 2))
    boss_rect = boss_image.get_rect()
    boss_rect.x = SCREEN_WIDTH - boss_rect.width - 20
    boss_rect.y = SCREEN_HEIGHT // 2 - boss_rect.height // 2
    return boss_rect, boss_image, 1  # 1 = moving down initially

def move_boss(boss, direction):
    boss.y += direction * 3
    if boss.top <= 0 or boss.bottom >= SCREEN_HEIGHT:
        direction *= -1
    return boss, direction

def fire_boss_bullets(boss, boss_bullets, boss_bullet_timer, boss_bullet_img):
    boss_bullet_timer += 1

    if boss_bullet_timer > 30:
        bullet_rect = boss_bullet_img.get_rect()
        bullet_rect.center = (boss.left, boss.centery)

        boss_bullets.append({
            'rect': bullet_rect,
            'img': boss_bullet_img,
            'dx': -8,
            'dy': random.choice([-4, -2, 2, 4])
        })

        boss_bullet_timer = 0

    return boss_bullets, boss_bullet_timer

def update_boss_bullets(boss_bullets, screen, player, lives):
    for bullet in boss_bullets[:]:
        bullet['rect'].x += bullet['dx']
        bullet['rect'].y += bullet['dy']

        screen.blit(bullet['img'], bullet['rect'])

        if bullet['rect'].colliderect(player):
            boss_bullets.remove(bullet)
            lives -= 1
        elif bullet['rect'].right < 0 or bullet['rect'].top < 0 or bullet['rect'].bottom > SCREEN_HEIGHT:
            boss_bullets.remove(bullet)

    return boss_bullets, lives

def draw_boss_health_bar(screen, boss, health, max_health, boss_image):
    bar_width = boss_image.get_width()
    bar_height = 10
    health_ratio = health / max_health
    health_bar_width = int(bar_width * health_ratio)

    bg_rect = pygame.Rect(boss.x, boss.y - 15, bar_width, bar_height)
    pygame.draw.rect(screen, (100, 100, 100), bg_rect)

    health_rect = pygame.Rect(boss.x, boss.y - 15, health_bar_width, bar_height)
    pygame.draw.rect(screen, (0, 255, 0), health_rect)
