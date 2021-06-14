import pygame.font

class Settings:
    #A class to store all game settings
    def __init__(self):
        #Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_colour = (230,230,230)

        #hangman picts
        self.hangman_picts = [pygame.image.load('hangman0.png'), pygame.image.load('hangman1.png'), pygame.image.load('hangman2.png'), pygame.image.load('hangman3.png'), pygame.image.load('hangman4.png'), pygame.image.load('hangman5.png'), pygame.image.load('hangman6.png')]
        self.limbs = 0

        #colour
        self.BLACK = (0,0, 0)
        self.WHITE = (255,255,255)
        self.RED = (255,0, 0)
        self.GREEN = (0,255,0)
        self.BLUE = (0,0,255)
        self.LIGHT_BLUE = (102,255,255)

        self.buttons = []
        self.guessed = []

        self.word = ''

        #button settings
        self.button_font = pygame.font.SysFont("arial", 20)
        self.button_colour = (102,255,255)
        self.text_colour = (0,0,0)
        self.button_radius = 20
        self.center_point = (20,20)