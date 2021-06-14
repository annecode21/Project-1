import pygame.font

class AlphaButton:
    def __init__(self, gDrug_game):
        #Button dimensions and properties
        self.screen = gDrug_game.screen
        self.settings = gDrug_game.settings
        self.colour = self.settings.button_colour
        self.font = self.settings.button_font
        self.text = self.settings.text_colour
       
        #Create a circle rect at (0,0) and then set the correct position
        self.rect = pygame.Rect (0,0, self.settings.screen_width, self.settings.screen_height)
        self.rect.midtop = gDrug_game.ship.rect.midtop #setting position to match the ship's midtop   
        

    def draw_button(self):
        pygame.draw.circle(self.screen, self.settings.button_colour, self.settings.center_point, self.settings.button_radius) 
        
    def button_setup(self):
        increase = round(self.settings.screen_width / 13)
        self.buttons()
        for i in range(26):
            if i < 13:
                y = 40
                x = 25 + (increase * i)
            else:
                x = 25 + (increase * (i - 13))
                y = 85
            self.buttons.append([self.settings.button_colour, x, y, 20, True, 65 + i])
            #buttons.append([color, x_pos, y_pos, radius, visible, char])

   