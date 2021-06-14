import sys
import pygame
import random
from settings import Settings
from alpha_button import AlphaButton
from drug import Drug


class GuessADrug:
    #Overall class to manage game functions
    def __init__(self):
        #initialize python
        pygame.init()
        
        #setting up screen
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

        #title and icon
        pygame.display.set_caption('Guess a drug!')
        icon = pygame.image.load('medicine.png')
        pygame.display.set_icon(icon)

        self.drug = Drug()
        self.alpha_button = AlphaButton()


    def run_game(self):
        #start the main loop of the game
        while True:
            self._draw_game_window()
            self._update_screen()
            self._check_events()

    def _check_events(self):
        #Respond to keypresses and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_alpha (mouse_pos)

    def _draw_game_window(self):
        self.alpha_button
        self.settings.hangman_picts
        self._update_screen() 


    def _rand_drug_selection(self):
        i = random.randint(0, len(self.drug.name)-1)
        drug = rand_drug_list[i]
        drug_name = drug.name.upper()
        return drug_name
    


    def _check_keydown_events(self, event):
        #Respond to key presses
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _update_screen(self):
        #Update the images on the screen and glip to the new screen
        self.screen.fill(self.settings.bg_colour)
        
        #Draw the play button 
        self.alpha_button.draw_button()


            

if __name__ == '__main__':
    #Make a game instance, and run the game
    gDrug = GuessADrug()
    gDrug.run_game() 