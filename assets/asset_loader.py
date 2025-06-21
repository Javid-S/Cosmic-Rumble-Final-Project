import pygame
import os
import settings  # Assuming settings.py is accessible

def load_assets(world_name):
    world_path = os.path.join("assets", world_name)
    assets = {}

    try:
        # --- Load and scale images to match object sizes from settings.py ---

        # Player: scaled to fit PLAYER_WIDTH x PLAYER_HEIGHT
        player_img = pygame.image.load(os.path.join(world_path, "player.png")).convert_alpha()
        assets["player"] = pygame.transform.scale(player_img, (settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT))

        # Enemy: scaled to fit ENEMY_WIDTH x ENEMY_HEIGHT
        enemy_img = pygame.image.load(os.path.join(world_path, "enemy.png")).convert_alpha()
        assets["enemy"] = pygame.transform.scale(enemy_img, (settings.ENEMY_WIDTH, settings.ENEMY_HEIGHT))

        # Bullet: scaled to fit BULLET_WIDTH x BULLET_HEIGHT
        bullet_img = pygame.image.load(os.path.join(world_path, "bullet.png")).convert_alpha()
        assets["bullet"] = pygame.transform.scale(bullet_img, (settings.BULLET_WIDTH, settings.BULLET_HEIGHT))

        # Boss: scaled to fit BOSS_WIDTH x BOSS_HEIGHT
        boss_img = pygame.image.load(os.path.join(world_path, "boss.png")).convert_alpha()
        original_width = boss_img.get_width()
        original_height = boss_img.get_height()

        # Calculate scale factor to fit within max width or height
        scale_factor = min(settings.BOSS_WIDTH / original_width, settings.BOSS_HEIGHT / original_height)

        # Apply proportional scaling
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)

        assets["boss"] = pygame.transform.scale(boss_img, (new_width, new_height))

            # Boss bullet: keep as-is
        boss_bullet_img = pygame.image.load(os.path.join(world_path, "boss_bullet.png")).convert_alpha()
        assets["boss_bullet"] = boss_bullet_img

        # Background: scale height to screen, keep original width
        bg_img = pygame.image.load(os.path.join(world_path, "background.png")).convert()
        scaled_bg = pygame.transform.scale(bg_img, (bg_img.get_width(), settings.SCREEN_HEIGHT))
        assets["background"] = scaled_bg

        # Load custom font if available
        font_path = os.path.join(world_path, "font.ttf")
        if os.path.exists(font_path):
            assets["font"] = pygame.font.Font(font_path, settings.FONT_SIZE)
        else:
            print(f"[Warning] No font.ttf found for world '{world_name}'")

    except Exception as e:
        print(f"[Error] Failed to load assets for {world_name}: {e}")

    return assets
