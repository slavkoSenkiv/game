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
dct = char_stats_sheet.get_all_records()
print(dct)
# </editor-fold>


class Character:
    def __init__(self, name):
        for character in dct:
            if name == character['name']:
                self.name = character['name']
                self.hp = character['hp']
                self.damage = character['dmg']

    def attack(self, target, turn):
        target.hp = target.hp - self.damage * random.randint(1, 10)
        logs_sheet.update(f'{self.name}{turn + 1}', self.hp)

        if target.hp <= 0:
            print(target.name, 'lost')
            exit()



