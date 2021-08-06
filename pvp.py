# here list values represent player characteristics
# player = [0 health,  1 defence, 2 damage, 3 name]
player_A = [1000, 50, 200, 'player_A']
player_B = [1000, 50, 300, 'player_B']


def hp_left(attacker, victim):
    # this function calculate the attacked player HP los
    # attacked_player_HP = attacked_player_HP - attacking_player_damage
    # attacking_player_damage = attacking_player_attack * (100/(100 + attacked_player_defence))

    damage = attacker[2] * (100/(100 + victim[1]))
    print(f'the damage from {attacker[3]} to {victim[3]} = {int(damage)}')

    victim[0] = int(victim[0] - damage)
    print(f'{victim[3]} HP = {victim[0]}\n')

    return victim[0]


def who_won(player_a, player_b):
    # this function checks if someone win and who exactly
    # if player1's HP <= 0 then player2 is winner
    if player_a[0] <= 0:
        won = player_b
        print(f'won {won[3]}')
        exit()

    if player_b[0] <= 0:
        won = player_a
        print(f'won {won[3]}')
        exit()


print('player_A = ', player_A)
print('player_B = ', player_B, '\n')

while player_B[0] >= 0 or player_A[0] >= 0:

    hp_left(player_A, player_B)
    who_won(player_A, player_B)

    hp_left(player_B, player_A)
    who_won(player_A, player_B)


