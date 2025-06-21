# worlds.py
# This file helps manage all the different worlds and their images

import pygame
import os

# Set up the path to the 'assets' folder
ASSETS_PATH = os.path.join(os.path.dirname(__file__), 'assets')

# List of all available worlds and where to find them
WORLDS = {
    "elf_world": os.path.join(ASSETS_PATH, "elf_world"),
    "tech_world": os.path.join(ASSETS_PATH, "tech_world"),
    "cyber_hell_world": os.path.join(ASSETS_PATH, "cyber_hell_world")
}

def load_image(path):
    # Loads an image from the given path, returns None if it fails
    try:
        return pygame.image.load(path).convert_alpha()
    except Exception as e:
        print(f"Failed to load image at {path}: {e}")
        return None

def load_assets_for_world(world_name):
    """
    Loads and returns all images (sprites/backgrounds) needed for a specific world.
    The returned dictionary will have keys like 'player', 'enemy', etc.
    """
    world_path = WORLDS.get(world_name)
    if not world_path:
        raise ValueError(f"World '{world_name}' not found.")

    assets = {
        "player": load_image(os.path.join(world_path, "player.png")),
        "enemy": load_image(os.path.join(world_path, "enemy.png")),
        "bullet": load_image(os.path.join(world_path, "bullet.png")),
        "boss": load_image(os.path.join(world_path, "boss.png")),
        "boss_bullet": load_image(os.path.join(world_path, "boss_bullet.png")),
        "background": load_image(os.path.join(world_path, "background.png")),
    }

    return assets

def get_world_list():
    # Just returns a list of all available world names
    return list(WORLDS.keys())
