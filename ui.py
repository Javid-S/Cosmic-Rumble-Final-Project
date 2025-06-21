import pygame

def draw_ui(screen, font, lives, score, selected_world=None):  # selected_world no longer used
    # Set smaller font
    small_font = pygame.font.Font(font.get_name(), 24) if hasattr(font, 'get_name') else font

    # Draw lives (top-left)
    lives_text = small_font.render(f"Lives: {lives}", True, (255, 255, 255))
    screen.blit(lives_text, (10, 10))

    # Draw score (top-right)
    score_text = small_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (screen.get_width() - score_text.get_width() - 10, 10))
