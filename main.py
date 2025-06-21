import pygame
import random
import os

from player import handle_player_movement, clamp_player
from enemy import create_enemies, move_enemies, check_enemy_collisions, draw_enemies
from bullet import fire_bullets, draw_bullets
from ui import draw_ui
from boss import create_boss, move_boss, fire_boss_bullets, update_boss_bullets, draw_boss_health_bar
from menu import title_screen, world_select_screen, main_menu_screen
from pause import draw_pause_menu
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT
from assets.asset_loader import load_assets

# --- Setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("World Shooter")
clock = pygame.time.Clock()

# Load default font for early screens
pixel_font_path = os.path.join("assets", "default", "font.ttf")
pixel_font = pygame.font.Font(pixel_font_path, 32)

# --- Title and World Selection ---
state = title_screen(screen, pixel_font)
if state == "quit":
    pygame.quit()
    exit()

while True:
    state, selected_world = world_select_screen(screen, pixel_font)
    if state == "quit":
        pygame.quit()
        exit()

    assets = load_assets(selected_world)
    font = assets.get('font', pixel_font)

    while True:
        action = main_menu_screen(screen, font)
        if action == "quit":
            pygame.quit()
            exit()
        elif action == "change":
            break  # back to world selection
        else:
            break  # continue to game

    # --- Game Setup ---
    player = pygame.Rect(50, 250, PLAYER_WIDTH, PLAYER_HEIGHT)
    enemies, enemy_speeds = create_enemies(5)
    bullets = []

    lives = 3
    score = 0
    bullet_timer = 0

    boss_rect, boss_image, boss_direction = create_boss(assets['boss'])
    boss_bullets = []
    boss_bullet_timer = 0
    boss_active = False
    boss_max_health = 50
    next_boss_score = 50

    bullet_img = pygame.transform.scale(assets['bullet'], (25, 12))

    boss_bullet_img = pygame.transform.scale(assets['boss_bullet'], (100, 40))


    original_bg = assets['background']
    bg_width = original_bg.get_width()
    background = pygame.transform.scale(original_bg, (bg_width, SCREEN_HEIGHT))
    bg_x = 0
    bg_scroll_speed = 4.0

    start_ticks = pygame.time.get_ticks()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                result = draw_pause_menu(screen, font)
                if result == "resume":
                    continue
                elif result == "quit_world":
                    running = False
                    break
                elif result == "quit_game":
                    pygame.quit()
                    exit()

        clock.tick(60)

        # Background Scroll
        bg_x -= bg_scroll_speed
        if bg_x <= -bg_width:
            bg_x = 0
        screen.blit(background, (bg_x, 0))
        screen.blit(background, (bg_x + bg_width, 0))

        # Player
        keys = pygame.key.get_pressed()
        handle_player_movement(keys, player)
        clamp_player(player)

        # Enemy logic
        if not boss_active:
            if pygame.time.get_ticks() - start_ticks > 1000:
                move_enemies(enemies, enemy_speeds)
                lives = check_enemy_collisions(player, enemies, enemy_speeds, lives)
                if len(enemies) < 5:
                    needed = 5 - len(enemies)
                    new_enemies, new_speeds = create_enemies(needed)
                    enemies.extend(new_enemies)
                    enemy_speeds.extend(new_speeds)

        if lives <= 0 and score > 0:
            break

        # Bullets
        bullet_timer, bullets, score = fire_bullets(
            bullet_timer, bullets, player, enemies, enemy_speeds, score, bullet_img
        )

        draw_enemies(screen, enemies, assets['enemy'])
        draw_bullets(screen, bullets)

        # Boss Logic
        if score >= next_boss_score and not boss_active:
            boss_active = True
            boss_max_health = int(boss_max_health * 1.5)
            boss_health = boss_max_health
            next_boss_score += 100

        if boss_active:
            boss_rect, boss_direction = move_boss(boss_rect, boss_direction)
            boss_bullets, boss_bullet_timer = fire_boss_bullets(
                    boss_rect, boss_bullets, boss_bullet_timer, boss_bullet_img)

            boss_bullets, lives = update_boss_bullets(boss_bullets, screen, player, lives)

            screen.blit(boss_image, boss_rect)
            draw_boss_health_bar(screen, boss_rect, boss_health, boss_max_health, boss_image)

            for bullet in bullets[:]:
                if bullet['rect'].colliderect(boss_rect):
                    bullets.remove(bullet)
                    boss_health -= 1

            if boss_health <= 0:
                boss_active = False
                boss_rect.x = -200
                enemies, enemy_speeds = create_enemies(5)

        # Player and UI
        screen.blit(assets['player'], player)
        draw_ui(screen, font, lives, score)
        pygame.display.update()

    print("Game Over! Your score:", score)
    pygame.time.delay(1000)
