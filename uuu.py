import pygame


import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("HAPPY BIRTHDAY!")

# Load images
try:
    whole_cake_img = pygame.image.load('whole_cake.png')
    cut_cake_img = pygame.image.load('cut_cake.png')

    # Scale images to fit the screen
    whole_cake_img = pygame.transform.scale(whole_cake_img, (400, 300))
    cut_cake_img = pygame.transform.scale(cut_cake_img, (400, 300))

except pygame.error as e:
    print(f"Error loading images: {e}")
    sys.exit()

# Set up fonts
font = pygame.font.Font(None, 72)
message_font = pygame.font.Font(None, 36)

# Initial state
cake_state = "whole"

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cake_state == "whole":
                cake_state = "cut"

    # Clear the screen
    screen.fill(WHITE)

    # Render text messages
    happy_bday_text = font.render("HAPPY BIRTHDAY BACCHA ", True, PURPLE)
    instruction_text = message_font.render("LETS CUT THE CAKE BABY", True, PURPLE)

    # Get the rectangle for the text to center it
    text_rect = happy_bday_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
    instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))

    # Display the current cake image
    cake_rect = whole_cake_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    if cake_state == "whole":
        screen.blit(whole_cake_img, cake_rect)
    else:
        screen.blit(cut_cake_img, cake_rect)
        # Change instruction after cutting
        instruction_text = message_font.render("ENJOY YOUR CAKE JANNU!", True, PURPLE)
        instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))


    # Blit the text to the screen
    screen.blit(happy_bday_text, text_rect)
    screen.blit(instruction_text, instruction_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
