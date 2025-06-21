# assets.py
# This file loads all the pictures and fonts we need for the game based on the selected world

import os
import pygame

# We'll store all the loaded images and fonts here so we can get them later
loaded_images = {}
loaded_fonts = {}

# These are the types of images we want to load from the folder
SPRITE_NAMES = [
    "player",        # the main character
    "enemy",         # regular enemies
    "boss",          # big enemy
    "bullet",        # player bullets
    "boss_bullet",   # boss bullets
    "background"     # background image
]

def load_world_assets(world_name):
    """
    This function loads all the images and font for a specific world.
    It looks in the 'assets/world_name' folder and grabs whatever it can.
    """
    global loaded_images, loaded_fonts

    # This is the folder where this world's stuff is stored
    base_path = os.path.join("assets", world_name)

    # --- Load all the images ---
    images = {}
    for name in SPRITE_NAMES:
        image_path = os.path.join(base_path, f"{name}.png")
        if os.path.exists(image_path):
            # load image with transparent background
            images[name] = pygame.image.load(image_path).convert_alpha()
        else:
            # tell us if something is missing (not a big deal, just helpful)
            print(f"[Warning] Missing {name}.png in {world_name}")

    # Save the images in the global dictionary
    loaded_images = images

    # --- Load the font (if there's one) ---
    font_path = os.path.join(base_path, "font.ttf")
    if os.path.exists(font_path):
        try:
            font = pygame.font.Font(font_path, 32)  # try to load custom font
        except Exception as e:
            print(f"[Error] Couldn't load custom font: {e}")
            font = pygame.font.SysFont("arial", 32)  # fallback if broken
    else:
        print(f"[Info] No custom font found for {world_name}, using default.")
        font = pygame.font.SysFont("arial", 32)

    # Save the font too
    loaded_fonts["main"] = font

def get_image(name):
    """
    Just get the image we already loaded earlier.
    """
    return loaded_images.get(name)

def get_font():
    """
    Return the current font for the selected world.
    """
    return loaded_fonts.get("main")
