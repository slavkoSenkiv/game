# <editor-fold desc="default">
import random
import gspread
gs_name = 'turn based combat'
path_to_gspread_credentials_json = '/Users/ysenkiv/.config/gspread/credentials.json'
path_to_gspread_authorized_user = '/Users/ysenkiv/.config/gspread/authorized_user.json'
gc = gspread.oauth()
gs = gc.open(gs_name)
char_stats_sheet = gs.get_worksheet(0)
logs_sheet = gs.get_worksheet(1)
chat_stats_dict = char_stats_sheet.get_all_records()
print(chat_stats_dict)
# </editor-fold>


class Character:
    def __init__(self, name):
        for character in chat_stats_dict:
            if name == character['name']:
                self.name = character['name']
                self.hp = character['hp']
                self.damage = character['dmg']
                self.lives = True

    def attack(self, target):
        target.hp = target.hp - self.damage

        if target.hp <= 0:
            self.lives = False
            print(target.name, 'lost')



