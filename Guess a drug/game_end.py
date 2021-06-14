class GameEnd:

    def __init__(self, gDrug_game):
        self.settings = gDrug_game.settings
        self.reset_game()

        #Start game in inactive state
        self.game_active = False

    def reset_game(self):
        game_won = True