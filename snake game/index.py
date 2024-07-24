import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
width = 500
height = 400
screen = pygame.display.set_mode((width, height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Font for score
font_style = pygame.font.SysFont(None, 25)
