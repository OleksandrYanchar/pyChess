import pygame
from pieces_txt import *
from checks import check_options

pygame.font.init()

HEIGHT = 900
WIDTH = 1000
fps = 60
turn_step = 0
selection = 100
valid_moves = []
counter = 0
winner = ''
game_over = False

screen = pygame.display.set_mode([WIDTH, HEIGHT])
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)