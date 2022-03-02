import classes

pA = classes.Character('A')
pB = classes.Character('B')

for turn in range(1, 100):
    pA.attack(pB, turn)
    pB.attack(pA, turn)



