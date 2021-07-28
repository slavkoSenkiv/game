# player = [0 health,  1 defence, 2 damage]
player_A = [1000, 50, 200, 'player_A']
player_B = [1000, 50, 300, 'player_B']


def damage(attacker, victim):
    # damage = attack * (100/(100 + defence))
    # hpLost = hpLost - damage
    victim[0] = victim[0] - (attacker[2] * (100/(100 + victim[1])))
    return victim[0]

def whoWon(playerA, playerB):
    if playerA[0] <= 0:
        won = playerA
        print(f'won {won[3]}')

    if playerB[0] <= 0:
        won = playerB
        print(f'won {won[3]}')



print('player_A = ', player_A)
print('player_B = ', player_B, '\n')


while player_B[0] >= 0 or player_A[0] >= 0:
    print('here goes damage from A to B')
    damage(player_A, player_B)
    whoWon(player_A, player_B)
    print('player_B = ', player_B)

    print('here goes damage from B to A')
    damage(player_B, player_A)
    whoWon(player_A, player_B)
    print('player_A = ', player_A, '\n')


