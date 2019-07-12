from src.button import Button
import src.draw as draw


class PlayerPanel:

    def __init__(self, x: int, y: int, player, teams: tuple):
        self.x = x
        self.y = y
        self.player = player
        self.teams = teams
        self.team_score_button = Button(x + 20, y + 30 + 22, "+ Team score", 13, (17, 16, 255, 255),
                                        True, True, (160, 160, 160, 255))
        self.team_score_button2 = Button(x + 20, y + 30, "- Team score", 13, (16, 16, 255, 255),
                                         True, True, (160, 160, 160, 255))
        self.suspend_button = Button(x + 20, y + 30 - 22, "Suspend", 13, (200, 16, 16, 255),
                                     True, True, (160, 160, 160, 255))
        self.release_button = Button(x + 20, y + 30 - 44, "Release", 13, (16, 235, 16, 255),
                                     True, True, (160, 160, 160, 255))
        self.yellow_card_button = Button(x + 20, y + 30 - 66, "+ Yellow card", 13, (255, 255, 17, 255),
                                         True, True, (160, 160, 160, 255))
        self.yellow_button2 = Button(x + 20, y + 30 - 88, "- Yellow card", 13, (255, 255, 16, 255),
                                     True, True, (160, 160, 160, 255))
        self.red_card_button = Button(x + 20, y + 30 - 110, "+ Red card", 13, (255, 16, 17, 255),
                                      True, True, (160, 160, 160, 255))
        self.red_button2 = Button(x + 20, y + 30 - 132, "- Red card", 13, (255, 16, 16, 255),
                                  True, True, (160, 160, 160, 255))
        self.disqualify_button = Button(x + 20, y + 30 - 154, "Disqualify", 13, (120, 64, 64, 255),
                                        True, True, (160, 160, 160, 255))
        self.buttons = (
            self.team_score_button,
            self.team_score_button2,
            self.suspend_button,
            self.release_button,
            self.yellow_card_button,
            self.yellow_button2,
            self.red_card_button,
            self.red_button2,
            self.disqualify_button
        )
        self.width = 145
        self.height = 23 * len(self.buttons)

    def render(self):
        draw.rect(self.x + 14, self.y - 15 * (len(self.buttons)), self.width, self.height, (205, 200, 205, 255))
        for button in self.buttons:
            button.render()

    def update(self, x: int, y: int, timer) -> bool:  # returns bool to not check for other buttons bellow the panel
        if not self.player.disqualified:
            if self.buttons[0].pressed(x, y):
                if self.player.team_score(True):  # if the player could actually get a score
                    for i, team in enumerate(self.teams):
                        for player in self.teams[i].players:
                            if player == self.player:
                                self.teams[i].score_up()
                return True
            elif self.buttons[1].pressed(x, y):
                if self.player.team_score(False):  # if the player could actually get a score
                    for i, team in enumerate(self.teams):
                        for player in self.teams[i].players:
                            if player == self.player:
                                self.teams[i].score_down()
                return True
            elif self.buttons[2].pressed(x, y):
                self.player.suspend(timer)
                return True
            elif self.buttons[3].pressed(x, y):
                self.player.release()
                return True
            elif self.buttons[4].pressed(x, y):
                self.player.give_card("yellow")
                return True
            elif self.buttons[5].pressed(x, y):
                self.player.take_away_card("yellow")
                return True
            elif self.buttons[6].pressed(x, y):
                self.player.give_card("red")
                return True
            elif self.buttons[7].pressed(x, y):
                self.player.take_away_card("red")
                return True
            elif self.buttons[8].pressed(x, y):
                self.player.disqualify()
                self.player.release()
                return True
        return False

    def get_buttons(self) -> tuple:
        return self.buttons
