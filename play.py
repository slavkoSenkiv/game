import classes

pA = classes.Character('A')
pB = classes.Character('B')

print(pA.name, pA.damage, pA.hp)
print(pB.name, pB.damage, pB.hp)

while pA.lives or pB.lives:
    pA.attack(pB)
    pB.attack(pA)



