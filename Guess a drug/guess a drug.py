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
        self.alpha_button = AlphaButton(self)


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

    def _buttonHit(self, x , y):
        for i in range(len(self.settings.buttons)):
            if x < self.settings.buttons[i][1] + 20 and x > self.settings.buttons[i][1] - 20:
                if y < self.settings.buttons[i][2] + 20 and y > self.settings.buttons[i][2] - 20:
                    return self.settings.buttons[i][5]
        return None     

    def _check_alpha(self):
        spaced = self.spacedOut(self.settings.word, self.settings.guessed)
        label1 = self.settings.guess_font.render(spaced, 1, self.settings.BLACK)
        rect = label1.get_rect()
        length = rect[2]

        self.screen.blit(label1,(self.settings.screen_width/2 - length/2, 400))

        pic = self.settings.hangman_picts[self.settings.limbs]
        self.screen.blit(pic, (self.settings.screen_width/2 - pic.get_width()/2 + 20, 150))

        clickPos = pygame.mouse.get_pos()
        letter = self._buttonHit(clickPos[0], clickPos[1])
        if letter != None:
            self.settings.guessed.append(chr(letter))
            self.settings.buttons[letter - 65][4] = False
            if self.hang(chr(letter)):
                if self.settings.limbs != 5:
                    self.settings.limbs += 1
                else:
                    end()
            else:
                print(self.spacedOut(self.settings.word, self.settings.guessed))
                if self.spacedOut(self.settings.word, self.settings.guessed).count('_') == 0:
                    end(True)
    
    def hang(self, guess):
        if guess.lower() not in self.settings.word.lower():
            return True
        else:
            return False

    def rand_drug_selection(self):
        i = random.randint(0, len(self.drug.name) -1)
        self.drug = self.drug.name[i]
    


    def _check_keydown_events(self, event):
        #Respond to key presses
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _update_screen(self):
        #Update the images on the screen and glip to the new screen
        self.screen.fill(self.settings.bg_colour)
        
        #Draw the play button 
        self.alpha_button.draw_button()

    def spacedOut(self, word, guessed=[]):
        spacedWord = ''
        guessedLetters = guessed
        for x in range(len(word)):
            if word[x] != ' ':
                spacedWord += '_ '
                for i in range(len(guessedLetters)):
                    if word[x].upper() == guessedLetters[i]:
                        spacedWord = spacedWord[:-2]
                        spacedWord += word[x].upper() + ' '
            elif word[x] == ' ':
                spacedWord += ' '
        return spacedWord

    def end(self, winner=False):
        lostTxt = 'You Lost, press any key to play again...'
        winTxt = 'Yay!, press any key to play again...'
        self._draw_game_window()
        pygame.time.delay(1000)
        self.screen.fill(self.settings.WHITE)

        if winner == True:
            label = self.settings.lost_font.render(winTxt, 1, self.settings.BLACK)
        else:
            label = self.settings.lost_font.render(lostTxt, 1, self.settings.BLACK)

        wordTxt = self.settings.lost_font.render(self.settings.word.upper(), 1, self.settings.BLACK)
        wordWas = self.settings.lost_font.render('The drug was: ', 1, self.settings.BLACK)
        urlLink = self.settings.lost_font.render('Learn about the drug here: ', 1, self.settings.BLACK)
        url_link = self.settings.lost_font.render(link, 1, self.settings.BLACK)

        self.screen.blit(wordTxt, (self.settings.screen_width/2 - wordTxt.get_width()/2, 295))
        self.screen.blit(wordWas, (self.settings.screen_width/2 - wordWas.get_width()/2, 245))
        self.screen.blit(urlLink, (self.settings.screen_width/2 - urlLink.get_width()/2, 400))
        self.screen.blit(label, (self.settings.screen_width / 2 - label.get_width() / 2, 140))
        self.screen.blit(url_link, (self.settings.screen_width/2 - url_link.get_width()/2, 450))

        pygame.display.update()
            

if __name__ == '__main__':
    #Make a game instance, and run the game
    gDrug = GuessADrug()
    gDrug.run_game() 